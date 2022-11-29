from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logged

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logged.log(update, context)

    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! \n'
                                     'Это бот-калкулятор. \n' 
                                     'Ты можешь получить справку по команде | /help |.')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logged.log(update, context)

    msg = update.message.text
    items = msg.split()

    if '.' in items[1]:
        x = float(items[1])
    else:
        x = int(items[1])

    if '.' in items[3]:
        y = float(items[3])
    else:
        y = int(items[3])
    
    if items[2] == '+':
        await update.message.reply_text(f'Результат: {x} + {y} = {x + y}')
    elif items[2] == '-':
        await update.message.reply_text(f'Результат: {x} - {y} = {x - y}')
    elif items[2] == '*':
        await update.message.reply_text(f'Результат: {x} * {y} = {x * y}')
    elif items[2] == '/':
        await update.message.reply_text(f'Результат: {x} / {y} = {x / y}')
    elif items[2] == '**':
        await update.message.reply_text(f'Результат: {x} в степени {y} равно {x ** y}.')

async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logged.log(update, context)

    msg = update.message.text
    items = msg.split()

    if '.' in items[1]:
        x1 = float(items[1])
    else:
        x1 = int(items[1])

    if '.' in items[2]:
        x2 = float(items[2])
    else:
        x2 = int(items[2])

    if '.' in items[4]:
        y1 = float(items[4])
    else:
        y1 = int(items[4])

    if '.' in items[5]:
        y2 = float(items[5])
    else:
        y2 = int(items[5])

    x = complex(x1, x2)
    y = complex(y1, y2)    
    
    if items[3] == '+':
        await update.message.reply_text(f'Результат: {x} + {y} = {x + y}')
    elif items[3] == '-':
        await update.message.reply_text(f'Результат: {x} - {y} = {x - y}')
    elif items[3] == '*':
        await update.message.reply_text(f'Результат: {x} * {y} = {x * y}')
    elif items[3] == '/':
        await update.message.reply_text(f'Результат: {x} / {y} = {x / y}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logged.log(update, context)
    
    await update.message.reply_text(f'Команды бота: \n'
                                     '| /calc | - калькулятор. \n\n' 
                                     'Для выполнения необходимо ввести компанду и два числа, между которыми будет знак действия. \n'
                                     'Вводить необходимо одим сообщением через пробел - "/calc 1 + 2"). \n'
                                     'Вещественные числа необходимо вводить через точку. \n\n'
                                     'Операции: \n'
                                     '"+" - сложение.\n'
                                     '"-" - вычитание.\n'
                                     '"*" - умножение.\n'
                                     '"/" - деление.\n'
                                     '"**" - возведение в степень.\n\n'
                                     '| /complex | - калькулятор комплексных чисел. \n\n'
                                     'Для выполнения необходимо ввести компанду и четыре числа, между двумя которыми будет знак действия. \n'
                                     'Вводить необходимо одим сообщением через пробел - "/complex 1 2 + 3 4"). \n'
                                     'Вещественные числа необходимо вводить через точку. \n\n'
                                     'Операции: \n'
                                     '"+" - сложение.\n'
                                     '"-" - вычитание.\n'
                                     '"*" - умножение.\n'
                                     '"/" - деление.\n\n'
                                     '| /start | - начальное приветствие. \n'
                                     '| /help | - справка.')