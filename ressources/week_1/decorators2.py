# Decorator : Just like we're taking variables and modify them
# Decorators is a way of taking a function and modify it

# In Python, everythin is an object


def hello(func):
    def inner():
        print("Hello ")
        func()

    return inner


def name():
    print("Alice")


obj = hello(name)
obj()
