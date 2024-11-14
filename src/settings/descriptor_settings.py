from typing import Any


class DescriptorSettings:

    def __set_name__(self, owner, name):
        self.__name = "__" + name

    def __get__(self, instance, owner) -> Any:
        return getattr(instance, self.__name)

    def __set__(self, instance, value) -> None:
        if hasattr(instance, str(self.__name)):
            return None
        setattr(instance, self.__name, value)
