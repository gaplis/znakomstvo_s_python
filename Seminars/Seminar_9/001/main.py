from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("find", find_command))

print('server start')
app.run_polling()