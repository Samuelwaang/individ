def recur_fibonacci(n):
  if n<=1:
    return n
  else:
    # adds the two terms before the term
    return(recur_fibonacci(n-2) +     recur_fibonacci(n-1))

def tester():
  # tests if number isa number
    try:
      num = int(input("fibonacci number terms: "))
      # tests if number inputter is greater than 0
      if num>0:
          print("Fibonacci sequence:")  
          for i in range(num):
             print(recur_fibonacci(i))
      else:
          print("positive numbers only")
    except ValueError:
        print("the fibonacci number can't be a character")

    