import RPi.GPIO as GPIO
import src.check as check

class FanDriver:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        PIN = 18
        GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)
        PWM_FREQ_HZ = 50
        self.output = GPIO.PWM(PIN, PWM_FREQ_HZ)
    
    def __del__(self):
        self.output.stop()
        GPIO.cleanup()
    
    def setSpeed(self, speedPercent):
        check.range("speedPercent", speedPercent, min=0, max=100)
        self.output.ChangeDutyCycle(speedPercent)
