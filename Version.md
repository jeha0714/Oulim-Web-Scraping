### < 이번 버전에서 구현한 것들 >

[ 2.0.1 version ]
1. url에서 전날 데이터가 불특정 시간대에 삭제되는점을 고려하여 전날 데이터가 새로운 알바정보로 인식하고 메세지로 날라오지 않도록 수정함.


### < 이전 버전에서 구현한 것들 >

[ 1.0 version ] 롯데호텔월드[잠실]' 및 뷔페/연회에 대한 알바정보가 새롭게 올라왔을 때 텔레그램을 통해 메세지로 알려준다.

[ 1.1 version ] 00시 기준으로 saved_data 내 전날 데이터 삭제를 하였다.

[ 1.2 version ] 처음부터 내 목적인 롯데호텔월드[잠실]'의 연회서빙 or 롯데호텔월드[잠실]'의 뷔페서빙 07시조에 대해서만 알람을 주도록 설계

[ 2.0 version ]
 이전 버전( 1.x version )에서 데이터를 가져오는 url에 불필요한 데이터들이
많이 섞여있어 알바 정보를 가져올 수 있는 새로운 url을 찾아내어 해당 url에서 필요한 데이터를 가져올 수 있도록 Find_Data_from_html을 새롭게 정의하였고 이에 맞추어 Main또한 새롭게 구성하였음. 


### < 이번 버전에서 구현 못한 것들 >

1. kakaotalk이 아닌 telegram으로 구현하였다.
( kakaotalk은 다수가 속한 톡방의 bot생성 방법을 찾지 못하였고 카카오톡은 bot으로 인식한 유저의 톡방 초대를 막음. )

2. 새롭게 수집 된 데이터들의 수집 시간을 따로 저장하여 시각화 하기. 

3. 코드가 제대로 실행중인지 체크 ( 코드 혹은 서버에 문제가 생겨 실행이 중단될 경우 텔레그램을 통해 알려주기)


## < 현재 버전에서 발견한 문제점 >

1. url에서 기존에 올렸던 알바 정보 중 인원 수를 변경하여 재등록한 알바가 새롭게 올라온 알바라고 인식되며 saved에 저장된 기존 알바 new에 저장된 인원 수만 변경된 기존 알바 내용이 telegram에 올라온다.