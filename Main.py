# 데이터를 위한 라이브러리
import pandas as pd
import time


# 미리 구현해둔 함수 모음
import Find_Data_from_html # 알바정보 찾아오기
import Compare_2_dataframe # 두 개의 데이터프레임 전체 비교
import Link_with_Telegram # 텔레그램 정보
import drop_Yesterday_Data # 자정기준 다음날로 넘어갔을 때 전날 데이터 삭제


# 첫 데이터 선언
saved_Hotels_DataFrame = pd.DataFrame()
Different_DataFrame = pd.DataFrame()
new_Hotels_DataFrame = pd.DataFrame()


''' < 이 아래로 반복 실행 > '''
while(True) : 


    # 어제 데이터들은 제거해준다.
    # 최초 시작 saved_Hotels_DataFrame 데이터가 없는 경우는 넘어간다.
    if saved_Hotels_DataFrame.value_counts != 0 :
        saved_Hotels_DataFrame = drop_Yesterday_Data.drop_Yesterday_Data( saved_Hotels_DataFrame )

    # 웹사이트에서 새 데이터들을 가져온다.
    new_Hotels_DataFrame = Find_Data_from_html.Find_Main_Datas()

    # 기존에 저장된 데이터와 새롭게 가져온 데이터를 비교한다.
    Different_DataFrame =  Compare_2_dataframe.Compare_DataFrame( 
                            new_Hotels_DataFrame, saved_Hotels_DataFrame)

    ''' 찾고싶은 호텔알바의 조건 '''
    # < 현재 조건 >은 근무지에 롯데 & 잠실이라는 단어가 포함되어 있는지
    # 모집내용이 뷔페가 포함되거나 연회가 포함되어 있는지
    hotel_Option = ( Different_DataFrame['근무지'].str.contains('롯데') & 
                 Different_DataFrame['근무지'].str.contains('잠실') )
    buffet_Option = (  Different_DataFrame['모집내용'].str.contains('뷔페') )
    banquet_Option = ( Different_DataFrame['모집내용'].str.contains('연회') ) 

    # 호텔알바 조건을 포함한 데이터 프레임을 정의
    Target_Alba_DataFrame = Different_DataFrame[ hotel_Option & ( 
                                    buffet_Option | banquet_Option) ]


    ''' 만약 Target_Alba_DataFrame 내에 정보가 하나라도 존재한다면 '''
    if ( len( Target_Alba_DataFrame ) > 0 )  :
        
        # 기존 저장되있던 데이터프레임을 새롭게 들고온 데이터프레임으로 바꿔준다.
        saved_Hotels_DataFrame = new_Hotels_DataFrame

        # 텔레그램으로 알려주기!
        # 날짜와 근무지에 대한 정보를 넘겨주고 앱에서 메시지를 보낸다.
        for x in Target_Alba_DataFrame.values :
            texts = str(x)
            Link_with_Telegram.send_message( texts )
            time.sleep(1)
                
    
    # 잠시 쉬어준 후 다시 반복
    time.sleep(30)
