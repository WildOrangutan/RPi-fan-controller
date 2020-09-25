import unittest
import src.check as check

class TestCheck(unittest.TestCase):

    def test_range(self):
        # In range
        self.__checkRange(1)
        self.__checkRange(1, min=1, max=1)
        self.__checkRange(1, min=0, max=2)
        self.__checkRange(-1, min=-1, max=-1)
        self.__checkRange(-1, min=-2, max=0)
        # Out of range
        with self.assertRaises(ValueError):
            self.__checkRange(0, min=1)
        with self.assertRaises(ValueError):
            self.__checkRange(-2, min=-1)
        with self.assertRaises(ValueError):
            self.__checkRange(1, max=0)
        with self.assertRaises(ValueError):
            self.__checkRange(-1, max=-2)
        # Invalid min max
        with self.assertRaises(ValueError):
            self.__checkRange(0, min=2, max=1)
        with self.assertRaises(ValueError):
            self.__checkRange(0, -2, -3)

    def __checkRange(self, value, min=None, max=None):
        check.range("Fart", value, min, max)

    def test_none(self):
        self.__checkNotNone(1)
        with self.assertRaises(ValueError):
            self.__checkNotNone(None)
    
    def __checkNotNone(self, value):
        check.notNone("", value)
