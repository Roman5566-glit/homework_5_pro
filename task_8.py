def analyze_inheritance(cls):
    """Identify and print methods inherited from parent classes"""
    print(f"Клас {cls.__name__} наслідує:")

    for parent in cls.__mro__[1:]:
        if parent is object:
            continue

        for name in dir(parent):
            if callable(getattr(parent, name)) and not name.startswith("__"):
                if name not in cls.__dict__:
                    print(f"- {name} з {parent.__name__}")


class Parent:
    """Base class with a sample method."""

    def parent_method(self):
        """Placeholder parent method"""
        pass


class Child(Parent):
    """Subclass with a sample method"""

    def child_method(self):
        """Placeholder child method"""
        pass


analyze_inheritance(Child)
