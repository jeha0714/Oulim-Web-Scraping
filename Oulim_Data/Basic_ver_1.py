import requests
from bs4 import BeautifulSoup


# 사이트 주소
# 마지막 page 뒤 1~10 숫자를 붙여 페이지를 유동적으로 옮겨다닐 것임.
url = 'http://oulim.kr/alba/work_total_list.asp?pageno=1&startpage=' 

# 밑은 user-agent로 웹 스크래핑 시 차단 방지를 위한 유저값
hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

res = requests.get(url, headers = hdr) # 사이트를 불러온다.
res.encoding = None # res.text로 불러올 시 한글 깨짐을 방지
res.raise_for_status() # 오류로 인한 사이트 접속 불가 방지

soup = BeautifulSoup(res.text, 'html.parser')
