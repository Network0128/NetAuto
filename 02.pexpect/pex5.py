#Python의 pxssh 클래스를 사용하여 SSH로 특정 호스트에 로그인하고, 'show ip int br' 커맨드를 실행한 후 그 결과를 출력하고, 로그아웃하는 것을 자동화
from pexpect import pxssh  # pexpect 모듈에서 pxssh 클래스 임포트

sh = pxssh.pxssh()  # pxssh 객체 생성

sh.login('10.1.1.21', 'ccnp', 'cisco', auto_prompt_reset=False) # 로그인 (호스트 주소, 사용자 이름, 비밀번호 입력)

sh.sendline('show ip int br')  # 'show ip int br' 커맨드 전송

sh.expect('R1#')  # 커맨드 출력 대기

print(sh.before.decode())  # 출력 결과 디코딩 후 출력

sh.logout()  # 로그아웃
