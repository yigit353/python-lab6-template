import unittest

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
        
        # TRICK TEST 1: Empty or whitespace-only strings should return an empty string.
        self.assertEqual(clean_filename("   "), "")
        self.assertEqual(clean_filename(""), "")
        
        # TRICK TEST 2: String with internal spaces should not be altered aside from case.
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
        
        # TRICK TEST 1: dict1 must not be modified (CRITICAL - catches .update() misuse)
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict1_backup = dict1.copy()
        result = merge_dicts(dict1, dict2)
        self.assertEqual(dict1, dict1_backup, "Original dict1 was modified! It must remain unchanged.")
        
        # TRICK TEST 2: dict2 must also not be modified (ADDITIONAL TRICK)
        dict2_backup = dict2.copy()
        result = merge_dicts(dict1, dict2)
        self.assertEqual(dict2, dict2_backup, "Original dict2 was modified! It must remain unchanged.")
        
        # TRICK TEST 3: Ensure a NEW dictionary is returned (not one of the inputs)
        # (This test is implicit in the ones above, but can be made explicit)
        self.assertIsNot(result, dict1, "The returned dictionary should be a new object, not dict1.")
        self.assertIsNot(result, dict2, "The returned dictionary should be a new object, not dict2.")

    # Exercise 3: Week 5 Review - List Filtering
    def test_exercise3_filter_by_length(self):
        """Test filtering strings by length with preservation and non-destructive operation."""
        
        # Basic functionality - "greater than or equal to" yani >= olmalı
        self.assertEqual(filter_by_length(['hi', 'hello', 'hey', 'welcome'], 3), 
                        ['hello', 'hey', 'welcome'])  # 'hey' 3 karakter, 3>=3 True
        
        # Edge cases
        self.assertEqual(filter_by_length(['ab', 'abc'], 2), ['ab', 'abc'])  # 'ab' 2 karakter, 2>=2 True
        self.assertEqual(filter_by_length(['test'], 5), [])
        self.assertEqual(filter_by_length([], 3), [])
        
        # TRICK 1: Exact length match (boundary condition)
        self.assertEqual(filter_by_length(['cat', 'dog', 'elephant'], 3), 
                        ['cat', 'dog', 'elephant'])  # 'cat' ve 'dog' 3 karakter, 3>=3 True
        
        # TRICK 2: Original list must not be modified (non-destructive)
        original_list = ['python', 'c', 'java', 'go', 'rust']
        original_copy = original_list.copy()
        result = filter_by_length(original_list, 3)
        self.assertEqual(result, original_copy,
                        "Original list was modified. The function must be non-destructive.")
        
        # TRICK 3: Order preservation (important for list comprehensions done wrong)
        self.assertEqual(filter_by_length(['zzz', 'aaa', 'bbb', 'cccc'], 3), 
                        ['zzz', 'aaa', 'bbb', 'cccc'])  # Hepsi >= 3
        
        # TRICK 4: min_len = 0 (tests boundary condition with empty strings)
        # Empty string has length 0, and 0 >= 0 is TRUE
        # So '' SHOULD be included when using "greater than or equal to"
        self.assertEqual(filter_by_length(['', 'a', 'ab'], 0), 
                        ['', 'a', 'ab'])  # '' length=0, 0>=0 True
        
        # TRICK 5: Negative min_len (should still work)
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
        
        # Test 3: TRICK - Instance independence
        p2 = Person("Bob", 30)
        p2.name = "Robert"  # Modify one instance
        self.assertEqual(p2.get_info(), "Name: Robert, Age: 30")
        # Ensure original instance is unaffected
        self.assertEqual(p.get_info(), "Name: Alice, Age: 25")
        
        # Test 4: TRICK - Method existence and callability
        self.assertTrue(hasattr(p, "get_info"))
        self.assertTrue(callable(p.get_info))
        
        # Test 5: TRICK - Return type must be string (not print)
        info = p.get_info()
        self.assertIsInstance(info, str, "get_info() must return a string, not print.")

    def test_exercise5_circle_inheritance(self):
        """Test Circle inheritance with trick tests focusing on proper inheritance usage."""
        
        # Test 1: Circle has all expected attributes
        c = Circle("Blue", 10)
        assert c.color == "Blue"
        assert c.radius == 10
        
        # Test 2: TRICK - Exact output format required (tests override)
        assert c.get_info() == "Circle color: Blue, Radius: 10"
        
        # Test 3: TRICK - Must be a subclass (inheritance required)
        s = Shape("Red")
        assert isinstance(c, Shape)
        assert issubclass(Circle, Shape)
        
        # Test 4: TRICK - Parent and child methods must differ (override check)
        assert s.get_info() != c.get_info()
        assert s.get_info() == "Shape color: Red"
        
        # Test 5: TRICK - Instance independence (no shared class variables)
        c2 = Circle("Green", 5)
        c3 = Circle("Yellow", 7)
        c2.color = "Dark Green"
        assert c3.color == "Yellow"  # c3 should not be affected
        
        # Test 6: TRICK - New: Circle should NOT have a 'shape_id' attribute
        assert not hasattr(c, 'shape_id'), "Circle should have 'radius', not 'shape_id'"
        
        # Test 7: TRICK - New: Ensure Circle.__init__ doesn't break Shape.__init__
        # Shape should still work independently
        s2 = Shape("Black")
        assert s2.get_info() == "Shape color: Black"


    # Test code for EXERCISE 6
    def test_exercise6_method_overriding(self):
        """Test method overriding with focus on proper inheritance and exact output."""
        
        # TRICK 1: Device.get_sound() should not return a meaningful string
        device = Device()
        device_sound_result = device.get_sound()
        assert device_sound_result != "Ring!", \
            "Device.get_sound() should not return 'Ring!'"
        
        # TRICK 2: Must use inheritance
        smartphone = Smartphone()
        assert isinstance(smartphone, Device), "Smartphone must inherit from Device"
        
        # TRICK 3: Exact string "Ring!" required
        assert smartphone.get_sound() == "Ring!", \
            'Smartphone.get_sound() must return exactly "Ring!"'
        
        # TRICK 4: Smartphone.get_sound() must be different from Device.get_sound()
        assert device.get_sound() != smartphone.get_sound(), \
            "Smartphone.get_sound() should not return the same as Device.get_sound()"
        
        # TRICK 5: Ensure get_sound() returns a string
        result = smartphone.get_sound()
        assert isinstance(result, str), \
            "Smartphone.get_sound() must return a string"
        
        # TRICK 6: Multiple instances work independently
        smartphone2 = Smartphone()
        smartphone3 = Smartphone()
        smartphone2.get_sound()
        assert smartphone3.get_sound() == "Ring!"

    # ==========================================
    # SECTION B TESTS: MEDIUM - OOP CONCEPTS (18 points)
    # ==========================================

    # Exercise 7: Classes and Methods
    def test_exercise7_product_class(self):
        """Test Product class with trick tests focusing on state management."""
        
        # ÖNEMLİ: Önce tüm Product tanımlarını temizle
        for key in list(globals().keys()):
            if key == 'Product':
                del globals()[key]
        
        # Product sınıfının tanımlı olup olmadığını kontrol et
        if 'Product' not in globals():
            # Test dosyasından Product sınıfını import etmeye çalış
            try:
                # Eğer öğrenci kodu ayrı bir dosyada ise
                from lab6_exercises import Product
                globals()['Product'] = Product
            except ImportError:
                # Eğer doğrudan bu dosyada tanımlanmışsa
                self.fail("Product class not defined. Please create Product class with EXACT name 'Product'.")
        
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
        
        # Ensure apply_discount method exists
        self.assertTrue(hasattr(p1, 'apply_discount'), 
                       "Product class must have apply_discount method")
        self.assertTrue(callable(p1.apply_discount),
                       "apply_discount must be a method")
        
        
    # Test code for EXERCISE 8
    def test_exercise8_shoe_inheritance():
        """Test Shoe inheritance with focus on proper override and independent implementation."""
        
        # Test 1: Shoe has all expected attributes including inherited ones
        shoe = Shoe("Running Shoes", 80.0, 5, "Nike", 42)
        assert shoe.name == "Running Shoes"
        assert shoe.price == 80.0
        assert shoe.quantity == 5
        assert shoe.brand == "Nike"
        assert shoe.size == 42
        
        # Test 2: TRICK - Must inherit from ClothingItem (type check)
        assert isinstance(shoe, ClothingItem)
        
        # Test 3: TRICK - calculate_price() returns a different value than base ClothingItem
        basic_item = ClothingItem("Basic", 80.0, 5)
        shoe_price = shoe.calculate_price()
        item_price = basic_item.calculate_price()
        assert shoe_price != item_price, \
            "Shoe.calculate_price() must return different value than ClothingItem"
        
        # Test 4: TRICK - The difference should be consistent and significant
        difference = abs(shoe_price - item_price)
        assert difference > 1.0, \
            "Shoe price should be substantially different from base clothing item price"
        
        # Test 6: TRICK - Multiple shoes are independent
        s1 = Shoe("Sneakers", 60.0, 3, "Adidas", 40)
        s2 = Shoe("Boots", 120.0, 2, "Timberland", 41)
        s1.quantity = 4
        assert s2.quantity == 2, "Modifying one shoe should not affect another"
        
        # Test 7: TRICK - The calculation should work with edge cases
        free_shoe = Shoe("Free", 0.0, 8, "Generic", 39)
        assert isinstance(free_shoe.calculate_price(), (int, float)), \
            "calculate_price() should return a number even with zero price"
        
        # Test 8: TRICK - The override should handle different numeric inputs
        expensive_shoe = Shoe("Designer", 500.0, 2, "Gucci", 43)
        expensive_price = expensive_shoe.calculate_price()
        # Check that the price is different from simple multiplication
        assert expensive_price != 1000.0, \
            "With the modification, total should be different from price×quantity"
        
        print("All tests passed for Exercise 8!")


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
        
        # Test 4: TRICK - Private/mangled attribute should exist
        # Tests that student used name mangling for privacy
        self.assertTrue(hasattr(account, '_BankAccount__balance'),
                       "Balance should be stored with name mangling for privacy")
        
        # Test 5: TRICK - No simple public balance attribute
        # Catches students who use self.balance instead of private attribute
        self.assertFalse(hasattr(account, 'balance'),
                        "Should not have a simple public 'balance' attribute")
        
        # Test 6: TRICK - Insufficient funds protection
        initial_balance = account.get_balance()
        # Try to withdraw more than available
        withdrawal_result = account.withdraw(initial_balance + 100)
        self.assertEqual(account.get_balance(), initial_balance,
                        "Balance should not change after attempted over-withdrawal")
        
        # Test 7: TRICK - Exact balance withdrawal (edge case)
        account2 = BankAccount(500)
        account2.withdraw(500)
        self.assertEqual(account2.get_balance(), 0)
        
        # Test 8: TRICK - Negative or zero amounts (should be handled gracefully)
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
        
        # Test 9: TRICK - Instance independence
        acc1 = BankAccount(100)
        acc2 = BankAccount(200)
        acc1.deposit(50)
        self.assertEqual(acc1.get_balance(), 150)
        self.assertEqual(acc2.get_balance(), 200)
        
        # Test 10: TRICK - Method return values
        # get_balance() should return a numeric value
        balance = account.get_balance()
        self.assertIsInstance(balance, (int, float))
        
        # Test 11: NEW TRICK - Deposit with zero or negative (optional handling)
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
        dog = Dog()  
        cat = Cat()  
        
        # Test 2: TRICK - Inheritance must be used
        self.assertIsInstance(dog, AnimalBase)
        self.assertIsInstance(cat, AnimalBase)
        
        # Test 3: TRICK - Dog and Cat must return different strings
        dog_sound = dog.speak()
        cat_sound = cat.speak()
        self.assertNotEqual(dog_sound, cat_sound,
                          "Dog and Cat must produce different sounds")
        
        # Test 4: TRICK - Both must return strings (not print)
        self.assertIsInstance(dog_sound, str)
        self.assertIsInstance(cat_sound, str)
    
        # Test 5: TRICK - Sounds should not be empty or None
        self.assertTrue(len(dog_sound) > 0, "Dog sound should not be empty")
        self.assertTrue(len(cat_sound) > 0, "Cat sound should not be empty")
        
        # Test 6: TRICK - animal_concert function exists and works
        animals = [dog, cat, dog]  # 2 dogs, 1 cat
        sounds = animal_concert(animals)
        
        self.assertEqual(len(sounds), 3,
                        "Should return one sound per animal")
        
        # Test 7: TRICK - Order preservation in animal_concert
        self.assertEqual(sounds[0], dog_sound)
        self.assertEqual(sounds[1], cat_sound)
        self.assertEqual(sounds[2], dog_sound)
        
        # Test 8: TRICK - animal_concert works with empty list
        empty_result = animal_concert([])
        self.assertEqual(empty_result, [])
        
        # Test 9: TRICK - animal_concert works with homogeneous list
        three_dogs = [Dog(), Dog(), Dog()] 
        dog_sounds = animal_concert(three_dogs)
        self.assertEqual(len(dog_sounds), 3)
        # All should be the same sound
        self.assertEqual(dog_sounds[0], dog_sounds[1])
        self.assertEqual(dog_sounds[1], dog_sounds[2])
        
        # Test 10: NEW TRICK - animal_concert should not modify input list
        original_animals = [Dog(), Cat()]  
        animals_copy = original_animals.copy()
        animal_concert(original_animals)
        self.assertEqual(original_animals, animals_copy,
                        "animal_concert should not modify the input list")
        
        # Test 11: NEW TRICK - AnimalBase.speak() should not return same as Dog or Cat
        base_animal = AnimalBase()
        base_sound = base_animal.speak()
        # Base sound should be different from both Dog and Cat
        self.assertNotEqual(base_sound, dog_sound,
                          "AnimalBase sound should differ from Dog")
        self.assertNotEqual(base_sound, cat_sound,
                          "AnimalBase sound should differ from Cat")

    # Exercise 11: Class Variables
    def test_exercise11_class_variables(self):
        """Test Employee class with class variable tracking."""
        
        # Önce tüm Employee tanımlarını temizle
        for key in list(globals().keys()):
            if key == 'Employee':
                del globals()[key]
        
        # Employee sınıfının tanımlı olup olmadığını kontrol et
        if 'Employee' not in globals():
            self.fail("Employee class not defined. Please create Employee class.")
        
        # Reset count - ÖNEMLİ: Öğrencinin sınıfını kullan
        Employee._total_employees = 0
        
        # Test 1: Initial count is 0
        self.assertEqual(Employee.get_total_employees(), 0)
        
        # Test 2: Creating instances increments count
        emp1 = Employee("Alice", 50000)
        self.assertEqual(Employee.get_total_employees(), 1)
        
        emp2 = Employee("Bob", 60000)
        self.assertEqual(Employee.get_total_employees(), 2)
        
        # Test 3: Instance attributes are correct
        self.assertEqual(emp1.name, "Alice")
        self.assertEqual(emp1.salary, 50000)
        self.assertEqual(emp2.name, "Bob")
        self.assertEqual(emp2.salary, 60000)
        
        # Test 4: Class method works from instance too
        self.assertEqual(emp1.get_total_employees(), 2)
        
        # Test 5: Count only increases
        emp3 = Employee("Charlie", 70000)
        emp4 = Employee("Diana", 80000)
        self.assertEqual(Employee.get_total_employees(), 4)
        
        # Test 6: Check if _total_employees is a class variable, not instance
        self.assertFalse(hasattr(emp1, '_total_employees'), 
                        "_total_employees should be a class variable, not instance attribute")
        self.assertTrue(hasattr(Employee, '_total_employees'),
                       "Employee class should have _total_employees class variable")
        
        # Test 7: Check method types
        import types
        self.assertIsInstance(Employee.get_total_employees, types.MethodType,
                            "get_total_employees should be a class method")
        
    # Exercise 12: Special Methods (__str__ and __repr__)
    def test_exercise12_string_representation(self):
        """Test __str__ and __repr__ methods with focus on proper implementation."""
        
        # Test 1: Point can be created with coordinates
        point = Point(3, 4)
        self.assertEqual(point.x, 3)
        self.assertEqual(point.y, 4)
        
        # Test 2: TRICK - __str__ method exists (name check)
        self.assertTrue(hasattr(Point, '__str__'),
                       "Point class must have __str__ method")
        self.assertTrue(callable(point.__str__))
        
        # Test 3: TRICK - __repr__ method exists (name check)
        self.assertTrue(hasattr(Point, '__repr__'),
                       "Point class must have __repr__ method")
        self.assertTrue(callable(point.__repr__))
        
        # Test 4: TRICK - Both methods return strings
        str_result = str(point)
        repr_result = repr(point)
        
        self.assertIsInstance(str_result, str,
                            "__str__ must return a string")
        self.assertIsInstance(repr_result, str,
                            "__repr__ must return a string")
        
        # Test 5: TRICK - __str__ and __repr__ return DIFFERENT strings
        self.assertNotEqual(str_result, repr_result,
                          "__str__ and __repr__ should return different formats")
        
        # Test 6: TRICK - __str__ should contain coordinate information
        # (Without specifying exact format)
        self.assertIn("3", str_result,
                     "__str__ should include x coordinate")
        self.assertIn("4", str_result,
                     "__str__ should include y coordinate")
        
        # Test 7: TRICK - __repr__ should contain class name and coordinates
        self.assertIn("Point", repr_result,
                     "__repr__ should include class name")
        self.assertIn("3", repr_result,
                     "__repr__ should include x coordinate")
        self.assertIn("4", repr_result,
                     "__repr__ should include y coordinate")
        
        # Test 8: TRICK - eval(repr(point)) should create a similar object
        # (Tests that __repr__ is evaluable)
        try:
            new_point = eval(repr_result)
            self.assertEqual(new_point.x, 3)
            self.assertEqual(new_point.y, 4)
            self.assertIsInstance(new_point, Point)
        except:
            self.fail("repr() should return evaluable string that recreates object")
        
        # Test 9: TRICK - Different point coordinates
        p2 = Point(10, -5)
        str2 = str(p2)
        repr2 = repr(p2)
        
        self.assertIn("10", str2)
        self.assertIn("-5", str2)
        self.assertIn("10", repr2)
        self.assertIn("-5", repr2)
        
        # Test 10: TRICK - __str__ for negative/zero coordinates
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
        
        # Test 3: Private name-mangled attributes exist
        # (Catches students who use public attributes like self.width)
        self.assertTrue(hasattr(rect, '_Rectangle__width'),
                       "Must use private __width attribute (name-mangled)")
        self.assertTrue(hasattr(rect, '_Rectangle__height'),
                       "Must use private __height attribute (name-mangled)")
        
        # Test 4: No simple public attributes
        # (Catches students who use self.width instead of self.__width)
        self.assertFalse(hasattr(rect, 'width'),
                        "Should NOT have public 'width' attribute")
        self.assertFalse(hasattr(rect, 'height'),
                        "Should NOT have public 'height' attribute")
        
        # Test 5: TRICK - Validation prevents invalid dimensions
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
        
        # Test 6: TRICK - Only update when BOTH are valid
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
        
        # Test 7: TRICK - Instance independence
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r1_area_before = r1.get_area()
        r2_area_before = r2.get_area()
        
        r1.set_dimensions(5, 6)
        
        self.assertNotEqual(r1.get_area(), r1_area_before,
                          "r1 should change after set_dimensions")
        self.assertEqual(r2.get_area(), r2_area_before,
                       "r2 should NOT change when r1 is modified")
        
        # Test 8: NEW TRICK - get_area and get_perimeter are consistent
        # If w=10, h=20, area=200, perimeter should be 60 (2*(10+20))
        # But we won't specify the formula - just test consistency
        rect4 = Rectangle(7, 11)
        area4 = rect4.get_area()
        perimeter4 = rect4.get_perimeter()
        
        # Quick sanity: if dimensions are positive, perimeter > any single side
        # This catches completely wrong formulas
        self.assertGreater(perimeter4, 7)
        self.assertGreater(perimeter4, 11)
        
        # Test 9: NEW TRICK - set_dimensions with same values should work
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
        
        # Test 3: TRICK - get_instance_count() can be called from class
        # (Tests it's a class method or at least works at class level)
        class_count = Counter.get_instance_count()
        self.assertEqual(class_count, count_after_second)
        
        # Test 4: TRICK - get_instance_count() can also be called from instance
        # (Would fail if implemented as regular instance method without @classmethod)
        instance_count = counter1.get_instance_count()
        self.assertEqual(instance_count, class_count,
                        "Instance call should return same as class call")
        
        # Test 5: TRICK - is_even() method works correctly
        self.assertTrue(Counter.is_even(4))
        self.assertFalse(Counter.is_even(5))
        self.assertTrue(Counter.is_even(0))
        self.assertTrue(Counter.is_even(-2))
        self.assertFalse(Counter.is_even(-1))
        
        # Test 6: TRICK - is_even() can be called from class
        # (Tests it's accessible at class level)
        self.assertIsInstance(Counter.is_even(10), bool)
        
        # Test 7: TRICK - is_even() can also be called from instance
        # (Tests it's not an instance method requiring self)
        self.assertIsInstance(counter1.is_even(10), bool)
        
        # Test 8: TRICK - is_even() doesn't depend on instance/class state
        # Create new counter, is_even should work the same
        counter3 = Counter()
        # Should get same result regardless of which instance or class
        self.assertEqual(Counter.is_even(8), counter1.is_even(8))
        self.assertEqual(Counter.is_even(8), counter2.is_even(8))
        self.assertEqual(Counter.is_even(8), counter3.is_even(8))
        
        # Test 9: TRICK - Class variable is not an instance attribute
        # (Students might incorrectly use instance variable)
        self.assertFalse(hasattr(counter1, 'instance_count'),
                        "Counting should be at class level, not instance")
        
        # Test 10: NEW TRICK - Large numbers work with is_even()
        self.assertTrue(Counter.is_even(1000000))
        self.assertFalse(Counter.is_even(1000001))
        
        # Test 11: NEW TRICK - Even check works with different numeric types
        # (float with integer value)
        self.assertTrue(Counter.is_even(6.0))
        # (But odd float should still be False)
        self.assertFalse(Counter.is_even(7.0))

    # Exercise 15: Inheritance and Method Chaining
    def test_exercise15_inheritance_method_chaining(self):
        """Test inheritance hierarchy with method overriding and super() usage."""
        
        # Öğrencinin sınıflarının tanımlı olup olmadığını kontrol et
        if 'Vehicle' not in globals():
            self.fail("Vehicle class not defined. Please create Vehicle class.")
        
        if 'Car' not in globals():
            self.fail("Car class not defined. Please create Car class that inherits from Vehicle.")
        
        # Test 1: Both classes can be instantiated
        vehicle = Vehicle("Blue", 150)
        car = Car("Red", 200, 4)
        
        # Test 2: Car inherits from Vehicle
        self.assertIsInstance(car, Vehicle)
        
        # Test 3: Vehicle has expected attributes
        self.assertEqual(vehicle.color, "Blue")
        self.assertEqual(vehicle.max_speed, 150)
        
        # Test 4: Car has all Vehicle attributes plus its own
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.max_speed, 200)
        self.assertEqual(car.num_doors, 4)
        
        # Test 5: describe() methods exist and return strings
        vehicle_desc = vehicle.describe()
        car_desc = car.describe()
        
        self.assertIsInstance(vehicle_desc, str)
        self.assertIsInstance(car_desc, str)
        
        # Test 6: Car.describe() includes Vehicle information
        self.assertIn("Red", car_desc)
        self.assertIn("200", car_desc)
        
        # Test 7: Car.describe() is different from Vehicle.describe()
        self.assertNotEqual(vehicle_desc, car_desc,
                          "Car should override describe() method")
        
        # Test 8: Car.describe() includes car-specific information
        self.assertIn("4", car_desc)
        self.assertIn("doors", car_desc.lower())
        
        # Test 9: Multiple cars work independently
        car2 = Car("White", 180, 2)
        car2_desc = car2.describe()
        self.assertIn("White", car2_desc)
        self.assertIn("180", car2_desc)
        self.assertIn("2", car2_desc)
        self.assertNotEqual(car_desc, car2_desc)
        
        # Test 10: Vehicle.describe() for different vehicle
        vehicle2 = Vehicle("Green", 120)
        vehicle2_desc = vehicle2.describe()
        self.assertIn("Green", vehicle2_desc)
        self.assertIn("120", vehicle2_desc)
        
        # Test 11: Method signature compatibility
        import inspect
        vehicle_sig = inspect.signature(vehicle.describe)
        car_sig = inspect.signature(car.describe)
        self.assertEqual(len(vehicle_sig.parameters), len(car_sig.parameters),
                        "describe() should have same parameter count")
        
        # Test 12: Exact format matching (CRITICAL - matches problem statement)
        expected_vehicle_desc = "Vehicle: color=Blue, max_speed=150km/h"
        expected_car_desc = "Car: color=Red, max_speed=200km/h, doors=4"
        
        self.assertEqual(vehicle.describe(), expected_vehicle_desc,
                        f"Expected: '{expected_vehicle_desc}', Got: '{vehicle.describe()}'")
        self.assertEqual(car.describe(), expected_car_desc,
                        f"Expected: '{expected_car_desc}', Got: '{car.describe()}'")
        
        # Test 13: Check if super() was used properly
        # Car'ın __init__'inde Vehicle.__init__'ini çağırması gerekiyor
        try:
            # Try to create a Car without proper initialization
            test_car = Car("Test", 100, 2)
            # If we get here, it should have color and max_speed
            self.assertTrue(hasattr(test_car, 'color'), "Car should have color attribute")
            self.assertTrue(hasattr(test_car, 'max_speed'), "Car should have max_speed attribute")
        except Exception as e:
            self.fail(f"Failed to create Car instance: {e}")
        
        # Test 14: Inheritance check
        self.assertTrue(issubclass(Car, Vehicle), "Car must inherit from Vehicle")
        
        # Test 15: Override check
        self.assertNotEqual(Vehicle.describe, Car.describe,
                          "Car should override the describe method")

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
        
        # Test 3: TRICK - Vehicle HAS a component (composition)
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
        
        # Test 6: TRICK - Component power matches initialization value
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
        
        # Test 8: TRICK - Vehicle method delegates to component method
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
        
        # Test 9: TRICK - Vehicle result includes vehicle-specific info
        self.assertIn("Toyota", vehicle_result)
        
        # Test 10: TRICK - Vehicle result includes component power info
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
        
        # Test 12: NEW TRICK - Components are independent (deep copy)
        # Modifying one vehicle's component shouldn't affect another
        original_power = getattr(component_obj2, power_attr2)
        setattr(component_obj, power_attr, 999)  # Modify first vehicle's component
        
        self.assertEqual(getattr(component_obj2, power_attr2), original_power,
                        "Components should be independent instances")
        
