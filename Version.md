### < 이번 버전에서 구현한 것들 >

[ 2.2 version ]
 2.0.1 version 에서 구현한 drop_Yesterday_Data에 알고리즘 구현에 문제가 발생. ( 00시 기준 전날 데이터가 아닌 당일 데이터를 삭제해야함 ) 
 이에 맞추어 적절하게 코드를 수정함과 동시에 함수 이름을 'drop_Yesterday_Data' 에서 'drop_Today_Data' 로 변경 


### < 이전 버전에서 구현한 것들 >

[ 1.0 version ] 롯데호텔월드[잠실]' 및 뷔페/연회에 대한 알바정보가 새롭게 올라왔을 때 텔레그램을 통해 메세지로 알려준다.

[ 1.1 version ] 00시 기준으로 saved_data 내 전날 데이터 삭제를 하였다.

[ 1.2 version ] 처음부터 내 목적인 롯데호텔월드[잠실]'의 연회서빙 or 롯데호텔월드[잠실]'의 뷔페서빙 07시조에 대해서만 알람을 주도록 설계

[ 2.0 version ]
 이전 버전( 1.x version )에서 데이터를 가져오는 url에 불필요한 데이터들이
많이 섞여있어 알바 정보를 가져올 수 있는 새로운 url을 찾아내어 해당 url에서 필요한 데이터를 가져올 수 있도록 Find_Data_from_html을 새롭게 정의하였고 이에 맞추어 Main또한 새롭게 구성하였음. 

[ 2.0.1 version ]
 1.1 version에서 구현된 drop_Yesterday_Data를 url에서 전날 데이터가 불특정 시간대에 삭제되는점을 고려하여 전날 데이터가 새로운 알바정보로 인식하고 메세지로 날라오지 않도록 수정함.

[ 2.1 version ]
 2.0 이전 버전에서 구현한 Link_with_Telegram.py에서 aysncio관련 error가 발생하여 Link_with_Telegram.py 내부 코드 전체를 변경함.

