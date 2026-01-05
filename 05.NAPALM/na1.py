#napalm 라이브러리를 사용하여 특정 네트워크 장치(‘ios’)에 연결하고, 
#해당 장치로부터 정보를 가져와 출력하는 과정을 수행

import napalm                              # NAPALM 라이브러리 전체를 임포트 (모듈 구조 확인용)

# 1. 드라이버 객체 생성
# 'ios'는 Cisco 라우터/스위치용이며, 'junos', 'eos', 'nxos' 등으로 변경 가능
driver = napalm.get_network_driver('ios')

# 2. 장비 연결 정보 정의 (객체 생성 단계)
# hostname: IP주소 또는 도메인, username/password: 장비 접속 계정
device = driver(hostname='10.1.1.21', username='ccnp', password='cisco')

# 3. 세션 연결 (SSH 접속)
# 실제 네트워크 패킷이 전송되고 로그인이 이루어지는 시점
device.open()

# 4. 데이터 수집 (Facts)
# 모델명, 시리얼 번호, OS 버전, 가동 시간(Uptime) 등 핵심 정보를 딕셔너리로 반환
output = device.get_facts()

# 5. 결과 출력 (Raw Data)
# JSON 포맷팅 없이 출력하면 한 줄로 길게 늘어짐 -> 가독성 비교 교육용
print(output)

# 6. 세션 종료
# 세션을 닫지 않으면 장비의 VTY 라인이 고갈되어 추후 접속 장애 유발 가능
device.close()

----------------------------------------------------------------

보다 최적화 코드
import napalm  # napalm 라이브러리 가져오기

def get_device_facts():
    # 드라이버 설정 : 접속하는 장비의 유형('ios', 'nxos', 'junos' 등)
    driver = napalm.get_network_driver('ios')  # 'ios' 드라이버 가져오기
    
    # 장비에 연결
    device = driver(hostname='10.1.1.21', username='ccnp', password='cisco')  # 장치 연결 정보 설정
    
    try:
        device.open()  # 장치에 연결 시작
        # get_facts() 메서드 : 장비 정보 가져오기(장비 모델, 시리얼 번호, 운영 체제 버전 등)
        output = device.get_facts()  # 장치로부터 사실 가져오기
        print(output)  # 화면에 출력
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        device.close()  # 장치 연결 닫기

if __name__ == "__main__":
    get_device_facts()

1. 예외 처리 (try-except-finally)
장비에 연결할 때와 정보를 가져올 때 발생할 수 있는 예외를 처리하여 프로그램이 중단되지 않도록 합니다.
finally 블록을 사용하여 장비와의 연결을 항상 종료하도록 합니다.

2. 함수로 분리
장비에서 정보를 가져오는 코드를 함수로 분리하여 코드의 재사용성과 가독성을 높였습니다.

3. 메인 가드 (if __name__ == "__main__":)
스크립트를 직접 실행할 때만 get_device_facts 함수를 호출하도록 합니다. 이는 모듈로 임포트될 때 코드가 실행되지 않도록 합니다.
