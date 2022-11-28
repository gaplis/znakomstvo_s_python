from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

async def find_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum абв авбам пвапва
    res = []
    for i in range(1, len(items)):
            if not ('а' in items[i] and 'б' in items[i] and 'в' in items[i]):
                res.append(items[i])

    string = ' '.join(res)

    await update.message.reply_text(f'{string}')
    await update.message.reply_text(f'Ачуметь!')