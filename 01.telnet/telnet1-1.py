#네트워크를 통한 스크립트 실행에서 발생하는 에러인 buf=self.sock.recv(50) 관련 에러는 특히 타이밍 문제나 네트워크 지연으로 인해 발생할 수 있다.
#네트워크 연결 중 예외가 발생할 수 있으므로, try-except 블록을 사용하여 예외를 처리하고, 연결 문제 발생 시 사용자에게 알려주거나 재시도할 수 있게 할 수 있다.
import getpass
import telnetlib
import time

HOST = "10.1.1.21"
user = input("Enter your telnet username: ")
password = getpass.getpass("Enter your telnet password: ")

max_attempts = 3  # 최대 재시도 횟수
attempt = 0

while attempt < max_attempts:
    try:
        tn = telnetlib.Telnet(HOST, timeout=10)  # 10초 동안 응답 없으면 타임아웃
        tn.read_until(b"Username: ", timeout=10)
        tn.write(user.encode('ascii') + b"\n")

        if password:
            tn.read_until(b"Password: ", timeout=10)
            tn.write(password.encode('ascii') + b"\n")

        # 설정 명령 입력
        tn.write(b"sh ip int br\n")
        tn.write(b"conf t\n")
        tn.write(b"int l0\n")
        tn.write(b"ip add 1.1.1.1 255.255.255.0\n")
        tn.write(b"end\n")
        tn.write(b"sh ip int br\n")
        tn.write(b"exit\n")

        output = tn.read_all().decode('ascii')
        print(output)
        break  # 성공적으로 명령을 실행하고 결과를 출력했으면 루프를 종료
    except (EOFError, ConnectionRefusedError, OSError) as e:
        print(f"An error occurred: {e}")
        attempt += 1
        print(f"Attempting to reconnect... ({attempt}/{max_attempts})")
        time.sleep(5)  # 재시도 전 5초간 대기
    finally:
        tn.close()
