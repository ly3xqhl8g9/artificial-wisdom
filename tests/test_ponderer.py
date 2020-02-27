import unittest
import pprint
import time

from artificial_wisdom.ponderer import Ponderer



class TestPonderer(unittest.TestCase):
   def test_ponderer(self):
        def adder(one: int, two: int):
            return one + two

        ponderer = Ponderer(adder)

        # ponderer.ponder(784**2, 1)
        # print(ponderer.running_times)

        assert ponderer.ponder(5, 7) == 12


if __name__ == '__main__':
    unittest.main()
