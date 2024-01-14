#여러 원격 장비(R1,S1)에 SSH로 접속 후 특정 명령을 실행하고 그 결과를 출력한 후 연결을 종료하는 코드

import paramiko,time 

ssh_client = paramiko.SSHClient()  # SSH 클라이언트 인스턴스 생성
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 자동으로 호스트 키를 추가하는 정책 설정

# Router1과 Server1에 대한 접속 정보를 담은 딕셔너리
R1={'hostname':'10.1.1.21','port':'22','username':'ccnp','password':'cisco'}
S1={'hostname':'10.1.1.11','port':'22','username':'ccnp','password':'cisco'}

routers=[R1,S1]  # 두 딕셔너리를 리스트에 저장

for router in routers:  # 각 딕셔너리에 대해 반복
    print(f'Connecting to {router["hostname"]}')  # 접속 시작 메시지 출력
    ssh_client.connect(**router,look_for_keys=False,allow_agent=False)  # SSH로 원격 서버에 접속

    new_connection = ssh_client.invoke_shell()  # 새로운 셸 세션 시작
    output = new_connection.recv(5000)  # 셸 세션에서 출력된 데이터를 읽어옴
    print(output.decode())  # 출력된 데이터를 디코딩하여 출력
    
    new_connection.send('terminal length 0\nshow run\n')  # 원격 서버에 명령어 전송
    time.sleep(3)  # 3초 동안 대기
    output = new_connection.recv(5000)  # 셸 세션에서 출력된 데이터를 읽어옴
    print(output.decode())  # 출력된 데이터를 디코딩하여 출력

    print('Closing connection')  # 연결 종료 메시지 출력
    new_connection.close()  # 셸 세션 종료
