NAPALM 라이브러리를 사용하여 Cisco IOS 스위치에 연결하고, 
'Merge1.cfg' 파일에 정의된 새로운 설정을 현재 구성과 병합하는 과정을 구현합니다. 
병합 후 변경 사항이 있는지 확인하고, 변경 사항이 있으면 이를 커밋(적용)한 다음 연결을 종료합니다. 
필요에 따라 특정 파일 시스템을 대상으로 하는 선택적 인자를 설정하는 방법도 주석으로 언급되어 있습니다.

Cisco IOS 장치에서 ip scp server enable 명령은 SCP(Secure Copy Protocol) 서버를 활성화하는데 사용됩니다.
장치와의 안전한 파일 전송을 위해 SCP를 사용하려는 경우 이 명령이 필요합니다. 
SCP는 데이터 전송을 위해 SSH(Secure Shell)를 사용하여 인증과 암호화를 모두 제공합니다.
NAPALM과 함께 사용하는 방법을 사용하는 경우 Cisco IOS 장치에서 SCP 서버를 활성화해야 합니다.
       
[NAPALM 설정 변경 프로세스]
[설정 파일 준비] 👉 "작업 지시서 작성" : 변경할 장비의 명령어(Syntax)를 텍스트 파일(예: Merge1.cfg)로 미리 작성해 두는 단계입니다.
       ↓
load_merge_candidate() 👉 "가상 적재 (Staging)" : 작성한 파일을 장비로 전송하여 **임시 저장소(Candidate Config)**에 올립니다. (아직 실제 적용 안 됨)
       ↓
compare_config() 👉 "변경 예측 (Diff)" : 현재 설정(Running)과 임시 설정(Candidate)을 비교하여, 무엇이 추가(+)되고 삭제(-)되는지 눈으로 확인합니다.
       ↓
commit_config() 또는 discard_config() 👉 "결재 승인(적용) 또는 반려(취소)" :

commit: 변경 내용을 실제 운영 환경(Running Config)에 반영하고 저장합니다.

discard: 임시 저장소에 올렸던 내용을 싹 지우고 작업을 취소합니다.

💡 강의 멘트 가이드 (Tip)
이 흐름을 설명하실 때, 학생들에게 **"쇼핑몰 장바구니"**에 비유해주시면 이해가 빠릅니다.
설정 파일 준비: 사고 싶은 물건 목록 적기.
load: 장바구니에 물건 담기. (아직 결제 안 함)
compare: 장바구니 목록과 가격 확인하기. (잘못 담은 게 없나?)
commit: 결제 버튼 누르기. (배송 시작 = 설정 적용)
discard: 장바구니 비우기. (구매 취소)

------------------------------------------------------------------------------------------------------------------------------------------
from napalm import get_network_driver 
driver = get_network_driver('ios')                  
switch1 = driver('10.1.1.11', 'ccnp', 'cisco') 
# 필요에 따라 위에 다음을 추가: ​​optional_args={'dest_file_system': 'flash0:'}  # 명령어 실행 결과를 특정 파일 시스템에 저장하기 위한 선택적 인자를 설정할 수 있습니다.

switch1.open()  # 장비에 연결을 시작합니다.

print('Accessing 10.1.1.11')                 # 스위치 접근 시작을 알립니다.

switch1.load_merge_candidate(filename='Merge1.cfg')  # 'Merge1.cfg' 파일에서 새 설정을 불러와 현재 구성과 병합합니다.
# switch1.load_merge_candidate(filename='/home/ubuntu/PythonHome/4.napalm/Merge1.cfg')  실행이 안될경우 절대경로 사용

print(switch1.compare_config())              # 현재 구성과 새로 불러온 구성 사이의 차이점을 확인합니다.
switch1.commit_config()                      # 변경 사항을 커밋(적용)합니다.

switch1.close()                              # 장비와의 연결을 종료합니다.




