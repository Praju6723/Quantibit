import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
class TestFactorial(unittest.TestCase):

    def test_factorial_5(self):
        result = factorial(5)
        self.assertEqual(result, 120)
        print("Test Passed for input 5")

    def test_factorial_0(self):
        result = factorial(0)
        self.assertEqual(result, 1)
        print("Test Passed for input 0")

    def test_factorial_1(self):
        result = factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_3(self):
        result = factorial(3)
        self.assertEqual(result, 6)

    def test_factorial_4(self):
        result = factorial(4)
        self.assertEqual(result, 24)

if __name__ == '__main__':

    unittest.main(argv=[''], verbosity=0, exit=False)
