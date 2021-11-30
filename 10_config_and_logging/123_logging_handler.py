import logging

logging.basicConfig(level=logging.INFO)

logging.info('info')

"""
    Logger 를 사용하는 이유
    메인 함수에서 log 레벨을 설정해두고, 
    다른 곳에서 임시로 레벨을 변경하여 보여줄수 있기 때문에 사용함.  
    
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')


# #test
# import logging
#
# logger = logging.getLogger(__name__)