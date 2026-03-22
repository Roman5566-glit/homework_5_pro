import inspect
import importlib


def analyze_module(module_name):
    """Import and list built-in functions of a module"""
    module = importlib.import_module(module_name)

    print("Функції:\n")
    for name, obj in inspect.getmembers(module):
        if inspect.isbuiltin(obj):
            print("-", name)

    print("\nКласи:\n- <немає класів у модулі>")


analyze_module("math")
