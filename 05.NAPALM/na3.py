# NAPALM 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고,
# 해당 장치의 정보를 가져와 JSON 형식으로 출력하는 과정을 수행

from napalm import get_network_driver  # napalm 라이브러리에서 get_network_driver 함수 가져오기
import json  # json 라이브러리 가져오기
driver = get_network_driver('ios')  # 'ios' 드라이버 가져오기
SW1 = driver('10.1.1.11', 'ccnp', 'cisco')  # 장치 연결 정보 설정
SW1.open()  # 장치에 연결 시작
output = SW1.get_facts()  # 장치로부터 사실 가져오기
print(json.dumps(output,indent=4))  # 가져온 사실을 JSON 형식으로 출력 (4칸 들여쓰기 : 코드의 가독성을 높임)
SW1.close()  # 장치 연결 종료

---------------------------------

○ 위의 코드에서 아래 API 메서드들을 추가 해보기
from napalm import get_network_driver  # NAPALM의 핵심 함수 가져오기 (특정 벤더 드라이버를 호출하는 역할)
import json                            # 수집된 데이터(Dictionary)를 보기 좋게 정렬해서 출력하기 위한 라이브러리

driver = get_network_driver('ios')     # Cisco IOS용 드라이버 클래스 선택 ('junos', 'eos' 등으로 변경 가능)
switch1 = driver('10.1.1.11', 'ccnp', 'cisco')  # 장비 연결 객체 생성 (IP, ID, PW 정의 - 실제 연결은 아직 안 됨)
switch1.open()                         # 실제 장비에 SSH 접속 시도 (로그인 수행)

output = switch1.get_facts()           # 장비의 기본 정보 수집 (호스트네임, 모델명, OS 버전, 시리얼 등)
print(json.dumps(output, indent=4))    # 파이썬 딕셔너리를 JSON 포맷으로 변환하여 들여쓰기(4칸) 적용 후 출력
print()                                # 결과 구분을 위한 빈 줄 출력

output = switch1.get_interfaces()      # 모든 인터페이스의 상세 정보 수집 (Up/Down 상태, MAC 주소, 속도 등)
print(json.dumps(output, indent=4))    # 수집 결과 JSON 형식으로 출력
print()                                # 빈 줄 출력

output = switch1.get_interfaces_counters() # 인터페이스별 트래픽 통계 수집 (전송/수신 패킷 수, 에러, 드랍 등)
print(json.dumps(output, indent=4))    # 수집 결과 JSON 형식으로 출력

switch1.close()                        # SSH 세션 종료 (중요: 작업이 끝나면 반드시 연결을 끊어 리소스 반환)
