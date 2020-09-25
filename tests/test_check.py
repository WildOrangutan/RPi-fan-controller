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
        self._checkRangeErr(0, min=1)
        self._checkRangeErr(-2, min=-1)
        self._checkRangeErr(1, max=0)
        self._checkRangeErr(-1, max=-2)
        # Invalid min max
        self._checkRangeErr(0, min=2, max=1)
        self._checkRangeErr(0, min=-2, max=-3)
    
    def _checkRangeErr(self, value, min=None, max=None):
        with self.assertRaises(ValueError):
            self._checkRange(0, min=2, max=1)

    def _checkRange(self, value, min=None, max=None):
        check.range("Fart", value, min, max)

    def test_none(self):
        self._checkNotNone(1)
        with self.assertRaises(ValueError):
            self._checkNotNone(None)
    
    def _checkNotNone(self, value):
        check.notNone("", value)
