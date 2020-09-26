from typing import Callable
from time import time, sleep
from queue import Queue
from threading import Thread, Event
import src.check as check

class Looper:

    def __init__(self, period:float, work:Callable):
        '''
        period - time period in seconds, how often {work} is called
        work - function, that will get called periodically
        '''
        check.range("period", period, min=0.001)
        self._period = period
        check.notNone("work", work)
        self._work = work
        self._lastWorkDuration = 0
        self._running = Event()
        self._failed = Event()
        self._stop = Event()
    
    def start(self):
        self.thread = Thread(target=self._loop)
        self.thread.start()
        # Block calling thread, until worker thread starts, so there are no timing related
        # problems, when public methods of this class are called.
        self._running.wait()

    def _loop(self):
        self._running.set()
        try:
            while not self._stop.is_set():
                self._doWork()
                self._checkWorkedTooLong()
                self._sleepTillNextPeriod()
        except _TooMuchWorkException:
            self._stop.set()
            self._failed.set()
        finally:
            self._running.clear()
    
    def _doWork(self):
        start = time()
        self._work()
        end = time()
        self._lastWorkDuration = end - start
    
    def _checkWorkedTooLong(self):
        if self._lastWorkDuration > self._period: 
            raise _TooMuchWorkException()
    
    def _sleepTillNextPeriod(self):
        sleepDuration = self._period - self._lastWorkDuration
        sleep(sleepDuration)
    
    def __del__(self):
        self.stop()
    
    def stop(self):
        self._stop.set()
        self.thread.join()
        self._stop.clear()

    def hasFailed(self):
        return self._failed.is_set()

class _TooMuchWorkException(Exception):
    '''
    Raised when looper's work takes too long to exectute, and looper can't keep up
    '''