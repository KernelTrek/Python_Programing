"""
CRITICAL
ERROR
WARNING

INFO
DEBUG
"""

import logging

# 기본 설정은 WARNING부터 경고 표시 됨으로, Debug 부터 출력하고자 한다면 아래와 같이 수행
# 실제 배포시에는 INFO 부터 시작하는 편임...
# 파일을 지정하여 로그를 저장하도록도 할수 있음. 
logging.basicConfig(filename="test.log", level=logging.DEBUG)
#logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

print("------------------------------")
logging.info(f'info {"test"}')

