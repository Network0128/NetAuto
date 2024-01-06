#Python의 pexpect 모듈을 사용해 여러 장비에 Telnet 접속을 하고, 각 장비에서 명령어를 실행한 후 결과를 로그 파일에 저장하는 작업 자동화
import pexpect  # pexpect 모듈 임포트

# 연결할 장비의 IP 주소
host = ['10.1.1.21','10.1.1.11']

# 연결할 장비와 해당 장비의 프롬프트, IP 주소
devices={'R1':{'prompt':'R1#','ip':host[0]},
         'S1':{'prompt':'S1#','ip':host[1]}
}

username = 'ccnp'  # Telnet 접속 사용자 이름
password = 'cisco'  # Telnet 접속 비밀번호

# devices 딕셔너리의 키를 반복하는 for 문
for device in devices.keys():
    device_info = devices[device]  # 현재 장비의 정보
    device_prompt = device_info['prompt']  # 현재 장비의 프롬프트
    logfile_path = f'Runnig_Config_{device_info["ip"]}'  # 로그 파일 경로 설정

    tn = pexpect.spawn(f'telnet {device_info["ip"]}')  # Telnet 세션 생성
    tn.logfile = open(logfile_path, 'wb')  # 로그 파일 열기

    tn.expect('Username:')  # 'Username:' 프롬프트 기다림
    tn.sendline(username)  # 사용자 이름 전송
    tn.expect('Password:')  # 'Password:' 프롬프트 기다림
    tn.sendline(password)  # 비밀번호 전송
    tn.expect(device_prompt)  # 장비의 프롬프트 기다림

    tn.sendline('terminal length 0')  # 터미널 길이 설정
    tn.expect(device_prompt)  # 장비의 프롬프트 기다림

    list_a = ['conf t','do sh run','end']  # 실행할 커맨드 리스트

    for cmd in list_a:  # 커맨드 리스트 반복
        tn.sendline(cmd)  # 각 커맨드 전송

    tn.expect(device_prompt)  # 장비의 프롬프트 기다림
    print(tn.before.decode('ascii'))  # Telnet 세션에서 받은 출력 디코딩 후 출력

    tn.sendline('exit')  # 종료 커맨드 전송

tn.close()  # Telnet 세션 종료
