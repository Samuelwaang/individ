def gcd(a, b):
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

# tester
def printgcd():
  print("The greatest common denominator of 36 and 48 is", gcd(36,48))
  print("The greatest common denominator of of 412 and 104 is", gcd(412,104))
  print("The greatest common denominator of of 21487 and 12938 is", gcd(2148,128938))