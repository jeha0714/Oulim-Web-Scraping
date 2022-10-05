import telegram
import requests

bot_Token = "5627910267:AAEtrKaZHotkofGZaztn1Bo5P0oYb4CtBvs"
personal_room_id = "5763314133" # 개인방 아이디
public_room_id = "-700921908"   # 공공방 아이디 

# 텔레그램 room_id로 지정된 방에 texts내용을 전달함
def send_message( texts ) :
    
    url = f"https://api.telegram.org/bot{bot_Token}/sendMessage?chat_id={personal_room_id}&text={texts}"
    
    print(requests.get(url).json()) # this sends the message