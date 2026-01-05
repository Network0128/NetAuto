장비 연결 → 정보 수집(Facts) → 데이터 시각화(JSON) → 종료"**라는 가장 기초적인 자동화 흐름

from napalm import get_network_driver  # 멀티 벤더 지원을 위한 NAPALM 핵심 드라이버 로드
import json                            # 결과 데이터를 사람이 읽기 편하게 가공하는 도구

driver = get_network_driver('ios')     # 타겟 장비의 OS(Cisco IOS)에 맞는 드라이버 클래스 호출
SW1 = driver('10.1.1.11', 'ccnp', 'cisco')  # 장비 접속 객체 생성 (IP, 계정 정보 설정 - 아직 연결 안 됨)
SW1.open()                             # SSH 세션을 열고 실제 장비에 로그인 수행

output = SW1.get_facts()               # 장비의 고유 정보(버전, 시리얼, 호스트명 등)를 딕셔너리로 수집
print(json.dumps(output, indent=4))    # 수집된 딕셔너리를 보기 좋게 JSON 포맷(4칸 들여쓰기)으로 출력

SW1.close()                            # 작업 완료 후 세션 종료 (VTY 라인 점유 해제 및 리소스 반환)

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

------------------------------
○ S1#sh mac address-table 의 결과를 아래 코드로 출력

import json                                     # JSON 변환 및 포맷팅 도구 로드
from napalm import get_network_driver           # NAPALM 드라이버 호출 함수 임포트

driver = get_network_driver('ios')              # Cisco IOS용 드라이버 클래스 선택
switch1 = driver('10.1.1.11', 'ccnp', 'cisco')  # 장비 접속 정보 설정 (객체 생성)
switch1.open()                                  # 장비에 실제 SSH 연결 시도

output = switch1.get_mac_address_table()        # 장비의 MAC 주소 테이블(L2 정보) 전체 수집
print(json.dumps(output, indent=4))             # 결과를 들여쓰기된 JSON 형태로 출력

switch1.close()                                 # 작업 완료 후 세션 연결 종료
