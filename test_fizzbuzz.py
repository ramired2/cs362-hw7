import unittest
import fizzbuzz

class testCaseFizzbuzz(unittest.TestCase):
    def test_Divisible3and5(self):
        self.assertEqual(fizzbuzz.check(15), "FizzBuzz")



if __name__ == "__main__":
    unittest.main()