import unittest
import sys
import os
from lab6_exercises import *


class TestLab6(unittest.TestCase):

    # ==========================================
    # SECTION A TESTS: EASY - BASIC CONCEPTS (12 points)
    # ==========================================

    # Exercise 1: Week 4 Review - String Processing
    def test_exercise1_clean_filename(self):
        """Test cleaning filename"""
        result = clean_filename("  MyFile.TXT  ")
        self.assertEqual(result, "myfile.txt")
        
        result = clean_filename("REPORT.PDF")
        self.assertEqual(result, "report.pdf")
        
        result = clean_filename("alreadyclean.txt")
        self.assertEqual(result, "alreadyclean.txt")

    # Exercise 2: Week 5 Review - Dictionary Operations
    def test_exercise2_merge_dicts(self):
        """Test merging dictionaries"""
        result = merge_dicts({'a': 1, 'b': 2}, {'c': 3})
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3})
        
        result = merge_dicts({'x': 10}, {'x': 20, 'y': 30})
        self.assertEqual(result, {'x': 20, 'y': 30})
        
        result = merge_dicts({}, {'a': 1})
        self.assertEqual(result, {'a': 1})

    # Exercise 3: Week 5 Review - Filter List
    def test_exercise3_filter_by_length(self):
        """Test filtering strings by length"""
        result = filter_by_length(['hi', 'hello', 'hey', 'welcome'], 3)
        self.assertEqual(result, ['hello', 'hey', 'welcome'])
        
        result = filter_by_length(['a', 'ab', 'abc'], 2)
        self.assertEqual(result, ['ab', 'abc'])
        
        result = filter_by_length(['test'], 5)
        self.assertEqual(result, [])

    # Exercise 4: Week 6 - Simple Class
    def test_exercise4_person_class(self):
        """Test Person class"""
        person = Person("Alice", 25)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 25)
        
        info = person.get_info()
        self.assertIn("Alice", info)
        self.assertIn("25", info)

    # Exercise 5: Week 6 - Basic Inheritance
    def test_exercise5_student_inheritance(self):
        """Test Student inheritance"""
        student = Student("Bob", 20, "S12345")
        self.assertEqual(student.name, "Bob")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.student_id, "S12345")
        
        info = student.get_info()
        self.assertIn("Bob", info)
        self.assertIn("20", info)
        self.assertIn("S12345", info)

    # Exercise 6: Week 6 - Method Overriding
    def test_exercise6_method_overriding(self):
        """Test method overriding"""
        animal = Animal()
        self.assertEqual(animal.speak(), "Animal sound")
        
        dog = Dog()
        self.assertEqual(dog.speak(), "Woof!")
        
        # Check inheritance
        self.assertIsInstance(dog, Animal)

    # ==========================================
    # SECTION B TESTS: MEDIUM - OOP CONCEPTS (18 points)
    # ==========================================

    # Exercise 7: Create Simple Class
    def test_exercise7_product_class(self):
        """Test Product class"""
        product = Product("Laptop", 1000.0, 2)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1000.0)
        self.assertEqual(product.quantity, 2)
        
        total = product.get_total_value()
        self.assertEqual(total, 2000.0)
        
        product.apply_discount(10)  # 10% discount
        self.assertAlmostEqual(product.price, 900.0, places=2)

    # Exercise 8: Inheritance
    def test_exercise8_book_inheritance(self):
        """Test Book inheritance with tax"""
        book = Book("Python Guide", 50.0, 3, "John Doe", 300)
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.pages, 300)
        
        total = book.get_total_value()
        # 50 * 3 = 150, plus 10% tax = 165
        self.assertAlmostEqual(total, 165.0, places=2)

    # Exercise 9: Encapsulation
    def test_exercise9_bank_account_encapsulation(self):
        """Test BankAccount encapsulation"""
        account = BankAccount(1000)
        self.assertEqual(account.get_balance(), 1000)
        
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)
        
        account.withdraw(300)
        self.assertEqual(account.get_balance(), 1200)
        
        # Test insufficient funds
        account.withdraw(2000)
        self.assertEqual(account.get_balance(), 1200)  # Should not change

    # Exercise 10: Polymorphism
    def test_exercise10_polymorphism(self):
        """Test polymorphism with animals"""
        dog = Dog()
        cat = Cat()
        
        animals = [dog, cat]
        sounds = animal_concert(animals)
        
        self.assertEqual(len(sounds), 2)
        self.assertIn("Woof", sounds)
        self.assertIn("Meow", sounds)

    # Exercise 11: Class Variables
    def test_exercise11_class_variables(self):
        """Test class variables"""
        # Reset counter
        Employee.total_employees = 0
        
        emp1 = Employee("Alice", 50000)
        self.assertEqual(Employee.total_employees, 1)
        
        emp2 = Employee("Bob", 60000)
        self.assertEqual(Employee.total_employees, 2)

    # Exercise 12: String Representation
    def test_exercise12_string_representation(self):
        """Test __str__ and __repr__ methods"""
        point = Point(3, 4)
        
        str_result = str(point)
        self.assertEqual(str_result, "(3, 4)")
        
        repr_result = repr(point)
        self.assertEqual(repr_result, "Point(3, 4)")

    # ==========================================
    # SECTION C TESTS: HARD - ADVANCED OOP (20 points)
    # ==========================================

    # Exercise 13: Property Decorators
    def test_exercise13_property_decorators(self):
        """Test property decorators"""
        temp = Temperature(25.0)
        
        self.assertEqual(temp.celsius, 25.0)
        self.assertEqual(temp.fahrenheit, 77.0)  # 25*9/5+32=77
        
        temp.celsius = 30.0
        self.assertEqual(temp.fahrenheit, 86.0)  # 30*9/5+32=86

    # Exercise 14: Class and Static Methods
    def test_exercise14_class_static_methods(self):
        """Test class and static methods"""
        # Reset counter
        Calculator.operation_count = 0
        
        result = Calculator.add(5, 10)
        self.assertEqual(result, 15)
        self.assertEqual(Calculator.operation_count, 1)
        
        result = Calculator.multiply(4, 3)
        self.assertEqual(result, 12)
        self.assertEqual(Calculator.operation_count, 2)

    # Exercise 15: Iterator Protocol
    def test_exercise15_iterator_protocol(self):
        """Test custom iterator"""
        countdown = Range(5, 1)
        results = []
        
        for num in countdown:
            results.append(num)
        
        self.assertEqual(results, [5, 4, 3, 2, 1])
        
        # Test with single iteration
        single = Range(3, 3)
        self.assertEqual(list(single), [3])

    # Exercise 16: Composition over Inheritance
    def test_exercise16_composition(self):
        """Test composition pattern"""
        car = Car("Toyota", 150)
        
        result = car.start()
        self.assertIn("Toyota", result)
        self.assertIn("150HP", result)
        
        # Check that Car has Engine
        self.assertTrue(hasattr(car, 'engine'))
        self.assertIsInstance(car.engine, Engine)


def calculate_score():
    """Calculate and display score"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab6)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total_tests - failures - errors
    
    print("\n" + "=" * 50)
    print(f"LAB 6 RESULTS: {passed}/{total_tests} tests passed")
    
    # Calculate section scores
    section_a = min(passed, 6)  # First 6 tests
    section_b = max(0, min(passed - 6, 6))  # Next 6 tests
    section_c = max(0, min(passed - 12, 4))  # Last 4 tests
    
    section_a_score = section_a * 2  # 2 points each
    section_b_score = section_b * 3  # 3 points each
    section_c_score = section_c * 5  # 5 points each
    
    total_score = section_a_score + section_b_score + section_c_score
    
    print("\nSECTION SCORES:")
    print(f"Section A (Easy): {section_a}/6 passed = {section_a_score}/12 points")
    print(f"Section B (Medium): {section_b}/6 passed = {section_b_score}/18 points")
    print(f"Section C (Hard): {section_c}/4 passed = {section_c_score}/20 points")
    print(f"\nTOTAL SCORE: {total_score}/44 points")
    print(f"PERCENTAGE: {(total_score/44)*100:.1f}%")
    print("=" * 50)
    
    return total_score


if __name__ == "__main__":
    calculate_score()
