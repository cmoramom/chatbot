import logging.handlers
import os
import sys

LOGGER_NAME = 'my-logger'
LOG_FOLDER = './logs/'
LOG_FILE = 'chatbot.log'
LOG = LOG_FOLDER + LOG_FILE
ROTATE_TIME = 'midnight'
LOG_LEVEL = logging.DEBUG
LOG_COUNT = 5
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'

try:
    logger = logging.getLogger(LOGGER_NAME)
    loggerHandler = logging.handlers.TimedRotatingFileHandler(filename=LOG, when=ROTATE_TIME, interval=1,
                                                              backupCount=LOG_COUNT)
    formatter = logging.Formatter(LOG_FORMAT)
    loggerHandler.setFormatter(formatter)
    logger.addHandler(loggerHandler)
    logger.setLevel(LOG_LEVEL)
except Exception as error:
    print("Error with logs: %s" % (str(error)))
    sys.exit()


def get_logger():
    return logger
