from pymongo import MongoClient
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from operator import itemgetter
from util import *
from langchain_core.runnables import RunnableLambda

class AIAssistant:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o-mini-2024-07-18")
        self.parser = StrOutputParser()
        
    def llm_memory(self):
        trimmer = trim_messages(
            max_tokens=54,
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
        history = get_session_history_mongodb(session_id)
        for message in history.messages:
            print(f"{message.type}: {message.content}")
        with_message_history = RunnableWithMessageHistory(
            chain,
            get_session_history_mongodb,
            input_messages_key="question", #Which key is user's input
        )
        result = with_message_history.invoke(
            {
                "question": [HumanMessage(content=question)],
                "doc": """Doanh nghiệp này tên là Bao Bì Ánh Sáng và đây loại doanh nghiệp sản xuất."""
            },
            config=config,
        )
        return result