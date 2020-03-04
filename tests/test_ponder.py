import unittest
import pprint
import time

from artificial_wisdom.ponder import Ponder



class TestPonder(unittest.TestCase):
   def test_ponder(self):
        @Ponder
        def adder(one: int, two: int):
            return one + two

        # adder(5, 7)
        # adder(7, 5)
        # print(adder.running_times)

        assert adder(5, 7) == 12


if __name__ == '__main__':
    unittest.main()
