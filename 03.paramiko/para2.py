#para1.py와 기능이 같음
#'router' 딕셔너리를 사용하여 원격 서버의 정보를 관리하는 방식
#'router' 딕셔너리를 만들고 이를 'ssh_client.connect()' 메소드에 전달할 때 '**' 연산자를 사용
#딕셔너리의 키-값 쌍을 인자로 전달

import paramiko,time #paramiko와 time 모듈 임포트

ssh_client = paramiko.SSHClient() #SSH 클라이언트 객체를 생성
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #호스트 키 자동 추

#ssh_client.connect('10.1.1.21', username='ccnp', password='cisco', look_for_keys=False, allow_agent=False) 

# *, **를 이용한 호출
router={'hostname':'10.1.1.21','port':'22','username':'ccnp','password':'cisco'} # 라우터 정보 저장
print(f'Connecting to {router["hostname"]}') # 연결 시작 메시지 출력
ssh_client.connect(**router,look_for_keys=False,allow_agent=False) # 라우터 정보로 SSH 연결 시작

new_connection = ssh_client.invoke_shell() # 쉘 세션 시작
output = new_connection.recv(5000) # 서버로부터 데이터 수신
print(output.decode()) # 수신한 데이터 디코드 후 출력
new_connection.send('terminal length 0\nshow run\n') # 서버에 명령 전송
time.sleep(3) # 코드 실행 일시 중지
output = new_connection.recv(5000) # 서버로부터 데이터 다시 수신
print(output.decode()) # 수신한 데이터 디코드 후 출력

print('Closing connection') #연결 종료 메시지 출력
new_connection.close() # 쉘 세션 종료
