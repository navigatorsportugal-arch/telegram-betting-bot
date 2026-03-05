import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot de apostas ativo!")

async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://pifootball.com/widgets/full/download/"
    r = requests.get(url)

    if r.status_code == 200:
        await update.message.reply_text("⚽ Dados recebidos da API")
    else:
        await update.message.reply_text("Erro ao obter jogos")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jogos", jogos))

app.run_polling()
