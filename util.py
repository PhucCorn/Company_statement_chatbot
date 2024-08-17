from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory

def get_session_history_mongodb(session_id):
    return MongoDBChatMessageHistory(
        'mongodb://localhost:27017/', 
        session_id, 
        database_name="chat_database", 
        collection_name="messages"
    )