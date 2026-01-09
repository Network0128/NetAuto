# NAPALM 라이브러리를 사용하여 IOS 네트워크 장비(라우터)에 연결하고, 특정 구성 파일을 라우터에 병합하려고 시도합니다. 
# 주의: 라우터는 IOSvRouter를 사용
# 새로 불러온 구성과 현재 구성 사이의 차이점을 확인한 뒤, 차이점이 있으면 변경 사항을 적용(커밋)하고, 차이점이 없으면 변경 사항을 버립니다. 
# 마지막으로 네트워크 장비와의 연결을 종료합니다.

from napalm import get_network_driver  

driver = get_network_driver('ios')  
device = driver('10.1.1.21', 'ccnp', 'cisco') 
device.open()  

print('Accessing 10.1.1.21')  # 라우터 접근 시작을 알립니다.
device.load_merge_candidate(filename='Merge1.cfg') #Load new settings (merge)  # 'Merge1.cfg' 파일에서 새 설정을 불러와 현재 구성과 병합합니다.
# device.load_merge_candidate(filename='/home/ubuntu/PythonHome/4.napalm/Merge1.cfg') 컴파일 실패시, 절대경로 사용

diffs = device.compare_config() # 현재 구성과 새로 불러온 구성 사이의 차이점을 확인합니다.
if len(diffs) > 0:  # 차이점이 있다면,
    print(diffs)  # 차이점을 출력합니다.
    device.commit_config()  # 변경 사항을 커밋합니다.
else:  # 차이점이 없다면,
    print('No change : ACL, loopback')  # 변경 사항이 없음을 알리고,
    device.discard_config()  # 불러온 설정을 버립니다.

device.close()  

