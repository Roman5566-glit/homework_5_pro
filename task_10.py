class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists"""
    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        """Return the existing instance or create a new one if it doesn't exist"""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """Class implementing the Singleton pattern"""

    def __init__(self) -> None:
        """Print message upon instantiation"""
        print("Creating instance")


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)
