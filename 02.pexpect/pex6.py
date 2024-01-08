#사용자로부터 사용자 이름과 비밀번호를 받아, 미리 정의된 장비들에 SSH 접속 후, 특정 커맨드를 실행하고 그 결과를 파일에 저장하는 것을 자동화

import getpass  # 비밀번호 입력을 위한 라이브러리 임포트
from pexpect import pxssh  # SSH 접속을 위한 라이브러리 임포트

# 각 장비의 프롬프트와 IP 정보를 딕셔너리로 저장
devices = {'R1': {'prompt': 'R1#', 'ip': '10.1.1.21'},'S1': {'prompt': 'S1#', 'ip': '10.1.1.11'}}

# 실행할 커맨드들을 리스트로 저장
commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')  # 사용자로부터 username 입력 받기
password = getpass.getpass('Password: ')  # 사용자로부터 password 입력 받기 (입력 시에는 화면에 표시되지 않음)

# devices 딕셔너리의 모든 장비에 대해 반복
for device in devices.keys():
    outputFileName = device + '_output'  # 출력 파일 이름 설정
    device_prompt = devices[device]['prompt']  # 각 장비의 프롬프트 정보 가져오기
    sh = pxssh.pxssh()  # pxssh 객체 생성
    sh.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)  # SSH 로그인

    # 출력 파일을 binary write 모드로 열기
    with open(outputFileName, 'wb') as f:
        # 모든 커맨드에 대해 반복
        for command in commands:
            sh.sendline(command)  # 커맨드 전송
            sh.expect(device_prompt)  # 프롬프트 대기
            f.write(sh.before)  # 결과를 파일에 쓰기

    sh.logout()  # SSH 로그아웃
