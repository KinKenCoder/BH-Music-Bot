class ModuleExistsError(Exception):
    """
        The module is already registered
    """
class ModuleNotFoundError(Exception):
    """
        The module has not been registered yet
    """
class AccessError(Exception):
    """
        There are no rights to perform this action
    """
class SQLQueryError(Exception):
    """
        An error occurred during the execution of the SQL query
    """