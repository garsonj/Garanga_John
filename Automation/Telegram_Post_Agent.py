import os
import schedule
import time
import asyncio
from telegram import Bot
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

# List of messages to cycle through
messages = [
    "💡 Tip 1: Stay consistent in your learning!",
    "📚 Tip 2: Practice makes perfect — never skip coding!",
    "🚀 Tip 3: Automate what you repeat!",
    "🔥 Tip 4: Learning Python opens many doors.",
    "💬 Tip 5: Join dev communities to grow faster.",
    "🧠 Tip 6: Think, code, reflect. Improve every loop.",
]

message_index = 0  # Track which message to send

# Define async message sender
async def send_message(text):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text)
        print(f" Sent: {text}")
    except Exception as e:
        print("Error sending message:", e)

# Reuse event loop
loop = asyncio.get_event_loop()

# Send startup message
loop.run_until_complete(send_message("🚀 Bot is online and will post every 1 minute."))

# Define scheduled job
def send_rotating_message():
    global message_index
    message = messages[message_index]
    loop.run_until_complete(send_message(message))  # <-- FIXED
    message_index = (message_index + 1) % len(messages)

# ---------------------
# Schedule daily post 
# ---------------------
schedule.every().day.at("16:42").do(send_rotating_message)

print("🤖 Automation agent is running. Waiting for scheduled tasks...")

# Main loop
while True:
    schedule.run_pending()
    time.sleep(60)
