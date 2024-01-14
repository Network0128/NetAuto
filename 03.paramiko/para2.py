#para1.py와 기능이 같음
#'router' 딕셔너리를 사용하여 원격 서버의 정보를 관리하는 방식
#'router' 딕셔너리를 만들고 이를 'ssh_client.connect()' 메소드에 전달할 때 '**' 연산자를 사용하여 딕셔너리의 키-값 쌍을 인자로 전달하는 것이 특징

import paramiko,time 

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#ssh_client.connect('10.1.1.21', username='ccnp', password='cisco', look_for_keys=False, allow_agent=False) 

# *, **를 이용한 호출
router={'hostname':'10.1.1.21','port':'22','username':'ccnp','password':'cisco'}
print(f'Connecting to {router["hostname"]}') #시작 출력
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)

new_connection = ssh_client.invoke_shell() 
output = new_connection.recv(5000) 
print(output.decode()) 
new_connection.send('terminal length 0\nshow run\n')
time.sleep(3) 
output = new_connection.recv(5000) 
print(output.decode())

print('Closing connection') #종료 출력
new_connection.close()
