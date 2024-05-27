# Cisco IOS 장비에 연결하여 "show ip arp" 명령어를 실행하고 그 결과를 출력합니다.
# 다양한 네트워크 환경에서 느린 장비의 응답을 관리하기 위해 "global_delay_factor": 2 를 사용합니다.

from netmiko import ConnectHandler

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.1.21",
    "username": "ccnp",
    "password": "cisco",
    "global_delay_factor": 2, #﻿모든 지연 시간을 2배로 증가시킨다.
}

command = "show ip arp"
net_connect = ConnectHandler(**router1)
pirnt(net_connect.send_command(command))
net_connect.disconnect()