def calculate_score():
    """Calculate and display score"""
    import re
    import importlib
    import sys
    
    if 'lab6_exercises' in sys.modules:
        importlib.reload(sys.modules['lab6_exercises'])
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLab6)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(getattr(result, 'skipped', []))
    passed = total_tests - failures - errors - skipped
    
    print("\n" + "=" * 50)
    print(f"LAB 6 RESULTS: {passed}/{total_tests} tests passed")
    print(f"Failed tests: {failures}")
    print(f"Error tests: {errors}")
    print(f"Skipped tests: {skipped}")

    # Section counters
    section_a_passed = 0
    section_b_passed = 0
    section_c_passed = 0
    
    # Extract list of failed tests
    failed_test_names = {fail[0]._testMethodName for fail in result.failures}
    failed_test_names |= {err[0]._testMethodName for err in result.errors}
    
    # Find all test methods
    test_methods = [m for m in dir(TestLab6) if m.startswith("test_exercise")]

    for method_name in test_methods:
        if method_name not in failed_test_names:
            match = re.match(r"test_exercise(\d+)", method_name)
            if match:
                exercise_num = int(match.group(1))

                # Chapter matching
                if 1 <= exercise_num <= 6:
                    section_a_passed += 1
                elif 7 <= exercise_num <= 12:
                    section_b_passed += 1
                elif 13 <= exercise_num <= 16:
                    section_c_passed += 1
            else:
                # Let's try alternative regex
                match2 = re.match(r"test_exercise(\d+)_", method_name)
                if match2:
                    exercise_num = int(match2.group(1))
                    if 1 <= exercise_num <= 6:
                        section_a_passed += 1
                    elif 7 <= exercise_num <= 12:
                        section_b_passed += 1
                    elif 13 <= exercise_num <= 16:
                        section_c_passed += 1

    # Score calculation
    section_a_score = section_a_passed * 2
    section_b_score = section_b_passed * 3
    section_c_score = section_c_passed * 5
    total_score = section_a_score + section_b_score + section_c_score

    print("\nSECTION SCORES:")
    print(f"Section A (Easy): {section_a_passed}/6 passed = {section_a_score}/12 points")
    print(f"Section B (Medium): {section_b_passed}/6 passed = {section_b_score}/18 points")
    print(f"Section C (Hard): {section_c_passed}/4 passed = {section_c_score}/20 points")
    
    print(f"\nDETAILED RESULTS:")
    # Show which tests passed/failed
    for i in range(1, 17):
        test_name = f"test_exercise{i}_"
        found = False
        for method in test_methods:
            if method.startswith(test_name):
                found = True
                status = "✓ PASSED" if method not in failed_test_names else "✗ FAILED"
                print(f"  Exercise {i}: {status}")
                break
        if not found:
            print(f"  Exercise {i}: NOT FOUND")
    
    print(f"\nTOTAL SCORE: {total_score}/44 points")
    print(f"PERCENTAGE: {(total_score/44)*100:.1f}%")
    print("=" * 50)
    
    return total_score

if __name__ == "__main__":
    calculate_score()