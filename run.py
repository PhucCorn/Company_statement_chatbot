from telethon import TelegramClient, events
from dotenv import load_dotenv
import openai
import os
from pymongo import MongoClient
import datetime
import time as t
from pipeline import AIAssistant

load_dotenv()
api_id = os.getenv('API_ID')      
api_hash =  os.getenv('API_HASH') 
bot_token = os.getenv('BOT_TOKEN')
openai.api_key = os.getenv("OPENAI_API_KEY")
text_gen = AIAssistant()
dbclient = MongoClient('mongodb://localhost:27017/')
db = dbclient['company_statement_chat_database']
client = TelegramClient('bot', api_id, api_hash, timeout=50).start(bot_token=bot_token)

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
async def handle_new_message(event, stream=False):
    #Collect information from message
    sender = await event.get_sender()
    time = datetime.datetime.now()
    message = event.message.message
    session_id = sender.username
    #Gen the answer
    print(f'Nhận tin nhắn từ {session_id}: {message}')
    if not stream:
        initial_message = await event.respond("Đang sinh câu trả lời...")
        answer = text_gen.invoke(message, session_id)
        await client.edit_message(event.chat_id, initial_message, answer)
    else:
        initial_message = await event.respond("Đang sinh câu trả lời...")
        complete_response = ""
        answer_gen, dict_input, config = text_gen.stream(message, session_id)
        answer_stream_list = list(answer_gen.stream(dict_input, config=config))
        total_chunks = len(answer_stream_list)  
        for i, chunk in enumerate(answer_stream_list):
            try:
                complete_response += chunk
                if chunk == "" or chunk == " ":
                    continue
                if (i % 5 == 0) or (i == total_chunks - 1):
                    await client.edit_message(event.chat_id, initial_message, complete_response)
                    t.sleep(1)
            except Exception as e:
                await event.respond('Đã xảy ra lỗi trong quá trình sinh câu trả lời')
                break
                
    #Update log and database
    update_conversations(session_id, "", time)
    

#.\env\Scripts\activate
# Chạy client

print("Bot đang chạy...")
client.run_until_disconnected()
