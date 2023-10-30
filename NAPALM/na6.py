from napalm import get_network_driver

driver = get_network_driver('ios')
router1 = driver('10.1.1.3', 'ccnp', 'cisco',optional_args={'dest_file_system': 'nvram:'} )
router1.open()

print('Accessing 10.1.1.3')
router1.load_merge_candidate(filename='Merge1.cfg') #새로운 설정 로드(병합)

diffs = router1.compare_config() # 변경 사항 확인, 현재 설정과 새로 로드된 설정의 차이점 확인
#만약 변경사항(diffs)이 있다면, 변경사항 commit(적용), 그렇지 않으면 변경사항 폐기(discard)
if len(diffs) > 0:
    print(diffs)
    router1.commit_config()
else:
    print('No changes.')
    router1.discard_config()

router1.close()
