class AutoMethodMeta(type):
    """Metaclass that automatically generates getter and setter methods"""

    def __new__(mcs, name, bases, dct) -> type:
        """Inject get_ and set_ methods for each public class attribute"""
        attributes = [key for key in dct if not key.startswith("__")]

        for attr in attributes:
            def make_getter(a) -> object:
                """Create a getter lambda"""
                return lambda self: getattr(self, a)

            def make_setter(a) -> object:
                """Create a setter lambda"""
                return lambda self, value: setattr(self, a, value)

            dct[f'get_{attr}'] = make_getter(attr)
            dct[f'set_{attr}'] = make_setter(attr)

        return super().__new__(mcs, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    """Class with auto-generated accessors"""
    name: str = "John"
    age: int = 30


p = Person()
print(p.get_name())
p.set_age(31)
print(p.get_age())
