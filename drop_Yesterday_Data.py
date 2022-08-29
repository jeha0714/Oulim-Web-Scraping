import datetime


def drop_Yesterday_Data( saved_DataFrame ):
    
    # '현재 시간'과 '어제 날짜'를 가져온다.
    now_Datetime = datetime.datetime.now()              # 현재 시간
    Yesterday = now_Datetime - datetime.timedelta(1)    # 어제 날짜

    # 만약 지금 시간이 자정근처라면
    # < 분 설정을 0분이 아닌 0~2분으로 해둔 이유는 !!! >
    # 코드가 쉬는 시간 + 스크래핑 하는 시간으로 인해 drop_Yesterday_Data함수가 00분을 넘어서 실행되는 경우가 간혹 발생 할 수 있기 때문
    if now_Datetime.hour == 0 and (
         0 <= now_Datetime.minute and now_Datetime.minute <= 2)  :
        

        # '날짜'column.values들의 type이 str이므로 
        # yesterday 값도 str type으로 변형
        # 월/일은 항상 두자리로 표시 ex) 9.1 x 09.01 o
        yesterday_Month = str( Yesterday.month ).zfill(2)
        yesterday_Day = str( Yesterday.day ).zfill(2)
        yesterday_String = yesterday_Month +'.' + yesterday_Day
        

        # 어제 날짜와 관련된 데이터들의 인덱스를 추출한다.
        drop_Index = saved_DataFrame[ saved_DataFrame['날짜'] == yesterday_String ].index
        
        # 어제 날짜와 관련된 데이터들을 제거한다.
        saved_DataFrame = saved_DataFrame.drop( drop_Index )
    


    # 금일 날짜이후로 구성된 데이터프레임을 반환한다.
    return saved_DataFrame