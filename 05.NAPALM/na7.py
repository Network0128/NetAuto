# NAPALM 라이브러리를 사용하여 네트워크 스위치의 구성을 관리하는 예시를 보여줍니다. 
# 먼저, 스위치에 접근하여 'Merge1.cfg'와 'ospf1.cfg' 파일에서 불러온 새로운 설정을 현재 구성과 병합할 준비를 합니다. 
# 변경 사항이 있는 경우 이를 커밋하여 적용하고, 없으면 버립니다. 마지막으로 연결을 종료합니다.

from napalm import get_network_driver  # napalm에서 get_network_driver 함수를 임포트합니다. 네트워크 장비를 관리하기 위해 사용됩니다.
driver = get_network_driver('ios')  # Cisco IOS 장비를 위한 네트워크 드라이버를 가져옵니다.
switch2 = driver('10.1.1.12', 'ccnp', 'cisco')  # 드라이버를 사용하여 IP 주소가 10.1.1.12인 스위치에 대한 연결 객체를 생성합니다.
switch2.open()  # 스위치와의 연결을 시작합니다.

print('Accessing 10.1.1.12')  # 10.1.1.12 주소를 가진 스위치에 접근 중임을 알립니다.
switch2.load_merge_candidate(filename='Merge1.cfg')  # 'Merge1.cfg' 파일에서 새 설정을 불러와 현재 구성과 병합할 준비를 합니다.

diffs = switch2.compare_config()  # 현재 구성과 새로 불러온 구성 사이의 차이점을 비교합니다.
if len(diffs) > 0:  # 차이점이 있다면,
    print(diffs)  # 차이점을 출력합니다.
    switch2.commit_config()  # 변경 사항을 커밋하여 실제로 적용합니다.
else:  # 차이점이 없다면,
    print('No change : ACL, loopback')  # ACL이나 루프백 설정에 변화가 없음을 알리고,
    switch2.discard_config()  # 준비된 변경 사항을 버립니다.

switch2.load_merge_candidate(filename='ospf1.cfg')  # 'ospf1.cfg' 파일에서 새 OSPF 설정을 불러와 현재 구성과 병합할 준비를 합니다.

diffs = switch2.compare_config()  # 현재 구성과 새로 불러온 OSPF 구성 사이의 차이점을 다시 비교합니다.
if len(diffs) > 0:  # OSPF 설정에 차이점이 있다면,
    print(diffs)  # 차이점을 출력합니다.
    switch2.commit_config()  # OSPF 설정 변경 사항을 커밋하여 실제로 적용합니다.
else:  # OSPF 설정에 차이점이 없다면,
    print('No change : OSPF')  # OSPF 설정에 변화가 없음을 알리고,
    switch2.discard_config()  # 준비된 변경 사항을 버립니다.

switch2.close()  # 스위치와의 연결을 종료합니다.

