"""
This is simple low-pass filter of 1st order. Transfer function in s-domain is:

               1
    G(s) = ----------
           (1 + Tf*s)

    Tf - filter time constant

Discrete transformation of that functions, by approximating "s" with
2*(z-1) / T*(z+1) is:

              T                       T - T*Tf
    y(k) = -------- (x(k) + x(k-1)) - -------- y(k-1)
           T + 2*Tf                   T + 2*Tf

    y(k)   - current output value
    x(k)   - current input value
    x(k-1) - previous input value
    T      - sample time period

Or in short:
            A                     B
    y(k) = --- (x(k) + x(k-1)) - --- y(k-1)  =  p * (x(k) + x(k-1)) - o * y(k-1)
            C                     C
"""

class Filter:

    def __init__(self, T, Tf):
        self.T = T
        self.Tf = Tf
        self.__calcConstants()
        self.__initStates()

    def __calcConstants(self):
        T = self.T
        Tf = self.Tf

        A = T
        B = T - 2*Tf
        C = T + 2*Tf

        self.p = A / C
        self.o = B / C

    def __initStates(self):
        self.y_1 = 0
        self.x_1 = 0

    def calculateOutput(self, input):
        x = input
        y = self.p * (x + self.x_1) - self.o * self.y_1

        # Update states for next time
        self.x_1 = x
        self.y_1 = y

        return y