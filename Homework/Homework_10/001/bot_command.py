from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from sympy import Symbol, collect
import convert

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! \n'
                                     'Это бот по сложению многочленов. \n' 
                                     'Ты можешь получить справку по команде | /help |.')

async def polynomial_sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text
    items = msg.split()

    rec1 = convert.replace(items[1])
    rec2 = convert.replace(items[2])

    x = Symbol('x')

    res = str(collect(rec1 + '+' + rec2, 'x'))
    res = res.replace('**', '^')
    res = res.replace('*', '')
    res += '=0'
    await update.message.reply_text(f'Сумма многочленов: {res}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(f'Команды бота: \n'
                                     '| polsum | - сложение многочленов.\n\n'
                                     'Для сложения необходимо ввести компанду и два выражения через пробел \n'
                                     'При этом само выражение необходимо писать без пробелов - "/polsum 6x^2+26x+62=0 78x^2+123x+76=0" \n\n'
                                     '| /start | - начальное приветствие. \n'
                                     '| /help | - справка.')