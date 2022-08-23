# 데이터를 위한 라이브러리
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time


# 미리 구현해둔 함수 모음
import Find_Data_from_html # 알바정보 찾아오기
import Compare_2_dataframe # 두 개의 데이터프레임 전체 비교
import Link_with_Telegram # 텔레그램 정보



# 첫 데이터 선언
saved_Hotels_DataFrame = pd.DataFrame()
Different_DataFrame = pd.DataFrame()
new_Hotels_DataFrame = pd.DataFrame()


''' < 이 아래로 매 1분마다 실행 > '''
while(True) : 
    new_Hotels_DataFrame = Find_Data_from_html.Find_Main_Datas()

    Different_DataFrame =  Compare_2_dataframe.Compare_DataFrame( 
                            new_Hotels_DataFrame, saved_Hotels_DataFrame)

    # 만약 Different_DataFrame 내에 정보가 하나라도 존재한다면
    if ( len( Different_DataFrame ) > 0 )  :
        
        # 기존 저장되있던 데이터프레임을 새롭게 들고온 데이터프레임으로 바꿔준다.
        saved_Hotels_DataFrame = new_Hotels_DataFrame

        # Diffrent_DataFrame을 날짜와 근무지로 그룹화 시켜준다.
        # Diff_Data_Group = Different_DataFrame.groupby( ['날짜', '근무지'] ).groups 
        

        # 목표인 '롯데호텔월드[잠실].'이 Different_DataFrame에 있는지 확인
        # 확인 후 하나라도 값이 있다면 해당 근무지에 대한 정보가
        # 추가로 등록되었음을 kakaotalk으로 알림.
        if ( len( Different_DataFrame[ Different_DataFrame['근무지']
                                    == '롯데호텔월드[잠실].']) ) :
            # 텔레그램으로 알려주기!
            # 날짜와 근무지에 대한 정보를 넘겨주고 앱에서 메시지를 보낸다.
            for x in Different_DataFrame[ Different_DataFrame['근무지']
                                    == '롯데호텔월드[잠실].'].values :
                texts = str(x)
                Link_with_Telegram.send_message( texts )
                time.sleep(1)
                
    
    # 잠시 쉬어준 후 다시 반복
    time.sleep(50) # 60이 아닌 50인 이유는 soup을 통해 데이터를 가져오는 일에 시간이 걸리기 때문.
