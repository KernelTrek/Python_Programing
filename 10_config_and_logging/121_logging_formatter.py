"""
CRITICAL
ERROR
WARNING

INFO
DEBUG
"""
# log 메세지 관련 정보 
# https://docs.python.org/ko/3/library/logging.html

import logging

# 아래와 같이 표기하면 파이썬이 레벨 네임을 알아서 넣어줌
# formatter = '%(levelname)s:%(message)s'
# logging.basicConfig(level=logging.INFO, format=formatter)
#
# logging.info('info %s %s', 'test', 'test2')

formatter2 = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter2)

logging.info('info %s %s', 'test', 'test2')
