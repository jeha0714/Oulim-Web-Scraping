import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


''' <  알바 페이지에서 필요한 데이터를 꺼내 DataFrame 형태로 반환 > '''

def Find_Main_Datas() :
    
    # 밑은 user-agent로 웹 스크래핑 시 차단 방지를 위한 유저값
    user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    #res.encoding = None # res.text로 불러올 시 한글 깨짐을 방지

    # < 사이트 주소, user_agent값 >
    Now_Page = requests.get( 'http://oulim.kr/main.asp', headers = user_agent )


    # Soup 객체 생성
    Now_Page_Soup = BeautifulSoup(Now_Page.text, 'html.parser')
    # 알바와 관련된 정보를 전부 들고온다.
    Hotels_Info = Now_Page_Soup.find('div', id = 'divAlba' ).find_all('table')[4].find_all('td', align = {"center", "left", "right"} )


    # 알바정보가 담길 list 생성
    Alba_List = []
    # 가져온 알바 정보를 list내부로 옮긴다.
    for data in Hotels_Info :
        Alba_List.append( data.text.strip() ) # strip을 사용하여 공백 제거

        
    # Alba_List의 형태가 'column'이 10개이도록 형태를 변환해준다.
    Np_shpae_Hotel_Alba = np.array(Alba_List).reshape( int( len(Alba_List) / 10 ), 10 )

    # numpy 배열 형태를 DataFrame형태로 변환해준다.
    Hotels_DataFrame = pd.DataFrame( Np_shpae_Hotel_Alba )


    # 가져온 데이터 중 첫번째 행을 column으로 설정
    Hotels_DataFrame = Hotels_DataFrame.rename( columns=  Hotels_DataFrame.iloc[0] )
    # 필요없는 정보인 column='상태' 열을 제거
    Hotels_DataFrame = Hotels_DataFrame.drop(['상태'], axis = 1 )
    # column으로 정해준 첫번째 행 데이터 제거
    Hotels_DataFrame = Hotels_DataFrame.drop( Hotels_DataFrame.index[0])



    ''' [ url에서 가져온 새 DataFrame을 반환한다. ] '''
    return Hotels_DataFrame
