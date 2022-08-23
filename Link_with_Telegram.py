import telegram


bot_Token = "5627910267:AAEtrKaZHotkofGZaztn1Bo5P0oYb4CtBvs"
room_id = "5763314133"

bot = telegram.Bot( token= bot_Token )

def send_message( texts ) :
    bot.sendMessage(chat_id = room_id, text = texts )