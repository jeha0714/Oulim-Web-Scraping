# 데이터를 위한 라이브러리
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# 미리 구현해둔 함수 모음
import Find_Data_from_html 

# 모든 호텔 알바 정보를 들고온다.
new_Hotels_DataFrame = Find_Data_from_html.Find_Main_Datas()