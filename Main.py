# 데이터를 위한 라이브러리
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# 미리 구현해둔 함수 모음
import Find_Data_from_html # 알바정보 찾아오기
import Compare_2_dataframe # 두 개의 데이터프레임 전체 비교


# 1분간격으로 모든 호텔 알바 정보를 들고온다.
import threading
import time


# 첫 데이터 선언
saved_Hotels_DataFrame = pd.DataFrame()
Different_DataFrame = pd.DataFrame()


''' < 이 아래로 매 1분마다 실행 > '''
new_Hotels_DataFrame = Find_Data_from_html.Find_Main_Datas()

Different_DataFrame =  Compare_2_dataframe.Compare_DataFrame( 
                        new_Hotels_DataFrame, saved_Hotels_DataFrame)

# 만약 Different_DataFrame 내에 정보가 하나라도 존재한다면
if ( len( Different_DataFrame ) > 0 )  :
    
    # 기존 저장되있던 데이터프레임을 새롭게 들고온 데이터프레임으로 바꿔준다.
    saved_Hotels_DataFrame = new_Hotels_DataFrame

    # 목표인 '롯데호텔월드[잠실].'이 Different_DataFrame에 있는지 확인
    # 확인 후 하나라도 값이 있다면 해당 근무지에 대한 정보가
    # 추가로 등록되었음을 kakaotalk으로 알림.
    if ( len( Different_DataFrame[ Different_DataFrame['근무지']
                                == '롯데호텔월드[잠실].']) ) :
        # 카톡으로 알려주기!
        a = 1
        


