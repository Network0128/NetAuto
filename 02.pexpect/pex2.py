import pexpect  # pexpect 라이브러리 임포트

host = '10.1.1.21'  # 호스트 주소
username = 'ccnp'  # 사용자 이름
password = 'cisco'  # 비밀번호
tn = pexpect.spawn(f'telnet {host}') # telnet 세션 생성
tn.logfile=open('RunningConfig','wb')  # 로그 파일을 'RunningConfig'으로 설정하고 쓰기 모드('w')와 바이너리 모드('b')로 열기

tn.expect('Username:')  # 사용자 이름 프롬프트 기다림
tn.sendline(username)  # 사용자 이름 전송
tn.expect('Password:')  # 비밀번호 프롬프트 기다림
tn.sendline(password)  # 비밀번호 전송
tn.expect('R1#')  # 커맨드 프롬프트 기다림
tn.sendline('terminal length 0')  # 터미널 길이 설정 커맨드 전송
tn.expect('R1#')  # 커맨드 프롬프트 기다림

cmd_list=['conf t','do show run','end']  # 실행할 커맨드 리스트

for cmd in cmd_list:  # 커맨드 리스트 순회
    tn.sendline(cmd)  # 각 커맨드 전송

tn.expect('R1#')  # 커맨드 프롬프트 기다림
print(tn.before.decode('ascii'))  # 출력 결과 디코딩 후

tn.sendline('exit')  # 종료 커맨드 전송
tn.close()  # 세션 종료
