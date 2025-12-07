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
        """Test cleaning filename with basic operations and edge cases."""
        self.assertEqual(clean_filename("  MyFile.TXT  "), "myfile.txt")
        self.assertEqual(clean_filename("REPORT.PDF"), "report.pdf")
        self.assertEqual(clean_filename("alreadyclean.txt"), "alreadyclean.txt")
        
        # 🔥 TRICK TEST 1: Empty or whitespace-only strings should return an empty string.
        self.assertEqual(clean_filename("   "), "")
        self.assertEqual(clean_filename(""), "")
        
        # 🔥 TRICK TEST 2: String with internal spaces should not be altered aside from case.
        self.assertEqual(clean_filename("  My Document.DOCX  "), "my document.docx")

    # Exercise 2: Week 5 Review - Dictionary Operations
    def test_exercise2_merge_dicts(self):
        """Test merging dictionaries with emphasis on non-destructive operation."""
        # Test normal merge and overwrite
        self.assertEqual(merge_dicts({'a': 1, 'b': 2}, {'c': 3}), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(merge_dicts({'x': 10}, {'x': 20, 'y': 30}), {'x': 20, 'y': 30})
        
        # Test edge cases with empty dictionaries
        self.assertEqual(merge_dicts({}, {'a': 1}), {'a': 1})
        self.assertEqual(merge_dicts({'a': 1, 'b': 2}, {}), {'a': 1, 'b': 2})
        self.assertEqual(merge_dicts({}, {}), {})
        
        # 🔥 TRICK TEST 1: dict1 must not be modified (CRITICAL - catches .update() misuse)
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict1_backup = dict1.copy()
        result = merge_dicts(dict1, dict2)
        self.assertEqual(dict1, dict1_backup, "Original dict1 was modified! It must remain unchanged.")
        
        # 🔥 TRICK TEST 2: dict2 must also not be modified (ADDITIONAL TRICK)
        dict2_backup = dict2.copy()
        result = merge_dicts(dict1, dict2)
        self.assertEqual(dict2, dict2_backup, "Original dict2 was modified! It must remain unchanged.")
        
        # 🔥 TRICK TEST 3: Ensure a NEW dictionary is returned (not one of the inputs)
        # (This test is implicit in the ones above, but can be made explicit)
        self.assertIsNot(result, dict1, "The returned dictionary should be a new object, not dict1.")
        self.assertIsNot(result, dict2, "The returned dictionary should be a new object, not dict2.")

    # Exercise 3: Week 5 Review - List Filtering
    def test_exercise3_filter_by_length(self):
        """Test filtering strings by length with preservation and non-destructive operation."""
        
        # Basic functionality
        self.assertEqual(filter_by_length(['hi', 'hello', 'hey', 'welcome'], 3), 
                         ['hello', 'hey', 'welcome'])
        
        # Edge cases
        self.assertEqual(filter_by_length(['ab', 'abc'], 2), ['ab', 'abc'])
        self.assertEqual(filter_by_length(['test'], 5), [])
        self.assertEqual(filter_by_length([], 3), [])
        
        # 🔥 TRICK 1: Exact length match (boundary condition)
        self.assertEqual(filter_by_length(['cat', 'dog', 'elephant'], 3), 
                         ['cat', 'dog', 'elephant'])
        
        # 🔥 TRICK 2: Original list must not be modified (non-destructive)
        original_list = ['python', 'c', 'java', 'go', 'rust']
        original_copy = original_list.copy()
        result = filter_by_length(original_list, 3)
        self.assertEqual(original_list, original_copy, 
                         "Original list was modified. The function must be non-destructive.")
        
        # 🔥 TRICK 3: Order preservation (important for list comprehensions done wrong)
        self.assertEqual(filter_by_length(['zzz', 'aaa', 'bbb', 'cccc'], 3), 
                         ['zzz', 'cccc'])
        
        # 🔥 TRICK 4: min_len = 0 (should return all strings, including empty ones)
        self.assertEqual(filter_by_length(['', 'a', 'ab'], 0), 
                         ['', 'a', 'ab'])
        
        # 🔥 TRICK 5: Negative min_len (should still work, treat as 0)
        self.assertEqual(filter_by_length(['x', 'yy', 'zzz'], -1), 
                         ['x', 'yy', 'zzz'])
        
    # Exercise 4: Week 6 - Simple Class    
    def test_exercise4_person_class(self):
        """Test Person class with trick tests."""
        # Test 1: Basic attribute assignment and retrieval
        p = Person("Alice", 25)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 25)
        
        # Test 2: Exact format required (string matching)
        self.assertEqual(p.get_info(), "Name: Alice, Age: 25")
        
        # Test 3: 🔥 TRICK - Instance independence
        p2 = Person("Bob", 30)
        p2.name = "Robert"  # Modify one instance
        self.assertEqual(p2.get_info(), "Name: Robert, Age: 30")
        # Ensure original instance is unaffected
        self.assertEqual(p.get_info(), "Name: Alice, Age: 25")
        
        # Test 4: 🔥 TRICK - Method existence and callability
        self.assertTrue(hasattr(p, "get_info"))
        self.assertTrue(callable(p.get_info))
        
        # Test 5: 🔥 TRICK - Return type must be string (not print)
        info = p.get_info()
        self.assertIsInstance(info, str, "get_info() must return a string, not print.")

    # Exercise 5: Week 6 - Basic Inheritance
    def test_exercise5_student_inheritance(self):
        """Test Student inheritance with trick tests focusing on proper inheritance usage."""
        
        # Test 1: Student has all expected attributes
        s = Student("Bob", 20, "S12345")
        self.assertEqual(s.name, "Bob")
        self.assertEqual(s.age, 20)
        self.assertEqual(s.student_id, "S12345")
        
        # Test 2: 🔥 TRICK - Exact output format required (tests override)
        self.assertEqual(s.get_info(), "Name: Bob, Age: 20, ID: S12345")
        
        # Test 3: 🔥 TRICK - Must be a subclass (inheritance required)
        self.assertIsInstance(s, Person)
        self.assertTrue(issubclass(Student, Person))
        
        # Test 4: 🔥 TRICK - Parent and child methods must differ (override check)
        p = Person("Bob", 20)
        self.assertNotEqual(p.get_info(), s.get_info())
        self.assertEqual(p.get_info(), "Name: Bob, Age: 20")
        
        # Test 5: 🔥 TRICK - Instance independence (no shared class variables)
        s2 = Student("Alice", 25, "S999")
        s3 = Student("Charlie", 22, "S888")
        s2.name = "Alicia"
        self.assertEqual(s3.name, "Charlie")  # s3 should not be affected
        
        # Test 6: 🔥 TRICK - New: Student should NOT have a 'person_id' attribute
        # (Catches students who add wrong attribute names)
        self.assertFalse(hasattr(s, 'person_id'), 
                         "Student should have 'student_id', not 'person_id'.")
        
        # Test 7: 🔥 TRICK - New: Ensure Student.__init__ doesn't break Person.__init__
        # Person should still work independently
        p2 = Person("Eve", 30)
        self.assertEqual(p2.get_info(), "Name: Eve, Age: 30")

    # Exercise 6: Week 6 - Method Overriding
    def test_exercise6_method_overriding(self):
        """Test method overriding with focus on proper inheritance and exact output."""
        
        # 🔥 TRICK 1: Animal.speak() should not return a meaningful string
        # (Catches students who make Animal.speak() return something like "Animal sound")
        animal = Animal()
        animal_speak_result = animal.speak()
        self.assertNotEqual(animal_speak_result, "Woof!", 
                          "Animal.speak() should not return 'Woof!'")
        # Allow None, ..., or any non-string
        if animal_speak_result is not None:
            self.assertNotIsInstance(animal_speak_result, str,
                                   "Animal.speak() should not return a string")
        
        # Test Dog class
        dog = Dog()
        
        # 🔥 TRICK 2: Must use inheritance
        self.assertIsInstance(dog, Animal, "Dog must inherit from Animal")
        
        # 🔥 TRICK 3: Exact string "Woof!" required (case-sensitive, punctuation-sensitive)
        self.assertEqual(dog.speak(), "Woof!", 
                        'Dog.speak() must return exactly "Woof!" (with exclamation)')
        
        # 🔥 TRICK 4: Dog.speak() must be different from Animal.speak()
        # Simpler check: Animal's speak should not equal Dog's speak result
        self.assertNotEqual(animal.speak(), dog.speak(),
                          "Dog.speak() should not return the same as Animal.speak()")
        
        # 🔥 TRICK 5: Ensure speak() returns a string (not prints)
        result = dog.speak()
        self.assertIsInstance(result, str,
                            "Dog.speak() must return a string, not just print.")
        
        # 🔥 TRICK 6: Multiple instances work independently
        dog2 = Dog()
        dog3 = Dog()
        dog2.speak()  # Call it
        self.assertEqual(dog3.speak(), "Woof!",
                        "All Dog instances should behave the same")

    # ==========================================
    # SECTION B TESTS: MEDIUM - OOP CONCEPTS (18 points)
    # ==========================================

    # Exercise 7: Classes and Methods
    def test_exercise7_product_class(self):
        """Test Product class with trick tests focusing on state management."""
        
        # Test 1: Basic attributes and total value
        p1 = Product("Laptop", 1000.0, 2)
        self.assertEqual(p1.name, "Laptop")
        self.assertEqual(p1.price, 1000.0)
        self.assertEqual(p1.quantity, 2)
        self.assertEqual(p1.get_total_value(), 2000.0)
        
        # Test 2: Discount correctly modifies price
        p2 = Product("Tablet", 1000.0, 1)
        p2.apply_discount(10)  # 10% discount
        self.assertAlmostEqual(p2.price, 900.0, places=2)
        
        # Test 3: get_total_value() uses updated price
        self.assertAlmostEqual(p2.get_total_value(), 900.0, places=2)
        
        # Test 4: Sequential discounts apply correctly
        p3 = Product("Phone", 1000.0, 1)
        p3.apply_discount(10)  # First 10%
        p3.apply_discount(10)  # Another 10% on discounted price
        self.assertAlmostEqual(p3.price, 810.0, places=2)  # 1000 * 0.9 * 0.9 = 810
        
        # Test 5: Instance independence
        p4 = Product("Item1", 100, 1)
        p5 = Product("Item2", 200, 2)
        p4.apply_discount(50)
        self.assertEqual(p4.price, 50.0)
        self.assertEqual(p5.price, 200.0)
        
        # Test 6: Edge cases - zero price
        p6 = Product("Free", 0, 5)
        self.assertEqual(p6.get_total_value(), 0.0)
        p6.apply_discount(50)
        self.assertEqual(p6.price, 0.0)
        
        # Test 7: Edge cases - zero quantity
        p7 = Product("Sample", 100, 0)
        self.assertEqual(p7.get_total_value(), 0.0)
        
        # Test 8: Discount boundaries
        p8 = Product("Test", 500, 1)
        p8.apply_discount(0)
        self.assertEqual(p8.price, 500.0)
        
        p9 = Product("Test2", 500, 1)
        p9.apply_discount(100)
        self.assertEqual(p9.price, 0.0)
        
        # Test 9: Float precision
        p10 = Product("Precise", 100, 3)
        p10.apply_discount(33)
        self.assertAlmostEqual(p10.price, 67.0, places=2)
        
        # Test 10: Integer to float conversion after discount
        p11 = Product("Integer", 100, 2)
        p11.apply_discount(15)
        self.assertIsInstance(p11.price, (float, int))
        self.assertAlmostEqual(p11.price, 85.0, places=2)

    # Exercise 8: Inheritance and Method Overriding
    def test_exercise8_book_inheritance(self):
        """Test Book inheritance with focus on proper override and independent implementation."""
        
        # Test 1: Book has all expected attributes including inherited ones
        book = Book("Python Guide", 50.0, 3, "John Doe", 300)
        self.assertEqual(book.name, "Python Guide")
        self.assertEqual(book.price, 50.0)
        self.assertEqual(book.quantity, 3)
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.pages, 300)
        
        # Test 2: 🔥 TRICK - Must inherit from Product (type check)
        self.assertIsInstance(book, Product)
        
        # Test 3: 🔥 TRICK - get_total_value() returns a different value than base Product
        # (Tests that override actually changes behavior)
        simple_product = Product("Simple", 50.0, 3)
        book_total = book.get_total_value()
        product_total = simple_product.get_total_value()
        self.assertNotEqual(book_total, product_total,
                          "Book.get_total_value() must return different value than Product")
        
        # Test 4: 🔥 TRICK - The difference should be consistent and significant
        # (Without giving away the formula, test that it's not just a tiny rounding difference)
        difference = abs(book_total - product_total)
        self.assertGreater(difference, 1.0,
                         "Book total should be substantially different from base product total")
        
        # Test 5: 🔥 TRICK - Inheritance should preserve parent methods unless overridden
        # (If Product had other methods, Book should have them too)
        # Create a Product with a hypothetical method to test inheritance structure
        # Actually, we can't test this without defining the method... skip.
        
        # Test 6: 🔥 TRICK - Multiple books are independent
        b1 = Book("Book1", 100.0, 2, "Author1", 200)
        b2 = Book("Book2", 100.0, 2, "Author2", 300)
        # Modify b1's quantity
        b1.quantity = 3
        self.assertEqual(b2.quantity, 2, "Modifying one book should not affect another")
        
        # Test 7: 🔥 TRICK - The calculation should work with edge cases
        free_book = Book("Free", 0.0, 5, "Author", 100)
        self.assertIsInstance(free_book.get_total_value(), (int, float),
                            "get_total_value() should return a number even with zero price")
        
        # Test 8: 🔥 TRICK - The override should handle different numeric inputs
        expensive_book = Book("Expensive", 1000.0, 1, "Author", 500)
        expensive_total = expensive_book.get_total_value()
        self.assertGreater(expensive_total, 1000.0,
                         "With the described modification, total should be greater than price×quantity")

    # Exercise 9: Encapsulation
    def test_exercise9_bank_account_encapsulation(self):
        """Test BankAccount encapsulation with focus on data hiding and validation."""
        
        # Test 1: Initial balance is set correctly
        account = BankAccount(1000)
        self.assertEqual(account.get_balance(), 1000)
        
        # Test 2: Deposits increase balance correctly
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)
        
        # Test 3: Valid withdrawals decrease balance
        account.withdraw(300)
        self.assertEqual(account.get_balance(), 1200)
        
        # Test 4: 🔥 TRICK - Private/mangled attribute should exist
        # Tests that student used name mangling for privacy
        self.assertTrue(hasattr(account, '_BankAccount__balance'),
                       "Balance should be stored with name mangling for privacy")
        
        # Test 5: 🔥 TRICK - No simple public balance attribute
        # Catches students who use self.balance instead of private attribute
        self.assertFalse(hasattr(account, 'balance'),
                        "Should not have a simple public 'balance' attribute")
        
        # Test 6: 🔥 TRICK - Insufficient funds protection
        initial_balance = account.get_balance()
        # Try to withdraw more than available
        withdrawal_result = account.withdraw(initial_balance + 100)
        self.assertEqual(account.get_balance(), initial_balance,
                        "Balance should not change after attempted over-withdrawal")
        
        # Test 7: 🔥 TRICK - Exact balance withdrawal (edge case)
        account2 = BankAccount(500)
        account2.withdraw(500)
        self.assertEqual(account2.get_balance(), 0)
        
        # Test 8: 🔥 TRICK - Negative or zero amounts (should be handled gracefully)
        account3 = BankAccount(1000)
        initial3 = account3.get_balance()
        # This should either fail silently or raise error, but not crash
        try:
            account3.withdraw(-100)
        except (ValueError, TypeError):
            pass  # Acceptable - student implemented validation
        # Balance should not become > initial if negative withdrawal "added" money
        self.assertLessEqual(account3.get_balance(), initial3,
                           "Negative withdrawal should not increase balance")
        
        # Test 9: 🔥 TRICK - Instance independence
        acc1 = BankAccount(100)
        acc2 = BankAccount(200)
        acc1.deposit(50)
        self.assertEqual(acc1.get_balance(), 150)
        self.assertEqual(acc2.get_balance(), 200)
        
        # Test 10: 🔥 TRICK - Method return values
        # get_balance() should return a numeric value
        balance = account.get_balance()
        self.assertIsInstance(balance, (int, float))
        
        # Test 11: 🔥 NEW TRICK - Deposit with zero or negative (optional handling)
        # Some students might validate deposits too
        account4 = BankAccount(100)
        try:
            account4.deposit(0)
        except (ValueError, TypeError):
            pass  # Acceptable if student validates
        # Should not crash at least

    # Exercise 10: Polymorphism
    def test_exercise10_polymorphism(self):
        """Test polymorphism implementation with animal classes."""
        
        # Test 1: Classes can be instantiated
        # (This will fail if classes don't exist or have syntax errors)
        dog = Dog()
        cat = Cat()
        
        # Test 2: 🔥 TRICK - Inheritance must be used
        self.assertIsInstance(dog, AnimalBase)
        self.assertIsInstance(cat, AnimalBase)
        
        # Test 3: 🔥 TRICK - Dog and Cat must return different strings
        dog_sound = dog.speak()
        cat_sound = cat.speak()
        self.assertNotEqual(dog_sound, cat_sound,
                          "Dog and Cat must produce different sounds")
        
        # Test 4: 🔥 TRICK - Both must return strings (not print)
        self.assertIsInstance(dog_sound, str)
        self.assertIsInstance(cat_sound, str)
        
        # Test 5: 🔥 TRICK - Sounds should not be empty or None
        self.assertTrue(len(dog_sound) > 0, "Dog sound should not be empty")
        self.assertTrue(len(cat_sound) > 0, "Cat sound should not be empty")
        
        # Test 6: 🔥 TRICK - animal_concert function exists and works
        animals = [dog, cat, dog]  # 2 dogs, 1 cat
        sounds = animal_concert(animals)
        
        self.assertEqual(len(sounds), 3,
                        "Should return one sound per animal")
        
        # Test 7: 🔥 TRICK - Order preservation in animal_concert
        self.assertEqual(sounds[0], dog_sound)
        self.assertEqual(sounds[1], cat_sound)
        self.assertEqual(sounds[2], dog_sound)
        
        # Test 8: 🔥 TRICK - animal_concert works with empty list
        empty_result = animal_concert([])
        self.assertEqual(empty_result, [])
        
        # Test 9: 🔥 TRICK - animal_concert works with homogeneous list
        three_dogs = [Dog(), Dog(), Dog()]
        dog_sounds = animal_concert(three_dogs)
        self.assertEqual(len(dog_sounds), 3)
        # All should be the same sound
        self.assertEqual(dog_sounds[0], dog_sounds[1])
        self.assertEqual(dog_sounds[1], dog_sounds[2])
        
        # Test 10: 🔥 NEW TRICK - animal_concert should not modify input list
        original_animals = [Dog(), Cat()]
        animals_copy = original_animals.copy()
        animal_concert(original_animals)
        self.assertEqual(original_animals, animals_copy,
                        "animal_concert should not modify the input list")
        
        # Test 11: 🔥 NEW TRICK - AnimalBase.speak() should not return same as Dog or Cat
        base_animal = AnimalBase()
        base_sound = base_animal.speak()
        # Base sound should be different from both Dog and Cat
        # (or could be None/empty, but definitely not the same meaningful string)
        if isinstance(base_sound, str) and len(base_sound) > 0:
            self.assertNotEqual(base_sound, dog_sound,
                              "AnimalBase sound should differ from Dog")
            self.assertNotEqual(base_sound, cat_sound,
                              "AnimalBase sound should differ from Cat")

    def test_exercise11_class_variables(self):
        """Test class variable usage with focus on class-level tracking."""
        
        # Reset any existing class state by getting a fresh reference
        # (This handles test pollution from previous runs)
        from lab6_exercises import Employee
        
        # Test 1: 🔥 TRICK - Class has a class variable (without naming it)
        # Check that Employee has at least one class variable that is a number
        class_vars = [attr for attr in dir(Employee) 
                     if not attr.startswith('__') and not callable(getattr(Employee, attr))]
        
        # Find numeric class variables
        numeric_class_vars = []
        for var_name in class_vars:
            value = getattr(Employee, var_name)
            if isinstance(value, (int, float)):
                numeric_class_vars.append(var_name)
        
        self.assertTrue(len(numeric_class_vars) > 0,
                       "Employee should have at least one numeric class variable")
        
        # Test 2: Class variable changes when instances are created
        initial_value = getattr(Employee, numeric_class_vars[0])
        
        emp1 = Employee("Alice", 50000)
        after_first = getattr(Employee, numeric_class_vars[0])
        self.assertNotEqual(initial_value, after_first,
                           "Creating an instance should change the class variable")
        
        # Test 3: Each new instance changes the class variable
        before_second = getattr(Employee, numeric_class_vars[0])
        emp2 = Employee("Bob", 60000)
        after_second = getattr(Employee, numeric_class_vars[0])
        self.assertNotEqual(before_second, after_second,
                           "Each new instance should update the class variable")
        
        # Test 4: 🔥 TRICK - Instance attributes are set correctly
        self.assertEqual(emp1.name, "Alice")
        self.assertEqual(emp1.salary, 50000)
        self.assertEqual(emp2.name, "Bob")
        self.assertEqual(emp2.salary, 60000)
        
        # Test 5: 🔥 TRICK - The tracking variable is NOT an instance attribute
        # (It should be accessed via the class, not self)
        self.assertFalse(hasattr(emp1, numeric_class_vars[0]),
                        f"'{numeric_class_vars[0]}' should be a class variable, not instance attribute")
        
        # Test 6: 🔥 TRICK - Multiple instances share the same class variable
        emp3 = Employee("Charlie", 70000)
        emp4 = Employee("Diana", 80000)
        
        # All should see the same class variable value
        class_var_name = numeric_class_vars[0]
        value_via_class = getattr(Employee, class_var_name)
        value_via_emp1_class = getattr(emp1.__class__, class_var_name)
        value_via_emp2_class = getattr(emp2.__class__, class_var_name)
        
        self.assertEqual(value_via_class, value_via_emp1_class)
        self.assertEqual(value_via_class, value_via_emp2_class)
        
        # Test 7: 🔥 TRICK - The class variable only increases, never decreases
        # (Simple check that it's monotonic)
        values = []
        for i in range(3):
            emp = Employee(f"Temp{i}", 10000)
            values.append(getattr(Employee, class_var_name))
        
        # Check values are strictly increasing or at least non-decreasing
        for i in range(len(values) - 1):
            self.assertGreaterEqual(values[i + 1], values[i],
                                   "Class variable should not decrease when creating instances")
            
    # Exercise 12: Special Methods (__str__ and __repr__)
    def test_exercise12_string_representation(self):
        """Test __str__ and __repr__ methods with focus on proper implementation."""
        
        # Test 1: Point can be created with coordinates
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)
        
        # Test 2: 🔥 TRICK - __str__ method exists (name check)
        self.assertTrue(hasattr(Point, '__str__'),
                       "Point class must have __str__ method")
        self.assertTrue(callable(point.__str__))
        
        # Test 3: 🔥 TRICK - __repr__ method exists (name check)
        self.assertTrue(hasattr(Point, '__repr__'),
                       "Point class must have __repr__ method")
        self.assertTrue(callable(point.__repr__))
        
        # Test 4: 🔥 TRICK - Both methods return strings
        str_result = str(point)
        repr_result = repr(point)
        
        self.assertIsInstance(str_result, str,
                            "__str__ must return a string")
        self.assertIsInstance(repr_result, str,
                            "__repr__ must return a string")
        
        # Test 5: 🔥 TRICK - __str__ and __repr__ return DIFFERENT strings
        self.assertNotEqual(str_result, repr_result,
                          "__str__ and __repr__ should return different formats")
        
        # Test 6: 🔥 TRICK - __str__ should contain coordinate information
        # (Without specifying exact format)
        self.assertIn("3", str_result,
                     "__str__ should include x coordinate")
        self.assertIn("4", str_result,
                     "__str__ should include y coordinate")
        
        # Test 7: 🔥 TRICK - __repr__ should contain class name and coordinates
        self.assertIn("Point", repr_result,
                     "__repr__ should include class name")
        self.assertIn("3", repr_result,
                     "__repr__ should include x coordinate")
        self.assertIn("4", repr_result,
                     "__repr__ should include y coordinate")
        
        # Test 8: 🔥 TRICK - eval(repr(point)) should create a similar object
        # (Tests that __repr__ is evaluable)
        try:
            new_point = eval(repr_result)
            self.assertEqual(new_point.x, 3)
            self.assertEqual(new_point.y, 4)
            self.assertIsInstance(new_point, Point)
        except:
            self.fail("repr() should return evaluable string that recreates object")
        
        # Test 9: 🔥 TRICK - Different point coordinates
        p2 = Point(10, -5)
        str2 = str(p2)
        repr2 = repr(p2)
        
        self.assertIn("10", str2)
        self.assertIn("-5", str2)
        self.assertIn("10", repr2)
        self.assertIn("-5", repr2)
        
        # Test 10: 🔥 TRICK - __str__ for negative/zero coordinates
        p3 = Point(0, -1)
        str3 = str(p3)
        self.assertIn("0", str3)
        self.assertIn("-1", str3)

    # ==========================================
    # SECTION C TESTS: HARD - ADVANCED OOP (20 points)
    # ==========================================

    # Exercise 13: Encapsulation and Computed Property
    def test_exercise13_rectangle_encapsulation(self):
        """Test Rectangle encapsulation with Hoca's required trick tests."""
        
        # Test 1: Basic calculations work
        rect = Rectangle(10, 20)
        area = rect.get_area()
        perimeter = rect.get_perimeter()
        
        self.assertIsInstance(area, (int, float))
        self.assertIsInstance(perimeter, (int, float))
        # Without giving away formulas, check they're reasonable
        self.assertGreater(area, 0)
        self.assertGreater(perimeter, 0)
        
        # Test 2: Dimensions can be updated
        rect.set_dimensions(15, 25)
        new_area = rect.get_area()
        new_perimeter = rect.get_perimeter()
        
        self.assertNotEqual(area, new_area,
                          "Area should change after set_dimensions")
        self.assertNotEqual(perimeter, new_perimeter,
                          "Perimeter should change after set_dimensions")
        
        # Test 3: 🔥 HOCA'NIN İSTEDİĞİ TRICK - Private name-mangled attributes exist
        # (Catches students who use public attributes like self.width)
        self.assertTrue(hasattr(rect, '_Rectangle__width'),
                       "Must use private __width attribute (name-mangled)")
        self.assertTrue(hasattr(rect, '_Rectangle__height'),
                       "Must use private __height attribute (name-mangled)")
        
        # Test 4: 🔥 HOCA'NIN İSTEDİĞİ TRICK - No simple public attributes
        # (Catches students who use self.width instead of self.__width)
        self.assertFalse(hasattr(rect, 'width'),
                        "Should NOT have public 'width' attribute")
        self.assertFalse(hasattr(rect, 'height'),
                        "Should NOT have public 'height' attribute")
        
        # Test 5: 🔥 TRICK - Validation prevents invalid dimensions
        rect2 = Rectangle(5, 5)
        initial_area = rect2.get_area()
        
        # Try invalid width
        rect2.set_dimensions(-10, 20)
        self.assertEqual(rect2.get_area(), initial_area,
                        "Invalid width should not change dimensions")
        
        # Try invalid height
        rect2.set_dimensions(10, 0)
        self.assertEqual(rect2.get_area(), initial_area,
                        "Invalid height should not change dimensions")
        
        # Try both invalid
        rect2.set_dimensions(-5, -5)
        self.assertEqual(rect2.get_area(), initial_area,
                        "Both invalid should not change dimensions")
        
        # Test 6: 🔥 TRICK - Only update when BOTH are valid
        rect3 = Rectangle(2, 3)
        # Store initial state
        initial_state = (rect3.get_area(), rect3.get_perimeter())
        
        # First invalid attempt (should not change)
        rect3.set_dimensions(0, 10)
        self.assertEqual(rect3.get_area(), initial_state[0],
                        "Should not update with invalid width")
        
        # Then valid update (should change)
        rect3.set_dimensions(4, 6)
        self.assertNotEqual(rect3.get_area(), initial_state[0],
                          "Should update when both dimensions are valid")
        
        # Test 7: 🔥 TRICK - Instance independence
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r1_area_before = r1.get_area()
        r2_area_before = r2.get_area()
        
        r1.set_dimensions(5, 6)
        
        self.assertNotEqual(r1.get_area(), r1_area_before,
                          "r1 should change after set_dimensions")
        self.assertEqual(r2.get_area(), r2_area_before,
                       "r2 should NOT change when r1 is modified")
        
        # Test 8: 🔥 NEW TRICK - get_area and get_perimeter are consistent
        # If w=10, h=20, area=200, perimeter should be 60 (2*(10+20))
        # But we won't specify the formula - just test consistency
        rect4 = Rectangle(7, 11)
        area4 = rect4.get_area()
        perimeter4 = rect4.get_perimeter()
        
        # Quick sanity: if dimensions are positive, perimeter > any single side
        # This catches completely wrong formulas
        self.assertGreater(perimeter4, 7)
        self.assertGreater(perimeter4, 11)
        
        # Test 9: 🔥 NEW TRICK - set_dimensions with same values should work
        rect5 = Rectangle(8, 12)
        area_before = rect5.get_area()
        rect5.set_dimensions(8, 12)  # Same values
        self.assertEqual(rect5.get_area(), area_before,
                        "Setting same dimensions should not break anything")

    # Exercise 14: Class and Static Methods
    def test_exercise14_class_static_methods(self):
        """Test proper use of class and static methods."""
        
        # Reset by re-importing to get fresh class state
        # (Handles test pollution from other tests)
        import importlib
        import lab6_exercises
        importlib.reload(lab6_exercises)
        from lab6_exercises import Counter
        
        # Test 1: Initial state - no instances yet
        initial_count = Counter.get_instance_count()
        self.assertIsInstance(initial_count, (int, float),
                            "get_instance_count() should return a number")
        
        # Test 2: Creating instances increases count
        counter1 = Counter()
        count_after_first = Counter.get_instance_count()
        self.assertNotEqual(initial_count, count_after_first,
                          "Creating instance should change count")
        
        counter2 = Counter()
        count_after_second = Counter.get_instance_count()
        self.assertGreater(count_after_second, count_after_first,
                          "Each new instance should increase count")
        
        # Test 3: 🔥 TRICK - get_instance_count() can be called from class
        # (Tests it's a class method or at least works at class level)
        class_count = Counter.get_instance_count()
        self.assertEqual(class_count, count_after_second)
        
        # Test 4: 🔥 TRICK - get_instance_count() can also be called from instance
        # (Would fail if implemented as regular instance method without @classmethod)
        instance_count = counter1.get_instance_count()
        self.assertEqual(instance_count, class_count,
                        "Instance call should return same as class call")
        
        # Test 5: 🔥 TRICK - is_even() method works correctly
        self.assertTrue(Counter.is_even(4))
        self.assertFalse(Counter.is_even(5))
        self.assertTrue(Counter.is_even(0))
        self.assertTrue(Counter.is_even(-2))
        self.assertFalse(Counter.is_even(-1))
        
        # Test 6: 🔥 TRICK - is_even() can be called from class
        # (Tests it's accessible at class level)
        self.assertIsInstance(Counter.is_even(10), bool)
        
        # Test 7: 🔥 TRICK - is_even() can also be called from instance
        # (Tests it's not an instance method requiring self)
        self.assertIsInstance(counter1.is_even(10), bool)
        
        # Test 8: 🔥 TRICK - is_even() doesn't depend on instance/class state
        # Create new counter, is_even should work the same
        counter3 = Counter()
        # Should get same result regardless of which instance or class
        self.assertEqual(Counter.is_even(8), counter1.is_even(8))
        self.assertEqual(Counter.is_even(8), counter2.is_even(8))
        self.assertEqual(Counter.is_even(8), counter3.is_even(8))
        
        # Test 9: 🔥 TRICK - Class variable is not an instance attribute
        # (Students might incorrectly use instance variable)
        self.assertFalse(hasattr(counter1, 'instance_count'),
                        "Counting should be at class level, not instance")
        
        # Test 10: 🔥 NEW TRICK - Large numbers work with is_even()
        self.assertTrue(Counter.is_even(1000000))
        self.assertFalse(Counter.is_even(1000001))
        
        # Test 11: 🔥 NEW TRICK - Even check works with different numeric types
        # (float with integer value)
        self.assertTrue(Counter.is_even(6.0))
        # (But odd float should still be False)
        self.assertFalse(Counter.is_even(7.0))

    # Exercise 15: Inheritance and Method Chaining
    def test_exercise15_inheritance_method_chaining(self):
        """Test inheritance hierarchy with method overriding and super() usage."""
        
        # Test 1: Both classes can be instantiated
        vehicle = Vehicle("Blue", 150)
        car = Car("Red", 200, "ModelX")
        
        # Test 2: 🔥 TRICK - Car inherits from Vehicle
        self.assertIsInstance(car, Vehicle)
        
        # Test 3: Vehicle has expected attributes
        self.assertEqual(vehicle.color, "Blue")
        self.assertEqual(vehicle.max_speed, 150)
        
        # Test 4: Car has all Vehicle attributes plus its own
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.max_speed, 200)
        # Check for car-specific attribute (name not specified in test)
        # We'll check that car has at least one attribute not in vehicle
        vehicle_attrs = set(dir(vehicle))
        car_attrs = set(dir(car))
        extra_attrs = car_attrs - vehicle_attrs
        # Remove dunder methods and common attributes
        extra_attrs = {a for a in extra_attrs if not a.startswith('__')}
        self.assertTrue(len(extra_attrs) > 0,
                       "Car should have additional attributes beyond Vehicle")
        
        # Test 5: 🔥 TRICK - describe() methods exist and return strings
        vehicle_desc = vehicle.describe()
        car_desc = car.describe()
        
        self.assertIsInstance(vehicle_desc, str)
        self.assertIsInstance(car_desc, str)
        
        # Test 6: 🔥 TRICK - Car.describe() includes Vehicle information
        self.assertIn("Red", car_desc)
        self.assertIn("200", car_desc)
        
        # Test 7: 🔥 TRICK - Car.describe() is different from Vehicle.describe()
        self.assertNotEqual(vehicle_desc, car_desc,
                          "Car should override describe() method")
        
        # Test 8: 🔥 TRICK - Car.describe() includes car-specific information
        # Check that it includes the extra attribute value
        # Since we don't know the attribute name, check for the value
        self.assertIn("ModelX", car_desc)
        
        # Test 9: 🔥 TRICK - Multiple cars work independently
        car2 = Car("White", 180, "Sedan")
        car2_desc = car2.describe()
        self.assertIn("White", car2_desc)
        self.assertIn("180", car2_desc)
        self.assertIn("Sedan", car2_desc)
        self.assertNotEqual(car_desc, car2_desc)
        
        # Test 10: 🔥 NEW TRICK - Vehicle.describe() for different vehicle
        vehicle2 = Vehicle("Green", 120)
        vehicle2_desc = vehicle2.describe()
        self.assertIn("Green", vehicle2_desc)
        self.assertIn("120", vehicle2_desc)
        
        # Test 11: 🔥 NEW TRICK - Method signature compatibility
        # Both describe() methods should take the same parameters (just self)
        import inspect
        vehicle_sig = inspect.signature(vehicle.describe)
        car_sig = inspect.signature(car.describe)
        self.assertEqual(len(vehicle_sig.parameters), len(car_sig.parameters),
                        "describe() should have same parameter count in both classes")
        
    # Exercise 16: Composition over Inheritance
    def test_exercise16_composition_over_inheritance(self):
        """Test composition pattern where objects contain other objects."""
        
        # Test 1: Both classes can be instantiated
        # We don't know class names, so we need to test dynamically
        # Actually, we know from imports, but let's test existence
        
        # Test 2: Create composite object with component
        # Assuming class names are logical
        try:
            vehicle = Car("Toyota", 150)
            component = Engine(150)
        except NameError:
            self.fail("Expected classes (Car and Engine) not defined")
        
        # Test 3: 🔥 TRICK - Vehicle HAS a component (composition)
        self.assertTrue(hasattr(vehicle, 'engine') or hasattr(vehicle, 'motor') or 
                       hasattr(vehicle, 'component'),
                       "Vehicle should contain a component object")
        
        # Find the component attribute
        component_attr = None
        for attr in ['engine', 'motor', 'component', 'powerplant']:
            if hasattr(vehicle, attr):
                component_attr = attr
                break
        
        self.assertIsNotNone(component_attr, 
                            "Vehicle should have a component attribute")
        
        component_obj = getattr(vehicle, component_attr)
        
        # Test 4: Component has power attribute
        self.assertTrue(hasattr(component_obj, 'horsepower') or 
                       hasattr(component_obj, 'power') or
                       hasattr(component_obj, 'capacity'),
                       "Component should have a power/capacity attribute")
        
        # Test 5: Vehicle has brand attribute
        self.assertEqual(vehicle.brand, "Toyota")
        
        # Test 6: 🔥 TRICK - Component power matches initialization value
        # Find the power attribute
        power_attr = None
        for attr in ['horsepower', 'power', 'capacity']:
            if hasattr(component_obj, attr):
                power_attr = attr
                break
        
        self.assertIsNotNone(power_attr, "Component should have power attribute")
        self.assertEqual(getattr(component_obj, power_attr), 150)
        
        # Test 7: Both component and vehicle have activation methods
        self.assertTrue(hasattr(component_obj, 'start') or 
                       hasattr(component_obj, 'activate') or
                       hasattr(component_obj, 'run'),
                       "Component should have activation method")
        
        self.assertTrue(hasattr(vehicle, 'start') or 
                       hasattr(vehicle, 'activate') or
                       hasattr(vehicle, 'run'),
                       "Vehicle should have activation method")
        
        # Test 8: 🔥 TRICK - Vehicle method delegates to component method
        vehicle_method_name = 'start' if hasattr(vehicle, 'start') else \
                             'activate' if hasattr(vehicle, 'activate') else 'run'
        component_method_name = 'start' if hasattr(component_obj, 'start') else \
                               'activate' if hasattr(component_obj, 'activate') else 'run'
        
        vehicle_result = getattr(vehicle, vehicle_method_name)()
        component_result = getattr(component_obj, component_method_name)()
        
        self.assertIsInstance(vehicle_result, str)
        self.assertIsInstance(component_result, str)
        
        # Vehicle result should include component result
        self.assertIn(component_result, vehicle_result,
                     "Vehicle method should incorporate component method result")
        
        # Test 9: 🔥 TRICK - Vehicle result includes vehicle-specific info
        self.assertIn("Toyota", vehicle_result)
        
        # Test 10: 🔥 TRICK - Vehicle result includes component power info
        self.assertIn("150", vehicle_result)
        
        # Test 11: Different vehicle works correctly
        vehicle2 = Car("BMW", 300)
        component_attr2 = None
        for attr in ['engine', 'motor', 'component', 'powerplant']:
            if hasattr(vehicle2, attr):
                component_attr2 = attr
                break
        
        component_obj2 = getattr(vehicle2, component_attr2)
        
        # Find power attribute again
        power_attr2 = None
        for attr in ['horsepower', 'power', 'capacity']:
            if hasattr(component_obj2, attr):
                power_attr2 = attr
                break
        
        self.assertEqual(getattr(component_obj2, power_attr2), 300)
        
        # Test 12: 🔥 NEW TRICK - Components are independent (deep copy)
        # Modifying one vehicle's component shouldn't affect another
        original_power = getattr(component_obj2, power_attr2)
        setattr(component_obj, power_attr, 999)  # Modify first vehicle's component
        
        self.assertEqual(getattr(component_obj2, power_attr2), original_power,
                        "Components should be independent instances")
        
