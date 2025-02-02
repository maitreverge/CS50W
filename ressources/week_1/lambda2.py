# Lamba function = A small anonymous function for a one-time use (throwaway function)
# Lambda syntax: lambda arguments: expression
# They take any number of arguments, but only one expression
# Helps keep the namespace clean and is useful for higher-order functions
# # such as map(), filter(), and reduce()
# Lambda can have any number of arguments, but only one expression
# Lambda functions can be used wherever function objects are required
#

double = lambda x: x * 2
add = lambda x, y: x + y

max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " + last


print(max_value(5, 3))
print(min_value(5, 6))
print(full_name("Tintin", "Didier"))