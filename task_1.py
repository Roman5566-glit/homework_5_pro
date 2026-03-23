class MyClass:
    """Store value and greet"""

    def __init__(self, value: str) -> None:
        """Initialize value"""
        self.value = value

    def say_hello(self) -> None:
        """Return greeting"""
        return f"Hello, {self.value}"


def analyze_object(obj: object) -> None: 
    """Print object type and attributes"""
    print(f"Тип об'єкта: {type(obj)}\n")
    print("Атрибути і методи:")

    for attr in dir(obj):
        if attr.startswith("__"):
            continue

        value = getattr(obj, attr)
        print(f"- {attr}: {type(value)}")


obj: MyClass = MyClass("World")

analyze_object(obj)
