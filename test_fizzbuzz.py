import unittest
import fizzbuzz

class testCaseFizzbuzz(unittest.TestCase):
    def test_Divisible3and5(self):
        self.assertEqual(fizzbuzz.check(15), "FizzBuzz")
    
    def test_Divisible3Only(self):
        self.assertEqual(fizzbuzz.check3(33), "Fizz")


if __name__ == "__main__":
    unittest.main()