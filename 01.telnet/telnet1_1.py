#네트워크를 통한 스크립트 실행에서 발생하는 에러인 buf=self.sock.recv(50) 관련 에러는 특히 타이밍 문제나 네트워크 지연으로 인해 발생할 수 있다.
#네트워크 연결 중 예외가 발생할 수 있으므로, try-except 블록을 사용하여 예외를 처리하고, 연결 문제 발생 시 사용자에게 알려주거나 재시도할 수 있게 할 수 있다.
#코드 주요 내용
#루프와 조건 : while 루프를 사용하여 최대 재시도 횟수에 도달할 때까지 네트워크 연결 시도를 계속합니다.
#예외 처리 : try-except 블록을 사용해 네트워크 관련 예외를 처리하며, 발생한 오류를 사용자에게 알립니다.
#재시도 로직 : 예외 발생 시 재시도 메커니즘을 통해 연결을 다시 시도하고, 각 시도 사이에는 5초 간격을 둡니다.
#자원 정리 : finally 블록에서는 세션을 안전하게 종료합니다, tn.close()를 호출하여 모든 시나리오에서 리소스가 해제되도록 합니다.
#이 스크립트는 네트워크 연결의 문제에 더욱 견딜 수 있도록 설계되었으며, 사용자에게 발생 가능한 오류에 대해 피드백을 제공합니다.

#코드 3줄 요약
#이 스크립트는 최대 3번의 재시도를 허용하면서 telnetlib을 사용하여 지정된 호스트에 텔넷 연결을 시도합니다.
#사용자 이름과 비밀번호를 입력 받아 서버에 로그인하고, 네트워크 인터페이스 설정을 변경하는 명령어를 전송합니다.
#연결 중 발생할 수 있는 예외(예: 연결 거부, 네트워크 오류)를 처리하고, 오류 발생 시 재연결을 시도하며, 각 시도 사이에 5초의 대기 시간을 가집니다.

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
