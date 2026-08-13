import os
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot OK")

    def log_message(self, format, *args):
        return

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()



load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


user_sessions = {}
MAX_SESSIONS = 50 


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id  

    if not GEMINI_API_KEY:
        await update.message.reply_text("ERROR: No se encontró la GEMINI_API_KEY")
        return

    try:
       
        if len(user_sessions) > MAX_SESSIONS:
            user_sessions.clear()

        
        if user_id not in user_sessions:
            user_sessions[user_id] = client.chats.create(model='gemini-1.5-flash')

        chat = user_sessions[user_id]

        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

        response = await asyncio.to_thread(chat.send_message, user_text)
        bot_reply = response.text

    except Exception as e:
        print(f"Error de Python/Gemini: {e}")
        bot_reply = f"Error al procesar la respuesta: {e}"

    max_length = 4000
    if len(bot_reply) > max_length:
        for i in range(0, len(bot_reply), max_length):
            await update.message.reply_text(bot_reply[i:i + max_length])
    else:
        await update.message.reply_text(bot_reply)


if __name__ == '__main__':
    print("Iniciando bot con memoria...")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))
    
    app.run_polling(drop_pending_updates=True)