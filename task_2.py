class Calculator:
    def add(self, a, b):
        """Sum two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b


def call_function(obj, method_name, *args):
    """Call a method by name"""
    method = getattr(obj, method_name)

    return method(*args)


calc = Calculator()

print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
