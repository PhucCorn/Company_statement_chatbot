from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import datetime
from pipeline import AIAssistant

load_dotenv()
api_id = os.getenv('API_ID')      
api_hash =  os.getenv('API_HASH') 
bot_token = os.getenv('BOT_TOKEN')
text_gen = AIAssistant()
dbclient = MongoClient('mongodb://localhost:27017/')
db = dbclient['chat_database']
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

def update_conversations(session_id, note, time):
    conversations_collection = db["conversations"]
    data = {
        "session_id": session_id,
        'note': note,
        "last_access": time
    }
    conversations_collection.update_one(
        {"session_id": session_id}, 
        {"$set": data},  
        upsert=True  
    )
    return

def insert_messages(session_id, question, answer, time):
    messages_collection = db['messages']
    data = {
        'session_id': session_id,
        'message': [
            {'user_input': question, 'model_response': answer},
        ],
        'timestamp': time
    }
    messages_collection.insert_one(data)
    return

@client.on(events.NewMessage)
async def handle_new_message(event):
    #Collect information from message
    sender = await event.get_sender()
    time = datetime.datetime.now()
    message = event.message.message
    session_id = sender.username
    #Gen the answer
    print(f'Nhận tin nhắn từ {session_id}: {message}')
    answer = text_gen.invoke(message, session_id)
    await event.respond(answer)
    #Update log and database
    update_conversations(session_id, "", time)
    


# Chạy client
print("Bot đang chạy...")
client.run_until_disconnected()
