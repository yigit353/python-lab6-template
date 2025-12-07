# ==========================================
# LAB 6: OBJECT-ORIENTED PROGRAMMING (OOP)
# Advanced Python Course - Week 6
# ==========================================
# 
# INSTRUCTIONS:
# - Use only basic Python and OOP concepts
# - NO external libraries (only built-in)
# - NO advanced Python features unless specified
# - Complete each exercise below
# - Test with: python test_lab6.py
# 
# TOTAL POINTS: 44
# ==========================================

# ==========================================
# SECTION A: EASY - BASIC CONCEPTS (12 points)
# 3 reminders + 3 OOP fundamentals (2 points each)
# ==========================================

# ==========================================
# EXERCISE 1: Week 4 Reminder - String Processing (2 points)
# ==========================================
def clean_filename(filename):
    """
    Given a filename string, clean it by removing any leading/trailing whitespace
    and converting all alphabetical characters to lowercase.
    The function should handle edge cases such as strings that are empty or consist only of spaces.

    Args:
        filename (str): The raw filename provided by the user.

    Returns:
        str: The cleaned filename.
    """
    # TODO: Implement the cleaning logic using basic string methods.
    pass

# ==========================================
# EXERCISE 2: Week 5 Reminder - Dictionary Operations (2 points)
# ==========================================
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries into a new dictionary.
    If a key exists in both dictionaries, the value from dict2 should be used.
    The original dictionaries must not be modified.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.
    """
    # TODO: Implement the merge without modifying the original dictionaries.
    # Hint: Consider how to create a new dictionary and combine key-value pairs.
    pass


# ==========================================
# EXERCISE 3: Week 5 Reminder - Filter List (2 points)
# ==========================================
def filter_by_length(strings, min_len):
    """
    Return a new list containing only the strings from the input list
    whose length is greater than or equal to the specified minimum length.
    The original list must not be modified, and the order of elements
    must be preserved.

    Args:
        strings (list): A list of strings.
        min_len (int): The minimum acceptable length for a string.

    Returns:
        list: A new list containing the filtered strings.
    """
    # TODO: Implement the filter. Ensure the original list remains unchanged.
    pass


# ==========================================
# EXERCISE 4: Week 6 - Simple Class (2 points)
# ==========================================
# TODO: Create a Person class from scratch.
# The class must have:
#   1. An __init__(self, name, age) method that stores the provided name and age.
#   2. Instance attributes named 'name' and 'age'.
#   3. A method named get_info(self) that returns a string in the exact format:
#      "Name: {name}, Age: {age}"
# Important: Do not modify the method signature or attribute names.

# Student writes the class here



# ==========================================
# EXERCISE 5: Week 6 - Basic Inheritance (2 points)
# ==========================================
# TODO: In this exercise, create TWO classes from scratch:
# 
# 1. Person class with:
#    - __init__(self, name, age) method that stores name and age as instance attributes.
#    - get_info(self) method that returns a string: "Name: {name}, Age: {age}"
#
# 2. Student class that INHERITS from Person:
#    - __init__(self, name, age, student_id) method.
#    - Must use super() to initialize the name and age attributes from the parent class.
#    - Add a student_id instance attribute.
#    - Override the get_info() method to return:
#      "Name: {name}, Age: {age}, ID: {student_id}"
#
# Important: Do not copy-paste code from Person to Student. Use proper inheritance.

# Student writes both classes here


# ==========================================
# EXERCISE 6: Week 6 - Method Overriding (2 points)
# ==========================================

# TODO: Create two classes from scratch:
# 
# 1. Animal class:
#    - Has a method called speak(self)
#    - The speak() method should not return any meaningful value.
#      (Use pass or return None)
#
# 2. Dog class:
#    - MUST inherit from Animal
#    - MUST override the speak() method
#    - The overridden speak() method MUST return the exact string: "Woof!"
#
# Write both classes below. Do not include any test code.



# ==========================================
# SECTION B: MEDIUM - BASIC OOP CONCEPTS (18 points)
# Core OOP principles (3 points each)
# ==========================================

# ==========================================
# EXERCISE 7: Create Simple Class (3 points)
# ==========================================
# TODO: Create a Product class from scratch for an e-commerce system.
# 
# The class must have:
#   1. __init__(self, name, price, quantity) method
#      - Stores name, price, and quantity as instance attributes.
#   
#   2. get_total_value(self) method
#      - Returns the total monetary value of the product.
#      - Total value = price × quantity
#   
#   3. apply_discount(self, percent) method
#      - Applies a percentage discount to the product's price.
#      - The discount should permanently reduce the price attribute.
#      - The percent parameter is an integer (e.g., 20 means 20%).
#
# Important: The class should handle its own state; methods should not
# require external calculations. All calculations must be done within
# the class methods.

# Write your Product class below:


# ==========================================
# EXERCISE 8: Inheritance (3 points)
# ==========================================
# TODO: Create a book tracking system using inheritance.
# 
# IMPORTANT: This exercise is COMPLETELY INDEPENDENT from Exercise 7.
# You must create all classes from scratch here.
#
# Create TWO classes:
#
# 1. Product class:
#    - __init__(self, name, price, quantity) method
#    - Stores name, price, and quantity as instance attributes
#    - get_total_value(self) method that returns price multiplied by quantity
#
# 2. Book class (inherits from Product):
#    - __init__(self, name, price, quantity, author, pages) method
#    - Must use super() to initialize name, price, and quantity from Product
#    - Adds two new instance attributes: author and pages
#    - Overrides the get_total_value() method
#    - The overridden method should include an additional calculation
#      beyond the basic price × quantity formula
#
# Note: Do not copy any code from Exercise 7. Write everything fresh.
# The exact nature of the "additional calculation" is part of the challenge.

# Write both classes below:

# ==========================================
# EXERCISE 9: Encapsulation (3 points)
# ==========================================
# TODO: Create a BankAccount class that demonstrates proper encapsulation.
#
# The class should manage a bank account balance with the following requirements:
#
# 1. The balance should be stored in a way that prevents direct external access.
# 2. The class should have an __init__ method that accepts an initial balance.
# 3. It should have methods to deposit money and withdraw money.
# 4. It should have a method to retrieve the current balance.
# 5. Withdrawals should only succeed if sufficient funds are available.
#
# The exact implementation details (attribute names, method signatures, 
# and internal validation logic) are part of the challenge.
#
# Write your BankAccount class below:


# ==========================================
# EXERCISE 10: Polymorphism (3 points)
# ==========================================
# TODO: Create a demonstration of polymorphism with animals.
#
# You need to create the following from scratch:
#
# 1. An AnimalBase class:
#    - Must have a speak(self) method.
#    - The base implementation should not return a meaningful string.
#
# 2. Two subclasses that inherit from AnimalBase:
#    - Dog class
#    - Cat class
#    - Each must override the speak() method.
#    - Each must return a DIFFERENT, specific string when speak() is called.
#
# 3. A function named animal_concert(animals):
#    - Takes a single parameter: a list of AnimalBase objects.
#    - Returns a list of strings.
#    - Should call the speak() method on each object in the list.
#    - Should preserve the order of the input list.
#
# Important: All classes and the function must be written from scratch.
# Do not use any code from previous exercises.

# Write all your code below (classes and function):


# ==========================================
# EXERCISE 11: Class Variables (3 points)
# ==========================================
# TODO: Create an Employee class that demonstrates the use of class variables.
#
# The class should track information at the class level (shared among all instances)
# as well as having regular instance attributes.
#
# Requirements:
#
# 1. The class must have a class-level variable that tracks how many
#    Employee instances have been created.
#
# 2. Each instance should store its own name and salary.
#
# 3. When a new Employee instance is created, the class-level tracking
#    variable should be updated appropriately.
#
# 4. The tracking variable should be accessible at the class level,
#    not requiring an instance to access it.
#
# The exact names of the attributes and implementation details are
# part of the challenge.

# Write your Employee class below:


# ==========================================
# EXERCISE 12: String Representation (3 points)
# ==========================================
# TODO: Create a Point class that represents a 2D point with special string methods.
#
# The class should have:
# 1. An __init__ method that stores x and y coordinates.
# 2. A __str__ method that returns a human-readable string representation.
# 3. A __repr__ method that returns an unambiguous string representation.
#
# Important notes about the special methods:
# - __str__ is called by str(), print(), and format() functions.
# - __repr__ is called by repr() and should ideally allow object recreation.
# - Both methods must return strings.
# - The two methods should return DIFFERENT string formats.
#
# The exact format of the returned strings is part of the challenge.
# Focus on making __str__ user-friendly and __repr__ developer-friendly.

# Write your Point class below:

# ==========================================
# EXERCISE 13: Encapsulation and Computed Property (5 points)
# ==========================================
# TODO: Create a Rectangle class that demonstrates strong encapsulation
# and computed properties.
#
# The class should represent a rectangle with the following requirements:
#
# 1. The rectangle's dimensions should be stored in a way that prevents
#    direct external access or modification.
#
# 2. The class should have an __init__ method to set initial dimensions.
#
# 3. It should have a method to update both dimensions at once,
#    with appropriate validation to ensure only valid dimensions are set.
#
# 4. It should have methods to calculate and return:
#    - The area of the rectangle
#    - The perimeter of the rectangle
#
# 5. The validation should ensure dimensions are valid geometric values.
#
# Important: Focus on proper encapsulation. The internal representation
# should be hidden, and all interactions should go through the class methods.
#
# Write your Rectangle class below:


# ==========================================
# EXERCISE 14: Class Method for Tracking (5 points)
# ==========================================
# TODO: Create a Counter class that demonstrates the use of both
# class methods and static methods.
#
# The class should have the following characteristics:
#
# 1. It should track how many instances of Counter have been created,
#    using a class-level mechanism (not instance-level).
#
# 2. It should provide a way to retrieve the current count of instances
#    through a method that operates at the class level.
#
# 3. It should also provide a utility method that performs a calculation
#    without needing access to any instance or class data.
#    This method should determine whether a given number is even.
#
# Important: Pay attention to which methods should operate on the class
# versus which should be standalone utilities. The method types should
# be chosen appropriately based on their responsibilities.
#
# Write your Counter class below:


# ==========================================
# EXERCISE 15: Inheritance and Method Chaining (5 points)
# ==========================================
# TODO: Create a vehicle class hierarchy demonstrating inheritance
# and method overriding with proper use of super().
#
# You need to create TWO classes from scratch:
#
# 1. A Vehicle base class with:
#    - An __init__ method that takes color and max_speed parameters.
#    - A describe() method that returns a string containing information
#      about the vehicle.
#
# 2. A Car class that inherits from Vehicle:
#    - Should have all the attributes of Vehicle plus an additional
#      attribute specific to cars.
#    - Should override the describe() method to include information
#      from the parent class PLUS the additional car-specific information.
#    - Must use proper inheritance techniques to avoid code duplication.
#
# The exact attribute names, method implementations, and string formats
# are part of the challenge. Focus on creating a logical class hierarchy
# where the child class extends the parent class functionality.
#
# Write both classes below:


# ==========================================
# EXERCISE 16: Composition over Inheritance (5 points)
# ==========================================
# TODO: Create a system demonstrating the "composition over inheritance" principle.
#
# You need to create a small system with two classes that show how objects
# can contain other objects (composition) rather than inheriting from them.
#
# Requirements:
#
# 1. Create a component class that represents a mechanical part with:
#    - A numeric attribute representing its power or capacity.
#    - A method that returns a string describing its activation.
#
# 2. Create a composite class that represents a vehicle with:
#    - An attribute for its brand/make.
#    - An instance of the component class as an attribute (composition).
#    - A method that activates the vehicle by utilizing the component's
#      activation method and combines it with the vehicle's own information.
#
# The key concept is that the vehicle HAS-A component (composition),
# rather than IS-A component (inheritance).
#
# The exact class names, attribute names, method implementations, and
# string formats are part of the challenge.
#
# Write both classes below:


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "_main_":
    print("Run 'python lab6_exercises.py' to test your solutions!")