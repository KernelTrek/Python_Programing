# splunk 에서는 log 데이터의 대한 이미지 화 해서 보여줄 수 있다.

import logging

logger = logging.getLogger(__name__)

logger.error('Api call is failed')

logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})

logger.info({
    'action': 'save',
    'csv_file': 'csv_file',
    'force': 'force'
})


logger.info({
    'action': 'save',
    'csv_file': 'csv_file',
    'force': 'force'
})