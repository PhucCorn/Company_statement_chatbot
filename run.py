from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()
# Thông tin cần thiết
api_id = os.getenv('API_ID')      # Thay thế bằng API ID của bạn
api_hash =  os.getenv('API_HASH')  # Thay thế bằng API Hash của bạn
bot_token = os.getenv('BOT_TOKEN') # Thay thế bằng API Token của bạn

# Tạo một client cho bot
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token) 

# Đăng ký sự kiện để nhận tin nhắn mới
@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = await event.get_sender()
    sender_name = sender.first_name if sender else 'người dùng vô danh'
    message = event.message.message

    print(f'Nhận tin nhắn từ {sender_name}: {message}')

    # Trả lời tin nhắn
    # await event.respond(f'Xin chào {sender_name}, bạn đã gửi: {message}')
    await event.respond("Sứ mệnh của chúng tôi là đồng hành đem lại sự thịnh vượng cho khách hàng thông qua các giải pháp bao bì, đóng gói tiên tiến và hiệu quả, không chỉ giúp bảo vệ an toàn sản phẩm, đem lại sự thuận tiện trong bốc xếp, vận chuyển, lưu kho, mà còn hỗ trợ đắc lực khách hàng nâng tầm hình ảnh thương hiệu.")


# Chạy client
print("Bot đang chạy...")
client.run_until_disconnected()
