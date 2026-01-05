# NAPALM 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고, 
# 해당 장치의 모든 인터페이스 정보 출력

from napalm import get_network_driver      # 드라이버 함수만 명시적으로 가져오기 (메모리 효율 및 코드 간결성)
import json                                # 데이터를 보기 좋게 정렬(Pretty Print)하기 위한 라이브러리

# 1. 드라이버 로드
driver = get_network_driver('ios')         # Cisco IOS용 드라이버 선택

# 2. 장비 연결 객체 생성
device = driver(hostname='10.1.1.21', username='ccnp', password='cisco')

# 3. 세션 연결
device.open()                              # SSH 로그인 수행

# 4. 인터페이스 정보 수집
# 모든 인터페이스의 상태(Up/Down), MAC 주소, 속도, MTU 등을 수집
interfaces = device.get_interfaces()       # 원본 코드의 변수명 오류 수정 (interface -> interfaces)

# 5. 결과 출력 (JSON Formatting)
# indent=4 옵션을 주어 계층 구조를 시각적으로 명확하게 표현
print(json.dumps(interfaces, indent=4))

# 6. 세션 종료
device.close()                             # 작업 완료 후 연결 해제

---------------------------------------------------
# 인터페이스 정보 출력부분만 아래와 같이 수정

for interface_name in interface:                      # 이 부분은 딕셔너리의 key만 반복해서 꺼내오는 구조다
    print(interface_name, interface[interface_name])  # 각 인터페이스의 이름과 상세 정보 출력

# interface : 모든 인터페이스 정보를 담은 dictionary
# interface_name: GigabitEthernet0/0, Loopback0 등 모든 인터페이스의 이름
# interfaces[interface_name]: 해당 이름에 대한 세부 정보(서브 딕셔너리)

---------------------------------------------------
위의 for문을 다음과 같이 수정하면, 더 읽기 좋게 출력됨
for name, info in interface.items():
    print(f"[{name}]")
    for key, value in info.items():
        print(f"  {key}: {value}")

