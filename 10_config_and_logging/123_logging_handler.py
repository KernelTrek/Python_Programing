# logging 핸들러를 사용하면, 별도로 파일에 기록할 수 있다. 
# https://docs.python.org/ko/3.7/library/logging.handlers.html

import logging
import logtest

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info('from main')

logtest.do_something()


# #test
# import logging
#
# logger = logging.getLogger(__name__)