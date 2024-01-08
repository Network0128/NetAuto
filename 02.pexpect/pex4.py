#Python의 pexpect 모듈을 사용하여 SSH로 특정 호스트에 접속하고, 'sh ip int br' 커맨드를 실행한 후 그 결과를 출력하고, 세션을 종료하는 것을 자동화

import pexpect  # pexpect 라이브러리 임포트

ssh_session = pexpect.spawn("ssh ccnp@10.1.1.21")  # SSH 세션을 위한 pexpect 생성 객체

ssh_session.expect("Password:")  # 비밀번호 프롬프트 대기

ssh_session.sendline("cisco")  # 비밀번호 전송

ssh_session.expect("R1#")  # 프롬프트 대기

ssh_session.sendline("sh ip int br")  # 커맨드 전송

ssh_session.expect("R1#")  # 프롬프트 대기

print(ssh_session.before.decode())  # 출력 결과 디코딩 후 출력

ssh_session.close()  # SSH 세션 종료
