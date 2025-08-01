import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

import os

TELEGRAM_TOKEN = os.getenv("8317619029:AAEQh3kSbcJAGgw2VAa-N7TBxkJwKtYaKV0")
OPENAI_API_KEY = os.getenv("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")

openai.api_key = OPENAI_API_KEY

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje_usuario = update.message.text
    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sos un asistente simpático y útil."},
            {"role": "user", "content": mensaje_usuario}
        ]
    )
    await update.message.reply_text(respuesta.choices[0].message.content)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot corriendo...")
app.run_polling()
