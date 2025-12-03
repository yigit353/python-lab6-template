[file name]: README.md

[file content begin]
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/your-assignment-link-here)

# Lab 6: Object-Oriented Programming (OOP)

## Overview

Master Object-Oriented Programming concepts in Python! This lab introduces classes, inheritance, polymorphism, encapsulation, and advanced OOP patterns - the foundation for building complex, maintainable software.

**Time Limit:** 100 minutes  
**Total Points:** 44 (from autograding)

## 📋 Instructions

### 1. Accept the Assignment

Click the assignment link provided by your instructor to create your personal repository.

### 2. Clone Your Repository

```bash
git clone <your-repository-url>
cd <repository-name>
3. Complete the Exercises
Open lab6_exercises.py and complete each function/class. Write clean, readable OOP code!

4. Test Your Code Locally
bash
python test_lab6.py
This will run all tests and show your score breakdown.

5. Submit Your Work
bash
git add lab6_exercises.py
git commit -m "Complete Lab 6 exercises"
git push
6. Check Autograding Results
Go to your repository on GitHub

Click the "Actions" tab

View the latest workflow run to see your score

Green checkmark ✅ = All tests passed

Red X ❌ = Some tests failed (click to see details)

📚 Exercises
Exercise	Topic	Points	Difficulty
Section A: Easy - Basic Concepts		12	Easy
1	Week 4 Review - String Processing	2	Easy
2	Week 5 Review - Dictionary Operations	2	Easy
3	Week 5 Review - Filter List	2	Easy
4	Simple Class (Person)	2	Easy
5	Basic Inheritance (Student)	2	Easy
6	Method Overriding (Animal/Dog)	2	Easy
Section B: Medium - OOP Concepts		18	Medium
7	Create Product Class	3	Medium
8	Inheritance with Tax (Book)	3	Medium
9	Encapsulation (BankAccount)	3	Medium
10	Polymorphism (Animal Concert)	3	Medium
11	Class Variables (Employee)	3	Medium
12	String Representation (Point)	3	Medium
Section C: Hard - Advanced OOP		20	Hard
13	Property Decorators (Temperature)	5	Hard
14	Class/Static Methods (Calculator)	5	Hard
15	Iterator Protocol (Range)	5	Hard
16	Composition over Inheritance (Car/Engine)	5	Hard
TOTAL		44
🎯 OOP Concepts Covered
Classes and Objects
python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    def get_info(self):   # Instance method
        return f"Name: {self.name}, Age: {self.age}"
Inheritance
python
class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
Encapsulation
python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):  # Public getter
        return self.__balance
Polymorphism
python
class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):  # Override method
        return "Woof!"

# Polymorphic behavior
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Different behavior!
💡 Tips for Success
Section A (Easy - 12 points)
Exercises 1-3: Quick review of Weeks 4-5 concepts

Exercises 4-6: Basic OOP - focus on syntax and simple patterns

Goal: Complete in 20-25 minutes

Section B (Medium - 18 points)
Exercises 7-12: Core OOP principles

Key concepts: Inheritance, encapsulation, polymorphism

Goal: Complete in 35-40 minutes

Section C (Hard - 20 points)
Exercises 13-16: Advanced OOP patterns

Key concepts: Properties, class methods, iterators, composition

Goal: Complete in 35-40 minutes

Time Management
0-25 min: Complete Section A (exercises 1-6)

25-65 min: Complete Section B (exercises 7-12)

65-100 min: Complete Section C (exercises 13-16)

Behind? Get Section A working first!

🔧 Common OOP Patterns
Constructor (__init__)
python
def __init__(self, param1, param2):
    self.attribute1 = param1
    self.attribute2 = param2
Method Overriding
python
class Parent:
    def method(self):
        return "Parent"

class Child(Parent):
    def method(self):  # Override
        return "Child"
Property Decorators
python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
Composition over Inheritance
python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition

    def start(self):
        return self.engine.start()
🚫 Restrictions
NO external libraries (only built-in Python)

NO advanced Python features unless specified

Use proper OOP design (not procedural code in classes)

🐛 Debugging Tips
1. Check Instance Creation
python
obj = MyClass(param1, param2)  # Are parameters correct?
print(obj.attribute)  # Check initialization
2. Test Inheritance
python
child = ChildClass()
print(isinstance(child, ParentClass))  # Should be True
3. Verify Method Overriding
python
parent = ParentClass()
child = ChildClass()
print(parent.method())  # Parent behavior
print(child.method())   # Child behavior (should be different)
4. Test Encapsulation
python
account = BankAccount(1000)
print(account.get_balance())  # Should work
# account.__balance  # Should NOT work directly
📖 Key OOP Principles
1. Abstraction
Hide complex implementation, expose simple interface.

2. Encapsulation
Bundle data and methods, control access.

3. Inheritance
Create new classes from existing ones.

4. Polymorphism
Same interface, different implementations.

🏆 Success Checklist
Before submitting, verify:

All classes have proper __init__ methods

Inheritance uses super().__init__() correctly

Private attributes use __ prefix

Methods are properly overridden

Property decorators are used where appropriate

Tests pass locally: python test_lab6.py

Code follows OOP principles (not procedural in classes)

Code is pushed to GitHub

GitHub Actions shows green checkmark

🆘 When You're Stuck
Review the examples in this README

Check Python documentation for OOP syntax

Test small parts first - create a simple class, then add features

Use print statements to debug attribute values

Ask your TA for OOP-specific guidance

🎓 Learning Objectives
By completing this lab, you will:

✅ Create and use classes effectively

✅ Implement inheritance hierarchies

✅ Apply encapsulation with private attributes

✅ Use polymorphism for flexible code

✅ Understand property decorators

✅ Implement class and static methods

✅ Create custom iterators

✅ Apply composition over inheritance

📚 Resources
Python Documentation
Classes

Inheritance

Properties

Tutorials
Real Python OOP

Python OOP Tutorial

Week 6 Lecture Materials
Review your Week 6 lecture slides for:

Class design patterns

Inheritance strategies

Polymorphism examples

Advanced OOP features

⚙️ Grading
Your grade is automatically calculated:

Section A: 12 points (6 × 2 points)

Section B: 18 points (6 × 3 points)

Section C: 20 points (4 × 5 points)

Total: 44 points

Partial credit is awarded for partially correct solutions.

❓ Need Help?
Check test output - It shows exactly which exercises fail

Review lecture notes - Week 6 covers all OOP concepts

Test incrementally - After each exercise, run tests

Ask during lab hours - TAs can help with OOP design

💪 Final Advice
OOP is a mindset shift! Think in terms of objects and their interactions, not just functions and data.

Good design principles:

Keep classes focused (single responsibility)

Favor composition over inheritance

Use private attributes for encapsulation

Override methods meaningfully

Use properties for computed attributes

Remember: Well-designed OOP code is easier to maintain, extend, and debug!

Good luck! 🚀

Pro Tip: Start with the Person/Student example (exercises 4-6) to build confidence, then tackle the more complex patterns.
```
