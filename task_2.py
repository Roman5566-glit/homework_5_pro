class Calculator:
    def add(self, a: int, b: int | float) -> int | float:
        """Sum two numbers"""
        return a + b

    def subtract(self, a: int, b: int) -> int | float:
        """Subtract two numbers"""
        return a - b


def call_function(obj: object, method_name: str, *args: int | float) -> int | float:
    """Call a method by name"""
    method = getattr(obj, method_name)

    return method(*args)


calc = Calculator()

print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
