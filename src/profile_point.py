from dataclasses import dataclass

@dataclass
class ProfilePoint:
    temp: float 
    pwm: float

    def __post_init__(self):
        self.__validateTemp()
        self.__validatePwm()

    def __validateTemp(self):
        self.__validateRange("Temp", self.temp, 0, 100)

    def __validatePwm(self):
        self.__validateRange("PWM", self.pwm, 0, 100)
    
    def __validateRange(self, valueName, value, min, max):
        if value<min or value>max:
            raise ValueError(f"{valueName} should be {min} and {max}")
