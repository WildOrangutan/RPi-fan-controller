import unittest
from time import sleep
from src.looper import Looper

class TestLooper(unittest.TestCase):

    def setUp(self):
        self.workInvokeCount = 0
        self.workDur = 0.05

    def test_too_much_work(self):
        period = self.workDur / 2
        looper = Looper(period=period, work=self._work)

        looper.start()
        sleep(self.workDur*2)
        
        self.assertTrue(looper.hasFailed())

    def test_not_much_work(self):
        period = self.workDur * 2
        looper = Looper(period=period, work=self._work)

        looper.start()
        sleep(period)
        looper.stop()

        # No exception raised

    def test_stop_start(self):
        period = self.workDur * 3/4
        looper = Looper(period=period, work=self._work)

        looper.start()
        looper.stop()
        sleep(self.workDur)

        # Will throw exception, unless stopped

    def test_looping(self):
        period = self.workDur * 2
        looper = Looper(period=period, work=self._work)

        looper.start()
        sleep(period * 3)
        looper.stop()

        self.assertTrue(self.workInvokeCount > 1)
    
    def _work(self):
        self.workInvokeCount +=1
        sleep(self.workDur)
    