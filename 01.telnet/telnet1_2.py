# 네트워크 통신 중 발생할 수 있는 타이밍 문제나 지연으로 인해 예외가 발생할 수 있습니다.
# 이러한 예외를 처리하기 위해 try-except 블록을 사용하여 연결 문제가 발생할 경우 사용자에게 알리고 재시도할 수 있습니다.
# 코드 주요 내용:
# 루프와 조건: 최대 재시도 횟수에 도달할 때까지 while 루프를 사용하여 네트워크 연결을 시도합니다.
# 예외 처리: 네트워크 관련 예외를 처리하고, 발생한 오류를 사용자에게 알려줍니다.
# 재시도 로직: 예외 발생 시 재시도 메커니즘을 통해 연결을 다시 시도하며, 각 시도 사이에는 5초의 대기 시간을 둡니다.
# 자원 정리: finally 블록에서는 telnet 세션을 안전하게 종료하여 모든 시나리오에서 리소스가 해제되도록 합니다.
# 이 스크립트는 네트워크 연결의 문제에 견딜 수 있도록 설계되었으며, 발생 가능한 오류에 대해 사용자에게 피드백을 제공합니다.

# 코드 3줄 요약:
# 이 스크립트는 최대 3번의 재시도를 허용하며 telnetlib을 사용해 지정된 호스트에 텔넷 연결을 시도합니다.
# 사용자 이름과 비밀번호를 사용하여 서버에 로그인하고 네트워크 인터페이스 설정 변경 명령을 전송합니다.
# 연결 중 발생할 수 있는 예외(예: 연결 거부, 네트워크 오류)를 처리하고, 오류 발생 시 재연결을 시도하며, 각 시도 사이에는 5초의 대기 시간을 둡니다.

import telnetlib
import time

# 네트워크 장비 호스트 IP
HOST = "10.1.1.21"
# 미리 정의된 사용자 이름과 비밀번호
user = "ccnp"
password = "cisco"

# 최대 재시도 횟수 설정
max_attempts = 3
attempt = 0

# 네트워크 연결을 위한 while 루프. 최대 재시도 횟수까지 시도
while attempt < max_attempts:
    try:
        tn = telnetlib.Telnet(HOST, timeout=10)  # 응답 대기 타임아웃 설정
        tn.read_until(b"Username: ", timeout=10)
        tn.write(user.encode('ascii') + b"\n")

        if password:
            tn.read_until(b"Password: ", timeout=10)
            tn.write(password.encode('ascii') + b"\n")

        # 네트워크 설정 변경 명령어 입력
        tn.write(b"sh ip int br\n")
        tn.write(b"conf t\n")
        tn.write(b"int l0\n")
        tn.write(b"ip add 1.1.1.1 255.255.255.0\n")
        tn.write(b"end\n")
        tn.write(b"sh ip int br\n")
        tn.write(b"exit\n")

        # 결과 출력
        output = tn.read_all().decode('ascii')
        print(output)
        break  # 명령 실행 완료 후 루프 종료
    except (EOFError, ConnectionRefusedError, OSError) as e:
        # 예외 처리: 연결 오류 발생 시
        print(f"An error occurred: {e}")
        attempt += 1
        print(f"Attempting to reconnect... ({attempt}/{max_attempts})")
        time.sleep(5)  # 재시도 전 5초 대기
    finally:
        # 세션 안전 종료
        tn.close()
