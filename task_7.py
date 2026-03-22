def log_methods(cls):
    """Class decorator to log all public method calls"""
    for name in dir(cls):
        attr = getattr(cls, name)

        if callable(attr) and not name.startswith("__"):
            def make_wrapper(method, method_name):
                def wrapper(self, *args):
                    """Log call and execute original method"""
                    print(f"Logging: {method_name} called with {args}")
                    return method(self, *args)

                return wrapper

            setattr(cls, name, make_wrapper(attr, name))

    return cls


@log_methods
class MyClass:
    """Class with logged operations"""

    def add(self, a, b):
        """Return sum of two numbers"""
        return a + b

    def subtract(self, a, b):
        """Return difference of two numbers"""
        return a - b


obj = MyClass()
obj.add(5, 3)
obj.subtract(5, 3)
