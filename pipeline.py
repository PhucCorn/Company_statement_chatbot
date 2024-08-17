from pymongo import MongoClient
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,
    trim_messages,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from operator import itemgetter
from util import *

class AIAssistant:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o-mini-2024-07-18")
        self.parser = StrOutputParser()
        
    def llm_memory(self):
        trimmer = trim_messages(
            max_tokens=500,
            strategy="last",
            token_counter=self.model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )
        query = {'username': 'phuccngo'}
        dbclient = MongoClient('mongodb://localhost:27017/')
        db = dbclient['chat_database']
        conversations_collection = db['messages']
        result = conversations_collection.find_one(query)
        return trimmer
    
    def prompt_gen(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """Bạn là AI Chatbot của Công ty CP TM & SX Bao Bì Ánh Sáng. 
                    Bạn ở đây để trả lời tất cả các câu hỏi về văn hóa doanh nghiệp với các thông tin bạn được cung cấp. 
                    Thông tin được cung cấp: {doc} """,
                ),
                MessagesPlaceholder(variable_name="question"), #phần "messages" bên dưới sẽ được chèn vào đây
            ]
        )
        return prompt
    
    def docs_gen(self, question):
        documents = TextLoader("BBAS.txt", encoding = 'UTF-8').load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(texts, embeddings)
        retriever = vectorstore.as_retriever()
        docs = retriever.invoke(question)
        return "\n\n".join(doc.page_content for doc in docs)

    def invoke(self, question: str, session_id: str) -> str:
        config = {"configurable": {"session_id": session_id}}
        trimmer = self.llm_memory()
        prompt = self.prompt_gen()
        chain = (
            RunnablePassthrough.assign(messages=itemgetter("question") | trimmer)
            | prompt
            | self.model
            | self.parser
        )
        with_message_history = RunnableWithMessageHistory(
            chain,
            get_session_history_mongodb,
            input_messages_key="question", #Which key is user's input
        )
        docs = self.docs_gen(question)
        result = with_message_history.invoke(
            {
                "question": [HumanMessage(content=question)],
                "doc": docs
            },
            config=config,
        )
        return result