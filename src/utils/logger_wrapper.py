from sys import stdout
from loguru import logger

from src.core import config

class LoggerWrapper:

    STARTUP_LEVEL = "STARTUP"

    def __init__(self):
        self.startup_logger()
        self.create_custom_levels()

    def startup_logger(self):
        """
        Configuring the standard logger

        :return: None
        """
        logger.remove(0)
        logger.add(stdout, format=config.LOG_FORMAT)
        logger.add(config.LOG_FILE_PATH, format=config.LOG_FORMAT, rotation=config.LOG_ROTATION, compression='zip')

    def create_custom_levels(self):
        """
        Registration of custom logger levels

        :return: None
        """
        logger.level(self.STARTUP_LEVEL, no=20, color='<blue>', icon='🚀')

    def trace(self, message):
        logger.trace(message)

    def debug(self, message):
        logger.debug(message)

    def startup(self, message):
        logger.log(self.STARTUP_LEVEL, message)

    def info(self, message):
        logger.info(message)

    def success(self, message):
        logger.success(message)

    def warning(self, message):
        logger.warning(message)

    def error(self, message):
        logger.error(message)

    def critical(self, message):
        logger.critical(message)


wlogger = LoggerWrapper()
