def create_class(class_name: str, methods: dict) -> type:
    """Dynamically create a class with methods"""
    return type(class_name, (), methods)


def say_hello(self) -> str:
    """Return hello string"""
    return "Hello!"


def say_goodbye(self) -> str:
    """Return goodbye string"""
    return "Goodbye!"


methods: dict = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass: type = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())
print(obj.say_goodbye())
