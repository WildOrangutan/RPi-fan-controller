import unittest
import src.check as check

class TestCheck(unittest.TestCase):

    def test_range(self):
        # In range
        self._checkRange(1)
        self._checkRange(1, min=1, max=1)
        self._checkRange(1, min=0, max=2)
        self._checkRange(-1, min=-1, max=-1)
        self._checkRange(-1, min=-2, max=0)
        # Out of range
        with self.assertRaises(ValueError):
            self._checkRange(0, min=1)
        with self.assertRaises(ValueError):
            self._checkRange(-2, min=-1)
        with self.assertRaises(ValueError):
            self._checkRange(1, max=0)
        with self.assertRaises(ValueError):
            self._checkRange(-1, max=-2)
        # Invalid min max
        with self.assertRaises(ValueError):
            self._checkRange(0, min=2, max=1)
        with self.assertRaises(ValueError):
            self._checkRange(0, -2, -3)

    def _checkRange(self, value, min=None, max=None):
        check.range("Fart", value, min, max)

    def test_none(self):
        self._checkNotNone(1)
        with self.assertRaises(ValueError):
            self._checkNotNone(None)
    
    def _checkNotNone(self, value):
        check.notNone("", value)
