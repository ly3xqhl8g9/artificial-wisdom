import unittest
import pprint

from artificial_wisdom.wonderer import Wonderer



class TestWonderer(unittest.TestCase):
   def test_wonderer(self):
        wonderer = Wonderer()

        assert 5 + 7 == 12


if __name__ == '__main__':
    unittest.main()
