"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.


prime numbers: 2,3,5,7

Check the given number is prime or not

"""

class PrimeNumber(object):
    def is_prime_number(self, num):
        if num > 1:
            i=2
            while i <= num:
                if num % i == 0 and i != num:
                    return False
                i+=1
            return True


if __name__ == "__main__":
    print(PrimeNumber().is_prime_number(8))