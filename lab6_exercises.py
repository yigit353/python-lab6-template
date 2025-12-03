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
        return "Animal sound"

class Dog(Animal):
    """
    Dog class that overrides speak method
    
    Methods:
        speak(): Return "Woof!"
    """
    def speak(self):
        # TODO: Override method
        pass


# ==========================================
# SECTION B: MEDIUM - BASIC OOP CONCEPTS (18 points)
# Core OOP principles (3 points each)
# ==========================================

# ==========================================
# EXERCISE 7: Create Simple Class (3 points)
# ==========================================
class Product:
    """
    Product class for e-commerce system
    - Attributes: name (str), price (float), quantity (int)
    - Methods:
        get_total_value(): price × quantity
        apply_discount(percent): reduce price by percentage
    """
    def __init__(self, name, price, quantity):
        # TODO: Initialize attributes
        pass
    
    def get_total_value(self):
        # TODO: Calculate total value
        pass
    
    def apply_discount(self, percent):
        """
        Apply discount to price
        
        Args:
            percent (float): Discount percentage (0-100)
        """
        # TODO: Reduce price by percent
        pass


# ==========================================
# EXERCISE 8: Inheritance (3 points)
# ==========================================
class Book(Product):
    """
    Book class inheriting from Product
    - Additional attributes: author (str), pages (int)
    - Override get_total_value(): include 10% tax for books
    """
    def __init__(self, name, price, quantity, author, pages):
        # TODO: Initialize with inheritance
        pass
    
    def get_total_value(self):
        # TODO: Override to include 10% tax
        pass


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
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    # TODO: Override speak to return "Woof"
    pass

class Cat(Animal):
    # TODO: Override speak to return "Meow"
    pass

def animal_concert(animals):
    """
    Make all animals speak
    
    Args:
        animals (list): List of Animal objects
    
    Returns:
        list: Sounds from each animal
    """
    # TODO: Implement using polymorphism
    pass


# ==========================================
# EXERCISE 11: Class Variables (3 points)
# ==========================================
class Employee:
    """
    Employee class with class variable
    - Class variable: total_employees (count all employees)
    - Instance attributes: name, salary
    - Update total_employees in __init__
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
        __str__(): Return "(x, y)"
        __repr__(): Return "Point(x, y)"
    """
    def __init__(self, x, y):
        # TODO: Initialize
        pass
    
    def __str__(self):
        # TODO: Return human-readable string
        pass
    
    def __repr__(self):
        # TODO: Return code-readable string
        pass


# ==========================================
# SECTION C: HARD - ADVANCED OOP (20 points)
# More complex OOP concepts (5 points each)
# ==========================================

# ==========================================
# EXERCISE 13: Property Decorators (5 points)
# ==========================================
class Temperature:
    """
    Temperature with property decorators
    - Private: __celsius
    - Properties: celsius, fahrenheit
    - fahrenheit = celsius × 9/5 + 32
    """
    def __init__(self, celsius):
        # TODO: Initialize
        pass
    
    @property
    def celsius(self):
        # TODO: Getter
        pass
    
    @celsius.setter
    def celsius(self, value):
        # TODO: Setter
        pass
    
    @property
    def fahrenheit(self):
        # TODO: Computed property
        pass


# ==========================================
# EXERCISE 14: Class and Static Methods (5 points)
# ==========================================
class Calculator:
    """
    Calculator with class/static methods
    - Class variable: operation_count
    - Class method: track_operation()
    - Static methods: add, multiply
    """
    operation_count = 0
    
    @classmethod
    def track_operation(cls):
        """Increment operation count"""
        # TODO: Implement
        pass
    
    @staticmethod
    def add(a, b):
        """Add two numbers and track"""
        # TODO: Implement
        pass
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers and track"""
        # TODO: Implement
        pass


# ==========================================
# EXERCISE 15: Iterator Protocol (5 points)
# ==========================================
class Range:
    """
    Custom range iterator (simplified)
    - Similar to range() but as a class
    - Methods: __init__, __iter__, __next__
    """
    def __init__(self, start, end):
        # TODO: Initialize
        pass
    
    def __iter__(self):
        # TODO: Return iterator
        pass
    
    def __next__(self):
        # TODO: Implement next value
        pass


# ==========================================
# EXERCISE 16: Composition over Inheritance (5 points)
# ==========================================
class Engine:
    """Engine component"""
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine ({self.horsepower}HP) started"

class Car:
    """
    Car using composition (has-an Engine)
    - Instead of inheriting from Engine
    - Car has an Engine instance
    """
    def __init__(self, brand, engine_hp):
        # TODO: Initialize with Engine instance
        pass
    
    def start(self):
        # TODO: Delegate to engine
        pass


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python lab6_exercises.py' to test your solutions!")