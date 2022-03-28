class Factorial:
    def __init__(self):
        self.fact = [0, 1]
    def __call__(self, n):
      # factorial at 1 or 0 is always 1
      if n == 1 or n == 0:
          return 1
      else:
      # multiplies given term and all the previous terms
          return n * self(n-1)

class GCD:
    def __call__(self, a, b):
  # greatest common denominator of 0 is always 0
      if a == 0:
        return a
  # when b isn't 0
      while b != 0:
          if a > b:
              a = a - b
          else:
              b = b - a
      return a

def factorial_tester():
  factor_of = Factorial()
  print("The factorial of 3 is", factor_of(3))
  print("The factorial of 8 is", factor_of(8))
  print("The factorial of 17 is", factor_of(17))


def gcd_tester():
  gcd_of = GCD()
  print("The greatest common denominator of 36 and 48 is", gcd_of(36,48))
  print("The greatest common denominator of of 412 and 104 is", gcd_of(412,104))
  print("The greatest common denominator of of 21487 and 12938 is", gcd_of(2148,128938))
