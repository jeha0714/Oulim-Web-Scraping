import datetime
import pytz


def drop_Today_Data( DataFrame ):

    # '금일 시간' 관련 정보를 가져온다.
    Today = datetime.datetime.now( pytz.timezone('Asia/Seoul') )    # 금일 시간

    # 문자열로 이루어진 금일 날짜 변수를 선언해준다.
    # '날짜'column.values들의 type이 str이므로 today 값도 str type으로 변형
    # 월/일은 항상 두자리로 표시 ex) 9.1 x 09.01 o
    Today_Month = str( Today.month ).zfill(2)
    Today_Day = str( Today.day ).zfill(2)
    Today_String = Today_Month + '.' + Today_Day


    ### 인자로 받아온 DataFrame내부 '날짜'column에 금일 날짜 값이 존재하는 경우

    # DataFrame내에 금일과 관련된 정보가 포함된것으로 간주하고 관련 내용을 제거한다.
    if ( ( DataFrame['날짜'] == Today_String ).any() ) :

        # 금일 날짜와 관련된 데이터들의 인덱스를 추출한다.
        drop_Index = DataFrame[ DataFrame['날짜'] == Today_String ].index

        # 금일 날짜와 관련된 데이터들을 제거한다.
        DataFrame = DataFrame.drop( drop_Index )

    return DataFrame