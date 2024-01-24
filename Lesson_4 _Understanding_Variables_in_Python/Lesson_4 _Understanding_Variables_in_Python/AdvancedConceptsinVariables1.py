# Global Variables Example
global_var = 50

def my_function():
    print("Accessing global_var within the function:", global_var)

my_function()


# Local Variables Example 
def my_function():
    local_var = 10
    print("Accessing local_var within the function:", local_var)

my_function()


# Global vs. Local Variables Example
common_var = "I am global"

def my_function():
    common_var = "I am local"
    print(common_var)

my_function()
print("Accessing common_var outside the function:", common_var)


# Constants and Enumerations Example
PI = 3.14159
MAX_SIZE = 100

#Variable Swapping Example
a = 5
b = 10

a, b = b, a

print("a after swapping:", a)
print("b after swapping:", b)

