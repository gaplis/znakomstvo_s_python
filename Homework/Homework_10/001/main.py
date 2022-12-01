# Прикрутить телеграм бота к задаче по сложению многочленов.
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *

app = ApplicationBuilder().token("5889492635:AAEx2aL8Sa_K0JaOOK0N9UMXcKCW59mEqUg").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("polsum", polynomial_sum_command))
app.add_handler(CommandHandler("help", help_command))

print('Бот запущен')

app.run_polling()