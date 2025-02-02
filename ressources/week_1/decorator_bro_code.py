# Decorator : A function that extends the behaviour of another function
# without modifying the base function
# It does pass the base function as an argument to the decorator

# Example 
# @add_chocolate
# get_ice_cream("vanilla")
#
#
# The goal here is to "pimp" the current function by adding chocolate, without
# having to modify the current base function (some people might just want plain
# ice cream and not everyone likes having chocolate on their ice-cream)

def add_chocolate(func):
    # The wrapper is MANDATORY if we want to apply this function only when
    # get_ice_cream is called
    def wrapper(*args, **kwargs):
        print("* You added chocolate 🍫 *")
        func(*args, **kwargs)
    return wrapper

def add_salt(func):
    # The *args and **kwargs syntax in Python is used to allow a function to accept
    # an arbitrary number of positional and keyword arguments, respectively.
    # This is particularly useful in decorators because it allows the decorator to be applied to any function,
    # regardless of the number or type of arguments that function takes.
    def wrapper(*args, **kwargs):
        print("* You added salt 🧂 *")
        func(*args, **kwargs)
    return wrapper



# The order of decorators matters
@add_chocolate
@add_salt
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍦")

get_ice_cream("vanilla")



