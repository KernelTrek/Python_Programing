import logging
import logtest

logging.basicConfig(level=logging.INFO)

# log 기록시, 특정 키워드에 대해서 기록하지 않도록 하는 것
class NoPassFilter(logging.Filter):
    def filter(self, record) -> bool:
        log_message = record.getMessage()
        return 'password' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test"')
logger.info('from main xxxx = "test"')
