import pandas as pd


''' < 기존에 저장중이던 DataFrame과 url을 통해 새롭게 가져온 DataFrame의
        비교를 통해 다른 데이터들을 반환 > '''

def Compare_DataFrame( new_df, saved_df ) :

    # 우선 new_df와 saved_df 두 DataFrame을 하나로 합쳐준다.
    Combine_df = pd.DataFrame()
    Combine_df = pd.concat( [ new_df, saved_df ] )

    # 인덱스를 초기화 해준다. 
    Combine_df = Combine_df.reset_index( drop=True )


    # 결합한 DataFrame의 column을 모두 가져온다.
    df_column = Combine_df.columns.tolist()

    # Combine_df 를 df_column로 group화 시켜준다.
    df_group = Combine_df.groupby( df_column )


    # group화 시켜준 내용을 딕셔너리 형태로 전환시킨다.
    ### columns에 해당하는 정보가 들어있는 key 값과
    ### key값에 해당하는 DataFrame의 index 정보가 value에 저장된다.
    df_Dictionary = df_group.groups

    
    # new_df와 saved_df에서 다른 row 부분을 찾아낸다.
    ### 위 df_Dictionary에서 value >= 2 인 부분은 new_df와 saved_df에
    ### 모두 존재한다는 의미이므로 value = 1인 부분만이 new_df와 saved_df의 차이점이라고 할 수 있다.
    differnt_Indexs = [ x[0] for x in df_Dictionary.values() if len(x) == 1 ]

    
    ''' [ new_df와 saved_df의 다른 행 값만 반환해준다! ] '''
    return Combine_df.reindex( differnt_Indexs )


