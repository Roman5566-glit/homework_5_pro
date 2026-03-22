class Proxy:
    """Wrapper to log method calls on an object"""

    def __init__(self, obj):
        """Initialize with target object"""
        self.obj = obj

    def __getattr__(self, name):
        """Intercept attribute access and wrap methods"""
        func = getattr(self.obj, name)

        def wrapper(*args):
            print(f"Calling method:\n{name} with args: {args}")
            return func(*args)

        return wrapper


class MyClass:
    """Simple greeting class"""

    def greet(self, name):
        """Return a greeting string"""
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
