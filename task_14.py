class TypeCheckedMeta(type):
    """Metaclass that enforces type hints during attribute assignment"""

    def __new__(mcs, name, bases, dct):
        """Inject a type-checking __setattr__ into the class"""

        def __setattr__(self, key, value):
            """Validate value type against class annotations before setting"""
            annotations = getattr(self, '__annotations__', {})

            if key in annotations:
                expected_type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Для атрибута '{key}' очікується тип '{expected_type.__name__}', "
                        f"але отримано '{type(value).__name__}'."
                    )

            super(type(self), self).__setattr__(key, value)

        dct['__setattr__'] = __setattr__
        return super().__new__(mcs, name, bases, dct)


class Person(metaclass=TypeCheckedMeta):
    """Class with enforced type checking"""
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"

try:
    p.age = "30"
except TypeError as e:
    print(e)
