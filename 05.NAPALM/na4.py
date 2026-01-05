import socket                          # 로컬 컴퓨터(스크립트 실행 위치)에서 DNS 조회를 수행하기 위한 라이브러리
import json                            # Ping 결과(Dictionary)를 보기 좋은 포맷으로 변환하기 위한 도구
from napalm import get_network_driver  # NAPALM의 핵심 드라이버 로드

driver = get_network_driver('ios')     # Cisco IOS 장비 제어를 위한 드라이버 선택
switch1 = driver('10.1.1.11', 'ccnp', 'cisco')  # 장비 연결 객체 생성 (IP, ID, PW 설정)
switch1.open()                         # SSH 세션을 열고 장비에 로그인

# 1. 로컬 머신에서 도메인 주소를 IP로 변환
# 설명: 장비가 아닌, 스크립트가 실행되는 컴퓨터(PC/서버)가 DNS에 질의하여 IP를 얻어옵니다.
destination_ip = socket.gethostbyname('google.com')
print(f"Target IP derived from DNS: {destination_ip}")  # (선택사항) 변환된 IP를 확인하기 위한 출력

# 2. 장비에서 Ping 명령 수행
# 설명: 위에서 얻은 IP로 '장비가' Ping을 쏩니다. (source는 장비, destination은 구글)
output = switch1.ping(destination_ip)

# 3. 결과 출력
# 설명: NAPALM의 ping 결과는 성공률, RTT(지연시간) 등을 포함한 딕셔너리 형태로 반환됩니다.
print(json.dumps(output, indent=4))

switch1.close()                        # 작업 완료 후 세션 종료 (필수)

----------------------------------------------------------------------------------

gns 가상 장비의 느린 시간으로 실행이 안될 경우 아래와 같이 수정

우선 스위치에서 banner 제거 설정
SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW1(config)#no banner motd
SW1(config)#no banner login
SW1(config)#no banner exec
SW1(config)#end
SW1#wr

import socket
import json
from napalm import get_network_driver

driver = get_network_driver('ios')

# 1. secret 제거: SSH 접속 시 바로 # 모드인 것이 확인되었으므로 불필요
# 2. global_delay_factor 유지: GNS3가 느리므로 5배 정도 여유를 줌
switch1 = driver(
    '10.1.1.11', 
    'ccnp', 
    'cisco', 
    optional_args={'global_delay_factor': 5}
)

switch1.open()

target_ip = socket.gethostbyname('google.com')
print(f"Pinging {target_ip}...")

# 핵심 해결책: count=2 옵션 추가
# 설명: "5번 다 쏘지 말고 2번만 쏴라. 빨리 끝내자."
output = switch1.ping(target_ip, count=1)

print(json.dumps(output, indent=4))

switch1.close()
