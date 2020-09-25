class Filter:
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
        y(k) = --- (x(k) + x(k-1)) - --- y(k-1)  =  P * (x(k) + x(k-1)) - O * y(k-1)
                C                     C

    Additional notes:
    - "x(k-1)", for example, is named as a variable as "x_1"
    - smaller the T constant, more accurate the output becomes
    """

    def __init__(self, T, Tf):
        self._calcConstants(T, Tf)
        self._initStates()

    def _calcConstants(self, T, Tf):
        A = T
        B = T - 2*Tf
        C = T + 2*Tf
        self.P = A / C
        self.O = B / C

    def _initStates(self):
        self._setLastStates(0, 0)

    def calculateOutput(self, input):
        x = input
        y = self.P * (x + self.x_1) - self.O * self.y_1
        # Update states for next time
        self._setLastStates(x, y)
        return y

    def _setLastStates(self, x_1, y_1):
        self.x_1 = x_1
        self.y_1 = y_1
