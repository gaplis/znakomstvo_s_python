# Прикрутить бота к задачам с предыдущего семинара: 
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в него систему логирования
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("complex", complex_command))
app.add_handler(CommandHandler("help", help_command))

print('Бот запущен')

app.run_polling()