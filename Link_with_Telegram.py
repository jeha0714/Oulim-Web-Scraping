import telegram


bot_Token = "5627910267:AAEtrKaZHotkofGZaztn1Bo5P0oYb4CtBvs"
room_id = "-700921908" # 공유중인 톡방 아이디
#room_id = "5763314133" # 나 자신 방 아이디

bot = telegram.Bot( token= bot_Token )

def send_message( texts ) :
    bot.sendMessage(chat_id = room_id, text = texts )