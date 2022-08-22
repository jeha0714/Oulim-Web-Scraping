import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


''' <  필요한 페이지에서 데이터 를 꺼내 DataFrame 형태로 반환 > '''

def Find_Main_Datas() :
    # 밑은 user-agent로 웹 스크래핑 시 차단 방지를 위한 유저값
    hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    #res.encoding = None # res.text로 불러올 시 한글 깨짐을 방지

    # 모든 호텔 정보가 들어갈 데이터 프레임 생성
    Main_Hotels_DataFrame = pd.DataFrame(columns = ['날짜','요일','근무지','모집내용','근무시간','인원','성별','시급/일급'])


    for page in range(1,50) :
        
        # < 사이트 주소, User값 >
        # 중간 변수값 pageno=?의 값의 변경을 통해
        # 알바정보가 올라온 사이트를 유동적으로 옮겨다닐 것임.
        Now_Page = requests.get( 'http://oulim.kr/alba/work_total_list.asp?pageno={}&startpage=1'.format(page), 
                                headers = hdr)
        
        # 해당 페이지에 알바 정보가 없다면( status_code != 200 )
        # 그 즉시 반복문을 중지 시킨다.
        if Now_Page.status_code != 200 :
            print(page)
            break;
        
        # Soup 객체 생성
        Now_Page_Soup = BeautifulSoup(Now_Page.text, 'html.parser')
        
        
        # 알바 정보를 전부 들고온다.
        # html에 title 정보도 없고 for문으로 찾기에는 시간복잡도가 상당할 것으로 예측되어 위치는 직접 찾았다.
        Hotels_Info = Now_Page_Soup.find('body').find_all('table')[14].find_all('font')
        
        
        # Hotels_Info의 형태를 column에 맞게 적절히(column = 8) 변경해준다.
        Np_shape_Hotel = np.array(Hotels_Info).reshape( int(len(Hotels_Info) / 8),8)
        
        
        # 알바정보를 데이터프레임으로 변환
        Hotels_DataFrame = pd.DataFrame( Np_shape_Hotel ,
                                        columns = ['날짜','요일','근무지','모집내용','근무시간','인원','성별','시급/일급']) 
        
        # 메인 데이터프레임에 해당 웹에서 받아온 데이터를 추가
        Main_Hotels_DataFrame = Main_Hotels_DataFrame.append( Hotels_DataFrame,
                                                            ignore_index = True)



    ''' [ url에서 가져온 새 DataFrame을 반환한다. ] '''
    return Main_Hotels_DataFrame
