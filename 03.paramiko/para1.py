import paramiko

ssh = paramiko.SSHClient() # SSH 클라이언트 객체 생성

# 호스트 키 자동 추가 비활성화, 호스트 키 검증을 자동으로 수행하도록 설정
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #호스트 키를 직접 수동으로 추가하지 않아도 됩니다.

ssh.connect('10.1.1.21', username='ccnp', password='cisco') # SSH 연결 설정

# 명령(sh ip int br) 실행, 결과를 각 스트림(stdin, stdout, stderr)에 저장
stdin, stdout, stderr = ssh.exec_command('sh ip int br')

# 실행 결과를 읽어서 저장
output = stdout.read()

# SSH 연결 종료
ssh.close()

# 실행 결과를 출력
print(output.decode())

