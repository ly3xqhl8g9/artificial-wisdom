import unittest
import pprint
import time

from artificial_wisdom.wonder import Wonder



class TestWonder(unittest.TestCase):
   def test_wonder(self):
        @Wonder
        def adder(one: int, two: int):
            return one + two

        # adder(5, 7)
        # adder(5, 7)
        # print(adder.running_times)

        assert adder(5, 7) == 12


if __name__ == '__main__':
    unittest.main()
