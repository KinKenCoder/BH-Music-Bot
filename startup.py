"""
    The main file in which the entire project is configured and the application is launched
"""

from src.core import modules
from src.modules import DatabaseModule
from src.entity import Query
from src.utils import wlogger

def setup_modules():
    try:
        modules.registry('database', DatabaseModule())
        wlogger.startup("Подключение с базой данных успешно установлено.")
    except Exception as message:
        wlogger.critical(message)
        exit(-1)

def setup_database():
    database: DatabaseModule = modules.find('database')
    try:
        database.transaction(
            Query("CREATE TABLE IF NOT EXISTS `bhm_users` (`id` INT(11) NOT NULL AUTO_INCREMENT, `telegram_id` BIGINT(20) NOT NULL, `telegram_name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci', `is_admin` TINYINT(4) NOT NULL DEFAULT '0', `date_registration` TIMESTAMP NOT NULL DEFAULT current_timestamp(), `date_update` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(), PRIMARY KEY (`id`) USING BTREE, UNIQUE INDEX `telegram_id` (`telegram_id`) USING BTREE) COLLATE='utf8mb4_general_ci' ENGINE=InnoDB;")
        )
        wlogger.startup("Миграции успешно выполнены. База данных сконфигурирована.")
    except Exception as message:
        wlogger.critical(message)
        exit(-1)

def startup():
    setup_modules()
    setup_database()


if __name__ == '__main__':
    startup()
