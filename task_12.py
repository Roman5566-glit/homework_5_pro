class LoggingMeta(type):
    """Metaclass that logs attribute access and modification"""

    def __new__(mcs, name, bases, dct) -> type:
        """Inject logging methods into the class dictionary"""

        def __getattribute__(self, item) -> object:
            """Log attribute access"""
            print(f"Logging: accessed '{item}'")
            return object.__getattribute__(self, item)

        def __setattr__(self, item, value) -> None:
            """Log attribute modification"""
            print(f"Logging: modified '{item}'")
            return object.__setattr__(self, item, value)

        dct['__getattribute__'] = __getattribute__
        dct['__setattr__'] = __setattr__

        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=LoggingMeta):
    """Class with automatic attribute logging"""

    def __init__(self, name) -> None:
        """Initialize with a name"""
        self.name = name


obj = MyClass("Python")
print(obj.name)
obj.name = "New Python"
