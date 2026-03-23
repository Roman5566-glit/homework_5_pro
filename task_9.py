class DynamicProperties:
    """Manage dynamic properties using class-level descriptors"""

    def __init__(self) -> None:
        """Initialize value storage"""
        self._values = {}

    def add_property(self, name, default_value) -> None:
        """Dynamically add a property with getter and setter"""
        self._values[name] = default_value

        def getter(instance) -> object:
            """Return the property value"""
            return instance._values[name]

        def setter(instance, value) -> None:
            """Set the property value"""
            instance._values[name] = value

        setattr(self.__class__, name, property(fget=getter, fset=setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')

print(obj.name)

obj.name = "Python"
print(obj.name)
