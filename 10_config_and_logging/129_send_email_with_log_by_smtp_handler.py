import logging
import logging.handlers

#import config

smtp_host= 'smtp.live.com'
smtp_port= 587

from_email = 'xxxx@hotmail.com'
to_email = 'xxxx@hotmail.com'
username = 'xxxx@hotmail.com'
password = 'werwerwerew'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

# 나중에는 로그 해석 SW 가 해석해서 보내는 것도 가능하다.
logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')