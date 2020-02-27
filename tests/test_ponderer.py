import unittest
import pprint

from artificial_wisdom.ponderer import Ponderer



class TestPonderer(unittest.TestCase):
   def test_ponderer(self):
        ponderer = Ponderer()

        assert 5 + 7 == 12


if __name__ == '__main__':
    unittest.main()
