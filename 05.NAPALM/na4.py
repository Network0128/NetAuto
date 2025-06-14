# NAPALM 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고,
#'google.com’의 IP 주소를 가져와 해당 주소로 핑을 보낸 후, 그 결과를 JSON 형식으로 출력하는 과정을 수행

import socket  # 소켓 라이브러리 가져오기,네트워크 연결에 사용
import json  # json 라이브러리 가져오기, 데이터 포맷팅에 사용
from napalm import get_network_driver  # napalm 라이브러리에서 get_network_driver 함수 가져오기, 네트워크 장비 관리에 사용

driver = get_network_driver('ios')  # IOS 장비를 위한 네트워크 드라이버를 가져옵니다.
SW1 = driver('10.1.1.11', 'ccnp', 'cisco')  # 드라이버를 사용하여 스위치에 연결하기 위한 객체를 생성합니다.
SW1.open()  # 네트워크 장비에 연결을 시작합니다.

destination_ip = socket.gethostbyname('google.com')  # 'google.com'의 IP 주소를 조회합니다.
output = SW1.ping(destination_ip) # 조회한 IP 주소로 핑(ping)을 보냅니다.

print(json.dumps(output,indent=4))  # 핑 결과를 JSON 형식으로 출력합니다. 들여쓰기는 4칸입니다.
SW1.close()  # 네트워크 장비 연결을 종료합니다.
