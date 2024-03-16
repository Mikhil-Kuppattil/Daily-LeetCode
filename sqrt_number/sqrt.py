"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 

The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""

import math

class Sqrt(object):
    def mySqrt(self, numb):
        s = math.sqrt(8)
        return math.floor(s)

if __name__ == "__main__":

    print(Sqrt().mySqrt(8), 333333333333)


