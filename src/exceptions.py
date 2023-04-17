class ModuleExistsError(Exception):
    """
        The module is already registered
    """
class ModuleNotFoundError(Exception):
    """
        The module has not been registered yet
    """