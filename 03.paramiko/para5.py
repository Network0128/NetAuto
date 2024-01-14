import paramiko, getpass, time, json

with open('devices.json', 'r') as f:  #'devices.json'에서 데이터를 읽어와 devices 딕셔너리에 저장
    devices = json.load(f)

with open('commands.txt', 'r') as f:  #'commands.txt'에서 데이터를 읽어와 각 줄을 commands 리스트의 요소로 저장
    commands = [line for line in f.readlines()]

username = input('Username: ')
password = getpass.getpass('Password: ') 

#나머지 코드는 상기와 같음(생략함)
