#여러 원격 장에 SSH 접속을 통해 특정 명령을 실행하고 그 결과를 화면에 출력하며 동시에 파일로 저장한 후 연결을 종료하는 코드

import paramiko, getpass, time

devices = {'R1': {'ip': '10.1.1.3'},'S1': {'ip': '10.1.1.11'}}  # 연결할 장비의 이름과 IP 주소
commands = ['show ip int br\n', 'show run\n']  # 실행할 명령어들

username = input('Username: ')  # 사용자 이름 입력 받기
password = getpass.getpass('Password: ')  # 비밀번호 입력 받기

max_buffer = 65535  # 네트워크 장비로부터 수신할 최대 버퍼(데이터) 크기 지정

def clear_buffer(new_connection):  # SSH 연결로부터 데이터를 읽어오는 함수
    if new_connection.recv_ready():  # 데이터를 읽어올 준비가 되어 있으면
        return new_connection.recv(max_buffer)  # 데이터를 읽어와 반환

for device in devices.keys():  # 장비별 루핑
    outputFileName = device + '_output.txt'  # 출력 파일 이름 설정
    ssh_client = paramiko.SSHClient()  # SSH 클라이언트 인스턴스 생성
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 자동으로 호스트 키를 추가하는 정책 설정
    ssh_client.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)  # SSH로 장비에 연결

    new_connection = ssh_client.invoke_shell()  # 새로운 셸 세션 시작
    output = clear_buffer(new_connection)  # 결과 초기화 : 버퍼를 비우고 다음 명령을 실행할 준비
    time.sleep(3)
    new_connection.send("terminal length 0\n")  # "terminal length 0" 명령어 전송
    output = clear_buffer(new_connection)  # 결과 초기화 : 버퍼를 비우고 다음 명령을 실행할 준비

    with open(outputFileName, 'wb') as f:  # 파일을 바이너리 쓰기 모드('wb')로 열고 출력 파일 생성
        for cmd in commands:  # commands 리스트에 있는 각 명령어를 차례로 반복
            new_connection.send(cmd)  # 명령어를 장비에 전송
            time.sleep(3) 
            output = new_connection.recv(max_buffer)  # 결과를 max_buffer 크기만큼 받아옴
            print(output.decode())  # 결과 화면 출력
            f.write(output)  # 결과 파일 저장
    
    new_connection.close()  # 셸 세션 종료