def calculate_score():
    """Calculate and display score"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab6)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(getattr(result, 'skipped', []))  # Skip edilen testler
    passed = total_tests - failures - errors - skipped  # Skip edilenleri çıkar
    
    print("\n" + "=" * 50)
    print(f"LAB 6 RESULTS: {passed}/{total_tests} tests passed")
    print(f"Skipped tests: {skipped}")
    
    # Calculate section scores - ONLY count actually passed tests
    section_a_tests = 6  # Exercises 1-6
    section_b_tests = 6  # Exercises 7-12
    section_c_tests = 4  # Exercises 13-16
    
    # Calculate how many tests passed in each section
    # We need to track which tests belong to which section
    section_a_passed = 0
    section_b_passed = 0
    section_c_passed = 0
    
    # Simpler approach: Track section passes based on test names
    # Count passed tests by checking test names
    if hasattr(result, '_test_run_results'):
        for test_case in result._test_run_results:
            if test_case[0] == 'passed':  # If test passed
                test_name = test_case[1]
                if 'exercise1' in test_name or 'exercise2' in test_name or 'exercise3' in test_name or 'exercise4' in test_name or 'exercise5' in test_name or 'exercise6' in test_name:
                    section_a_passed += 1
                elif 'exercise7' in test_name or 'exercise8' in test_name or 'exercise9' in test_name or 'exercise10' in test_name or 'exercise11' in test_name or 'exercise12' in test_name:
                    section_b_passed += 1
                elif 'exercise13' in test_name or 'exercise14' in test_name or 'exercise15' in test_name or 'exercise16' in test_name:
                    section_c_passed += 1
    
    # Alternative: Use a more robust approach
    section_a_passed = min(passed, 6)  # Max 6 tests in section A
    section_b_passed = max(0, min(passed - section_a_passed, 6))  # Max 6 in B
    section_c_passed = max(0, min(passed - section_a_passed - section_b_passed, 4))  # Max 4 in C
    
    section_a_score = section_a_passed * 2
    section_b_score = section_b_passed * 3
    section_c_score = section_c_passed * 5
    
    total_score = section_a_score + section_b_score + section_c_score
    
    print("\nSECTION SCORES:")
    print(f"Section A (Easy): {section_a_passed}/6 passed = {section_a_score}/12 points")
    print(f"Section B (Medium): {section_b_passed}/6 passed = {section_b_score}/18 points")
    print(f"Section C (Hard): {section_c_passed}/4 passed = {section_c_score}/20 points")
    print(f"\nTOTAL SCORE: {total_score}/44 points")
    print(f"PERCENTAGE: {(total_score/44)*100:.1f}%")
    print("=" * 50)
    
    return total_score

if __name__ == "__main__":
    calculate_score()