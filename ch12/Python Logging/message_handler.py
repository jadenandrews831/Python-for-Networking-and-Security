import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
fileHandler = logging.FileHandler('debug.log')
fileHandler.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical error message')
