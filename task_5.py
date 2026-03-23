class MutableClass:
    """Class for dynamic attribute management"""

    def add_attribute(self, name, value) -> None:
        """Add or update an attribute"""
        setattr(self, name, value)

    def remove_attribute(self, name) -> None:
        """Remove an attribute if it exists"""
        if hasattr(self, name):
            delattr(self, name)
        else:
            print(f"Атрибут '{name}' не знайдено.")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)

obj.remove_attribute("name")
