"""
    The main file in which the entire project is configured and the application is launched
"""

from src.core import modules
from src.modules import DatabaseModule

def setup_modules():
    try:
        modules.registry('database', DatabaseModule())
        print("Подключение с базой данных успешно установлено.")
    except Exception as message:
        print(message)
        exit(-1)

def startup():
    setup_modules()


if __name__ == '__main__':
    startup()
