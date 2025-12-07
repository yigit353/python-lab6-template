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
    Clean a filename: remove whitespace, convert to lowercase
    
    Args:
        filename (str): Raw filename like "  MyFile.TXT  "
    
    Returns:
        str: Cleaned filename like "myfile.txt"
    
    Example:
        clean_filename("  REPORT.PDF  ") → "report.pdf"
    """
    # TODO: Implement (use only basic string methods)
    pass


# ==========================================
# EXERCISE 2: Week 5 Reminder - Dictionary Operations (2 points)
# ==========================================
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries (dict2 overwrites dict1 for same keys)
    
    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary
    
    Returns:
        dict: Merged dictionary
    
    Example:
        merge_dicts({'a': 1}, {'b': 2}) → {'a': 1, 'b': 2}
        merge_dicts({'a': 1}, {'a': 3}) → {'a': 3}
    """
    # TODO: Implement
    pass


# ==========================================
# EXERCISE 3: Week 5 Reminder - Filter List (2 points)
# ==========================================
def filter_by_length(strings, min_len):
    """
    Filter strings by minimum length
    
    Args:
        strings (list): List of strings
        min_len (int): Minimum length required
    
    Returns:
        list: Strings with length >= min_len
    
    Example:
        filter_by_length(['hi', 'hello', 'hey'], 3) → ['hello']
    """
    # TODO: Implement
    pass


# ==========================================
# EXERCISE 4: Week 6 - Simple Class (2 points)
# ==========================================
class Person:
    """
    Simple Person class
    
    Attributes:
        name (str): Person's name
        age (int): Person's age
    
    Methods:
        get_info(): Return formatted string
    """
    def __init__(self, name, age):
        # TODO: Initialize attributes
        pass
    
    def get_info(self):
        """
        Return person information
        
        Returns:
            str: "Name: {name}, Age: {age}"
        """
        # TODO: Implement
        pass


# ==========================================
# EXERCISE 5: Week 6 - Basic Inheritance (2 points)
# ==========================================
class Student(Person):
    """
    Student class inheriting from Person
    
    Additional attribute:
        student_id (str): Student ID
    
    Override get_info() to include student_id
    """
    def __init__(self, name, age, student_id):
        # TODO: Initialize with inheritance
        pass
    
    def get_info(self):
        """
        Return student information
        
        Returns:
            str: "Name: {name}, Age: {age}, ID: {student_id}"
        """
        # TODO: Override method
        pass


# ==========================================
# EXERCISE 6: Week 6 - Method Overriding (2 points)
# ==========================================
class Animal:
    """Base Animal class"""
    def speak(self):
        pass 

class Dog(Animal):
    """
    Dog class that overrides speak method
    """
    def speak(self):
        # TODO: Override method to return "Woof!"
        pass

# ==========================================
# SECTION B: MEDIUM - BASIC OOP CONCEPTS (18 points)
# Core OOP principles (3 points each)
# ==========================================

# ==========================================
# EXERCISE 7: Create Simple Class (3 points)
# ==========================================

# TODO:
#   - Initialize attributes: name, price, quantity
#   - Implement get_total_value() → price × quantity
#   - Implement apply_discount(percent)


class Product:
    """
    Product class for e-commerce system.
    """
    def __init__(self, name, price, quantity):
        pass
    
    def get_total_value(self):
        pass
    
    def apply_discount(self, percent):
        pass


# ==========================================
# EXERCISE 8: Inheritance (3 points)
# ==========================================

# TODO:
#   - Create a Book class inheriting from Product
#   - Add attributes: author, pages
#   - Use super() inside the constructor
#   - Override get_total_value() to include 10% tax


