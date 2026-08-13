import os
from dotenv import load_dotenv
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    if not GEMINI_API_KEY:
        await update.message.reply_text("ERROR: No se encontró la GEMINI_API_KEY en el .env")
        return

    try:
      
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_text,
        )
        bot_reply = response.text

    except Exception as e:
        print(f"Error de Python/Gemini: {e}")
        bot_reply = f"Error al procesar la respuesta: {e}"

    await update.message.reply_text(bot_reply)

if __name__ == '__main__':
    print("Iniciando bot...")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), responder))
    app.run_polling()