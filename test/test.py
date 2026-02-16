import unittest
from main import *


class AddTest(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculate()

    def test_args(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(self.calc.add(a=10, b=2), 12)

    def test_mixed(self):
        self.assertEqual(self.calc.add(1, a=2), 3)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(self.calc.add(0, -5, y, a=x), 5)

    def test_wrong_datatype(self):
        self.assertEqual(self.calc.add('5', "qwerty", 10), 15)


if __name__ == "__main__":
    unittest.main()
