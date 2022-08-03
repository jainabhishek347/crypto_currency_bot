from gc import callbacks
from lib2to3.pgen2 import driver
from re import M
from turtle import update
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint 
import tracker
from pprint import pprint

bot = Bot(token='5592239864:AAF1nnu5d-93mieHH0j2iJE4CKh5pv3PduQ')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Start", callback_data="start")
button2 = InlineKeyboardButton(text="Price", callback_data="price")
button3=InlineKeyboardButton(text="Help",callback_data="help")
# button4=InlineKeyboardButton(text="Logo",callback_data="logo")
keyboard_inline = InlineKeyboardMarkup().add(button1,button2,button3)
# key=ReplyKeyboardRemove(text="button1",callback_data="randomvalue_of10")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("/Start", "/Price","/Help")
button = InlineKeyboardButton(text="BTC", callback_data="BTC")
keyboard_inline = InlineKeyboardMarkup().add(button)


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)
@dp.message_handler(commands=['BTC'])
async def random_answer(message: types.Message):
    await message.reply("select a coin ",reply_markup=keyboard_inline)
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hello! telelgram", reply_markup=keyboard1)


@dp.message_handler(commands=['help'])
async def mess(message:types.Message):
    await message.reply("""    Available comands are :\n
    /start -> Welcome message.
    /price -> For Cyptocurency price alert.
    /help -> For user help.""")

@dp.message_handler(commands=['price'])
async def price(message:types.Message):
    data = ""

    crypto_data = tracker.get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        data += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    # context.bot.send_message(chat_id=chat_id, text=message)
    # return price
    await message.reply(data)

# @dp.message_handler(commands=['logo'])
# async def logo(message : types.Message):
#     await message.answer_photo("https://media.istockphoto.com/vectors/big-smile-emoticon-with-thumbs-up-vector-id1124532572?k=20&m=1124532572&s=612x612&w=0&h=IXpPDP4EXROUqjakNqxhq-pxrUURTO1jwy7SQKmP6Rw=")

@dp.callback_query_handler(text=["start", "help"])
async def random_value(call: types.CallbackQuery):
    if call.data == "start":
        await call.message.answer("/start")
    if call.data == "randomvalue_of100":
        await call.message.answer("/help")
    if call.data == "randomvalue_of10":
        await call.message.answer("/price")
    if call.data=="randomvalue_of10":
        await call.message.answer("/logo")
    await call.answer()


# print(tracker.price(update, context))
executor.start_polling(dp)
