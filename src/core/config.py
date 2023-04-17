from os import getenv
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


config = Config()
