def recur_fibonacci(n):
  if n<=1:
    return n
  else:
    return(recur_fibonacci(n-2) +     recur_fibonacci(n-1))

def tester():
    try:
      num = int(input("fibonacci number terms: "))
      if num>0:
          print("Fibonacci sequence:")  
          for i in range(num):
             print(recur_fibonacci(i))
      else:
          print("positive numbers only")
    except ValueError:
        print("the fibonacci number can't be a character")

    