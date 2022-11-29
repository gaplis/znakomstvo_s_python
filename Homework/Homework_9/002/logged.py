from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('log.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.now()}\n')
    file.close()