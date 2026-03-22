def create_class(class_name, methods):
    """Dynamically create a class with methods"""
    return type(class_name, (), methods)


def say_hello(self):
    """Return hello string"""
    return "Hello!"


def say_goodbye(self):
    """Return goodbye string"""
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())
print(obj.say_goodbye())
