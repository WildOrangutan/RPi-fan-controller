import unittest
from src.filter import Filter

class TestFilter(unittest.TestCase):

    def setUp(self):
        self.T = 0.001 # Filter update period
        self.Tf = 3 # Filter time constant
        self.filter = Filter(self.T, self.Tf)

    def test_filter_response(self):
        input = 100
        # How many calls it's needed, for 1 filter time constant (Tao) to pass
        callsPerTao = int(self.Tf/self.T)
        # Values after 1, 2, 3 Tao
        expectedOutputs = [63, 86, 95]
        expectedError = 1

        for i in range(3):
            actual = self._loopAndReturn(callsPerTao, input)
            expected = expectedOutputs[i]
            self._assert(actual, expected, expectedError)

    def _loopAndReturn(self, numTimes, value):
        for _ in range(numTimes):
            output = self.filter.calculateOutput(value)
        return output

    def _assert(self, actual, expected, maxError):
        expectedMin = expected - maxError
        expectedMax = expected + maxError
        assert expectedMin <= actual <= expectedMax, \
                f"expected {expectedMin}-{expectedMax}, actual {actual}"

if __name__ == '__main__':
    unittest.main()