# String Formatting Basics Example
name = "Alice"
age = 25
message = "Hello, my name is {} and I am {} years old.".format(name, age)
print(message)

# Positional and Keyword Arguments Example
greeting = "Hi, {}! Welcome to {}.".format("Alice", "Python World")
print(greeting)

# Using keyword arguments
greeting_keyword = "Hi, {name}! Welcome to {place}.".format(name="Bob", place="Programming Paradise")
print(greeting_keyword)

#Formatting Numbers Example
pi_value = 3.141592653589793
formatted_pi = "The value of pi is approximately {:.2f}".format(pi_value)
print(formatted_pi)

# F-Strings (Python 3.6 and later) Using f-string
#name = "Alice"
#age = 25
#message = f"Hello, my name is {name} and I am {age} years old."
#print(message)
