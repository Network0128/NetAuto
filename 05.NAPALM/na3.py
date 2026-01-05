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
