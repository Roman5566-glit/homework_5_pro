class LimitedAttributesMeta(type):
    """Metaclass to limit the number of public class attributes"""

    def __new__(mcs: type, name: str, bases: tuple[type], dct: dict[str, object]):
        """Enforce a maximum of 3 public attributes during class creation"""
        count = 0
        for key in dct:
            if not key.startswith("__"):
                count += 1

        if count > 3:
            raise TypeError(f"Клас {name} не може мати більше 3 атрибутів.")

        return super().__new__(mcs, name, bases, dct)


try:
    class LimitedClass(metaclass=LimitedAttributesMeta):
        """Class restricted by LimitedAttributesMeta"""
        attr1 = 1
        attr2 = 2
        attr3 = 3
        # attr4 = 4  # Якщо розкоментувати вилетить помилка


    print("Клас успішно створено!")
except TypeError as e:
    print(e)
