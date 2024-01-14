#Python을 이용해 SSH 접속을 통해 원격 라우터의(호스트)의 설정파일을 출력하고 연결을 종료하는 코드

import paramiko,time #paramiko, time 모듈 추가

ssh_client = paramiko.SSHClient()  #SSHClient 클래스의 인스턴스를 생성
print('Connecting to 10.1.1.21') #시작 출력
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #호스트 키가 없는 경우 자동으로 추가하는 정책을 설정
ssh_client.connect('10.1.1.21', username='ccnp', password='cisco', look_for_keys=False, allow_agent=False) #SSH 세션을 열고 원격 호스트에 연결

new_connection = ssh_client.invoke_shell() #새로운 셸 세션 연결
output = new_connection.recv(5000) #셸 세션에서 출력된 데이터를 읽어옴
print(output.decode()) #출력된 데이터를 디코딩하여 출력
new_connection.send('terminal length 0\nshow run\n')
time.sleep(3) #3초 대기, 지연시간을 추가하여 모든 출력을 저장할 수 있도록 기다림
output = new_connection.recv(5000) #셸 세션에서 출력된 데이터를 읽어옴
print(output.decode()) #출력된 데이터를 디코딩하여 출력

print('Closing connection') #종료 출력
new_connection.close() #셸 세션 닫음
