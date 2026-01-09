#여러 네트워크 장비에 대해 설정 변경 작업을 자동화하는 예입니다. 
#각 장비에 순차적으로 연결하여 'Merge1.cfg'와 'ospf1.cfg' 파일의 구성을 병합하려 시도합니다. 
#변경 사항이 있을 경우 적용하고, 없을 경우 버립니다. 작업이 완료된 후에는 장비와의 연결을 종료합니다.

from napalm import get_network_driver 

devices = ['10.1.1.11', '10.1.1.12', '10.1.1.13']  # 장비 IP 주소 리스트

for IP in devices:  # devices 리스트의 각 IP 주소에 대해 반복 실행
    print(f"Connecting to {IP}")  # 현재 연결 중인 장비 IP 주소 출력
    driver = get_network_driver('ios')  # Cisco IOS 장비를 위한 드라이버 가져오기
    device = driver(IP, 'ccnp', 'cisco')  # 인증 정보와 함께 장비에 대한 연결 객체 생성
    device.open()  # 장비와의 연결 시작
    device.load_merge_candidate(filename='Merge1.cfg')  # 'Merge1.cfg' 파일에서 설정 병합 준비
    diffs = device.compare_config()  # 현재 구성과 병합 후 구성 비교
    if len(diffs) > 0:  # 차이점이 있으면
        print(diffs)  # 차이점 출력
        device.commit_config()  # 변경 사항 커밋(적용)
    else:  # 차이점이 없으면
        print('No change : ACL, loopback')  # 변경 사항 없음 메시지 출력
        device.discard_config()  # 변경 사항 버림

    device.load_merge_candidate(filename='ospf1.cfg')  # 'ospf1.cfg' 파일에서 OSPF 설정 병합 준비

    diffs = device.compare_config()  # 현재 구성과 OSPF 설정 병합 후 구성 비교
    if len(diffs) > 0:  # 차이점이 있으면
        print(diffs)  # 차이점 출력
        device.commit_config()  # 변경 사항 커밋(적용)
    else:  # 차이점이 없으면
        print('No change : OSPF')  # OSPF 변경 사항 없음 메시지 출력
        device.discard_config()  # 변경 사항 버림

    device.close()  
