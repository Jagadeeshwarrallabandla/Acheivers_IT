#Calculating the Area of the Circle

import math
def circle_area(radius):
    area_of_the_circle = math.pi * radius**2
    return area_of_the_circle
print(circle_area(2))

'''mobile_list = [
    {"name" : "real me","price":29999,"processor":"snapdragon 720"},
    {"name" : "iphone","price":199999,"processor":"A-17"},
    {"name" : "One plus","price":29999,"processor":"snapdragon 820"}
    ]
for mobiles in mobile_list:
    print(mobiles)'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of" "is:", factorial(5))


'''def reverse_string_loop(input_string):
    """
    Reverse a string using a loop.

    Args:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    reversed_string = ""
    for cha in input_string:
        reversed_string = cha + reversed_string
    return reversed_string'''

# Example usage:
'''input_string = "hello"
print("Original string:", input_string)
print("Reversed string:", reverse_string_loop(input_string))

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 22},
    {"name": "David", "age": 19}
]
sorted_students  = sorted(students["age"])
for students in sorted_students:
    print(student)'''

def is_valid_identifier(string):
    """
    Check if a given string is a valid Python identifier.

    Args:
    string (str): The string to be checked.

    Returns:
    bool: True if the string is a valid identifier, False otherwise.
    """
    return string.isidentifier()

# Test cases
strings = ["hello", "_hello", "42hello", "hello world", "if", "def", "for"]
for string in strings:
    print(f"'{string}' is a valid identifier:", is_valid_identifier(string))

a = 12
print(id(a))
b = 10
print(id(b))
print(a is b)

a =[1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))

def add_elements_to_list(my_list, *elements):
    """
    Add elements to a list and return the updated list.

    Args:
    my_list (list): The original list.
    elements (tuple): Elements to add to the list.

    Returns:
    list: The updated list after adding the elements.
    """
    for index, element in enumerate(elements):
        my_list.insert(index, element)
    return my_list
    print(my_list)


my_details = {'name' : 'jagadeesh','gender' : 'male'}
print(my_details['name'])

# Define a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Iterate over the dictionary and print keys and values
print("Keys and Values:")
for values in my_dict:
    print(f"Key: {values}")
    
def reverse_string_slicing(input_string):
    return input_string[::-2]

# Example usage
original_string = "hello"
reversed_string = reverse_string_slicing(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)

'''students = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 18},
    {'name': 'David', 'age': 25}
]
sorted_items = students.sorted(['age'])
print(sorted_items)'''

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
upper_list = [item.upper() for item in my_list]
print("Uppercase list:", upper_list)

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Iterate over the dictionary and print keys and values
print("Keys and Values:")
for key, value in my_dict.items():
    print(key, value)
names = [1,2,3,4]
def add():
    add_list = [5,6,7,8]
    add_list += names
    
    print(add_list)
    
add()




