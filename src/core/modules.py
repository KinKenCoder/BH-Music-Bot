from src.base import BaseModule
from src.exceptions import (
    ModuleExistsError,
    ModuleNotFoundError
)

class ModulesStorage:
    """
        The class is intended for storing instances of modules
    """
    def __init__(self):
        self._modules = {}

    def registry(self, name: str, module: BaseModule):
        """
        The method registers the passed instance of the module, assigning it the passed name

        :param name: Module name
        :param module: An instance of a module inherited from BaseModule

        :type name: str
        :type module: BaseModule

        :raise TypeError: A module instance is not an inheritor of a BaseModule
        :raise ModuleExistsError: A module with this name has already been registered

        :return: None
        """
        if not isinstance(module, BaseModule):
            raise TypeError(f"Модуль {name} не является наследником BaseModule.")
        if name in self._modules:
            raise ModuleExistsError(f"Модуль с именем {name} уже зарегистрирован.")
        self._modules[name] = module

    def find(self, name: str) -> BaseModule:
        """
        The method returns a registered instance of the module

        :param name: Module name

        :type name: str

        :raise ModuleNotFoundError: The module with the specified name is not registered

        :return: An instance of the module with the specified name
        :rtype: BaseModule
        """
        if name not in self._modules.keys():
            raise ModuleNotFoundError(f"Модуль с именем {name} еще не зарегистрирован.")
        return self._modules[name]


modules = ModulesStorage()
