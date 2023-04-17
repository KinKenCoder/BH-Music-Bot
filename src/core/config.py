from os import getenv, path
from dotenv import load_dotenv

class Config:
    """
        A class for storing all data from an .env file
    """
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
        self.MYSQL_HOST = getenv('MYSQL_HOST')
        self.MYSQL_USER = getenv('MYSQL_USER')
        self.MYSQL_PASSWORD = getenv('MYSQL_PASSWORD')
        self.MYSQL_DATABASE = getenv('MYSQL_DATABASE')
        self.LOG_FILE = getenv('LOG_FILE')
        self.LOG_DIR_PATH = getenv('LOG_DIR_PATH')
        self.LOG_FILE_PATH = path.join(self.LOG_DIR_PATH, self.LOG_FILE)
        self.LOG_ROTATION = getenv('LOG_ROTATION')
        self.LOG_FORMAT = getenv('LOG_FORMAT')


config = Config()
