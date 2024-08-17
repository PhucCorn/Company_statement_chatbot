from langchain.document_loaders import TextLoader
documents = TextLoader("BBAS.txt", encoding = 'UTF-8').load()
print(documents)