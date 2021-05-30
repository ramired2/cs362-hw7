import unittest
import leapyear

class testCaseFizzbuzz(unittest.TestCase):
    def test_leapDivisible4(self):
        self.assertEqual(leapyear.check(), "Leap Year")

    def test_leapyear(self):
        self.assertEqual(leapyear.sneakyLeap(), "Leap Year")


if __name__ == "__main__":
    unittest.main()