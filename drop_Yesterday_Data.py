import datetime


def drop_Yesterday_Data( DataFrame ):
    
    # '현재 시간'과 '어제 날짜'를 가져온다.
    now_Datetime = datetime.datetime.now()              # 현재 시간
    Yesterday = now_Datetime - datetime.timedelta(1)    # 어제 날짜

    # 문자열로 이루어진 어제 날짜 변수를 선언해준다.
    # '날짜'column.values들의 type이 str이므로 yesterday 값도 str type으로 변형
    # 월/일은 항상 두자리로 표시 ex) 9.1 x 09.01 o
    yesterday_Month = str( Yesterday.month ).zfill(2)
    yesterday_Day = str( Yesterday.day ).zfill(2)
    yesterday_String = yesterday_Month +'.' + yesterday_Day


    ''' 인자로 받아온 DataFrame의 첫번째 row의 날짜 값이 어제 날짜일 경우 '''
    
    # DataFrame내에 어제와 관련된 정보가 포함된것으로 간주하고 관련 내용을 제거한다.
    if ( DataFrame.iloc[0]['날짜'] == yesterday_String ) :
        
        # 어제 날짜와 관련된 데이터들의 인덱스를 추출한다.
        drop_Index = DataFrame[ DataFrame['날짜'] == yesterday_String ].index
        
        # 어제 날짜와 관련된 데이터들을 제거한다.
        DataFrame = DataFrame.drop( drop_Index )
    
    return DataFrame