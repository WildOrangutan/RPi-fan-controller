from dataclasses import dataclass
import src.check as check

@dataclass
class ProfilePoint:
    temp: float 
    pwm: float

    def __post_init__(self):
        self.__validateTemp()
        self.__validatePwm()

    def __validateTemp(self):
        check.range("Temp", self.temp, 0, 100)

    def __validatePwm(self):
        check.range("PWM", self.pwm, 0, 100)