# ==========================================
# EXERCISE 9: Encapsulation (3 points)
# ==========================================
class BankAccount:
    """
    Bank account with encapsulated balance
    - Private attribute: __balance
    - Methods: deposit, withdraw, get_balance
    - Validation: cannot withdraw more than balance
    """
    def __init__(self, initial_balance=0):
        # TODO: Initialize private balance
        pass
    
    def deposit(self, amount):
        # TODO: Add to balance
        pass
    
    def withdraw(self, amount):
        # TODO: Subtract with validation
        pass
    
    def get_balance(self):
        # TODO: Return balance
        pass


# ==========================================
# EXERCISE 10: Polymorphism (3 points)
# ==========================================

# TODO:
#   - Create Dog and Cat classes that inherit from AnimalBase
#   - Override speak() in each:
#       Dog → "Woof!"
#       Cat → "Meow"
#   - Create a function animal_concert(animals) that:
#       - Takes a list of AnimalBase objects
#       - Returns a list of sounds using polymorphism


class AnimalBase:
    def speak(self):
        pass


# ==========================================
# EXERCISE 11: Class Variables (3 points)
# ==========================================
class Employee:
    """
    Employee class with class variable
    - Class variable: total_employees (count all employees)
    - Instance attributes: name, salary
    - Update total_employees in _init_
    """
    total_employees = 0  # Class variable
    
    def __init__(self, name, salary):
        # TODO: Initialize and update class variable
        pass


# ==========================================
# EXERCISE 12: String Representation (3 points)
# ==========================================
class Point:
    """
    2D Point class with string representation
    - Attributes: x, y (integers)
    - Methods:
        _str_(): Return "(x, y)"
        _repr_(): Return "Point(x, y)"
    """
    def __init__(self, x, y):
        # TODO: Initialize
        pass
    
    def _str_(self):
        # TODO: Return human-readable string
        pass
    
    def _repr_(self):
        # TODO: Return code-readable string
        pass


# ==========================================
# SECTION C: HARD - ADVANCED OOP (20 points)
# More complex OOP concepts (5 points each)
# ==========================================

# ==========================================
# EXERCISE 13: Encapsulation and Computed Property (5 points)
# ==========================================

# TODO:
#   - Initialize private attributes __width and __height
#   - Implement set_dimensions(w, h) with validation
#   - Implement get_area()
#   - Implement get_perimeter()


class Rectangle:
    """
    Rectangle class with private attributes and computed values.
    """

    def __init__(self, width, height):
        pass
    
    def set_dimensions(self, w, h):
        pass
        
    def get_area(self):
        pass
        
    def get_perimeter(self):
        pass

# ==========================================
# EXERCISE 14: Class Method for Tracking (5 points)
# ==========================================

# TODO:
#   - Increment the class variable instance_count inside the constructor
#   - Create a class method get_instance_count()
#   - Create a static method is_even(number)


class Counter:
    """
    A class to demonstrate the use of class and static methods.
    
    Class Variable:
        instance_count (int): Tracks how many instances of Counter have been created.
    """
    
    # Class Variable
    instance_count = 0
    
    def __init__(self):
        pass


# ==========================================
# EXERCISE 15: Inheritance and Method Chaining (5 points)
# ==========================================

# TODO:
# Create a subclass named Car that:
#   - Inherits from Vehicle
#   - Has an additional attribute: model
#   - Uses super() in the constructor
#   - Overrides describe() and instead of ending with . also add “, Model: <model_name here>.”

class Vehicle:
    """Base class for all vehicles."""
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
        
    def describe(self):
        return f"Color: {self.color}, Max Speed: {self.max_speed}."


# ==========================================
# EXERCISE 16: Composition over Inheritance (5 points)
# ==========================================

# TODO:
# Create a class named Car that:
#   - Uses composition (has-an Engine)
#   - Has attributes such as brand and engine (Engine instance)
#   - Initializes Engine using the given horsepower
#   - Delegates start() to the engine's start() method

class Engine:
    """Engine component"""
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine ({self.horsepower}HP) started"


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "_main_":
    print("Run 'python lab6_exercises.py' to test your solutions!")