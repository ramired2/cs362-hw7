import unittest
import leapyear

class testCaseFizzbuzz(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leapyear.check(), "Leap Year")


if __name__ == "__main__":
    unittest.main()