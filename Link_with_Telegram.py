import telegram


bot_Token = "5627910267:AAEtrKaZHotkofGZaztn1Bo5P0oYb4CtBvs"
room_id = "5763314133"
#room_id = "-700921908"

bot = telegram.Bot( token= bot_Token )

# 텔레그램 room_id로 지정된 방에 texts내용을 전달함
def send_message( texts ) :
    bot.sendMessage(chat_id = room_id, text = texts )