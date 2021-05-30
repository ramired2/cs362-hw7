import unittest
import leapyear

class testCaseFizzbuzz(unittest.TestCase):
    def test_leapDivisible4(self):
        self.assertEqual(leapyear.check(2004), "Leap Year")

    def test_leapyear(self):
        self.assertEqual(leapyear.sneakyLeap(2004), True)


if __name__ == "__main__":
    unittest.main()