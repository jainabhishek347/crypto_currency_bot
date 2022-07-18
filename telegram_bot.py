import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices


telegram_bot_token = "5592239864:AAHV73shOzgbPF4iPlEoqZKHB2c9aR9mniE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    print('context:', context)
    chat_id = update.effective_chat.id
    message = "Hello User\n\n"

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


# a="^/(?!start$)[a-z0-9]+$"
# def message():
#     return "Sorry this command is not available"
# # options = 'start'

dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()

# dispatcher.add_handler(CommandHandler("help", help))
# updater.start_polling()

# dispatcher.add_handler(CommandHandler(a, message))
# updater.start_polling()
# while True:
#     cmd=""
#     if(cmd="start"):
#         dispatcher.add_handler(CommandHandler("start", start))
#         updater.start_polling()
#     else:
#
