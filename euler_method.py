from decimal import Decimal
from math import exp

class EulerMethod:
    def __init__(self, f, g, start, end, iv):
        self.f = f
        self.g = g
        self.start = start
        self.end = end
        self.iv = iv

    def approximate(self, inc):
        curY = self.iv
        curT = self.start
        while curT <= self.end:
            gEval = self.g(curT)
            print(f"y({curT}) = {curY}; Φ({curT}) = {gEval}; Difference: {gEval - curY}")
            curY = curY + self.f(curT, curY) * (inc)
            curT += inc


ranges = [Decimal(i) for i in (".1", ".05", ".025")]
print("For y' = 3 + t - y")
f = lambda t, y: 3 + t - y
g = lambda t: t + Decimal('2') - (-t).exp()
for r in ranges:
    print("Increment of", r)
    EulerMethod(f, g, Decimal('0'), Decimal('0.4'), Decimal('1')).approximate(r)

print("\nFor y' = 0.5 - t + 2y")
f = lambda t, y: Decimal('0.5') - t + 2 * y
g = lambda t: Decimal('0.5') * t + Decimal.exp(2 * t)
for r in ranges:
    print("Increment of", r)
    EulerMethod(f, g, Decimal('0'), Decimal('0.4'), Decimal('1')).approximate(r)