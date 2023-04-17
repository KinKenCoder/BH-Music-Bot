from pymysql import connect
from pymysql.cursors import DictCursor

from src.core import config
from src.base import BaseModule
from src.entity import Query

from src.exceptions import (
    AccessError,
    SQLQueryError
)

class DatabaseModule(BaseModule):
    """
        A module for working with a database
    """
    def __init__(self):
        try:
            self._connection = connect(
                host=config.MYSQL_HOST,
                user=config.MYSQL_USER,
                password=config.MYSQL_PASSWORD,
                database=config.MYSQL_DATABASE,
                cursorclass=DictCursor
            )
        except Exception as message:
            raise AccessError(f"Не удалось подключиться к базе данных. Ошибка: {message}")

    def query(self, sql: str, *params):
        """
        Executes SQL query and commit changes

        :param sql: SQL query
        :param params: SQL query params

        :type sql: str

        :raise SQLQueryError: An error occurred during the execution of the SQL query

        :return: Dictionary of response data
        :rtype: dict
        """
        try:
            response = None
            with self._connection.cursor() as cursor:
                cursor.execute(sql, params)
                if cursor.rowcount == 1:
                    response = cursor.fetchone()
                elif cursor.rowcount > 1:
                    response = cursor.fetchall()
            self._connection.commit()
            return response
        except Exception as message:
            self._connection.rollback()
            raise SQLQueryError(f"Не удалось выполнить SQL запрос \"{sql}\" с параметрами {params}. Ошибка: {message}")

    def transaction(self, *queries: Query):
        """
        Executes a set of SQL queries combined into a transaction and commits changes.
        If at least one of the requests inside the transaction falls, the transaction will be rolled back

        :param queries: A set of SQL queries
        :type queries: list[Query]

        :raise SQLQueryError: An error occurred during the execution of the SQL query

        :return: None
        """
        for query in queries:
            try:
                with self._connection.cursor() as cursor:
                    cursor.execute(query.sql, query.params)
                    if cursor.rowcount == 1:
                        query.response = cursor.fetchone()
                        query.success = True
                    elif cursor.rowcount > 1:
                        query.response = cursor.fetchall()
                        query.success = True
                self._connection.commit()
            except Exception as message:
                self._connection.rollback()
                raise SQLQueryError(f"Не удалось выполнить SQL запрос \"{query.sql}\" с параметрами {query.params}. Ошибка: {message}")
