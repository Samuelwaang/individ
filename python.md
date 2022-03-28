{% include navigation.html %}

[My Replit](https://replit.com/@SamuelWang22/individ#main.py) 

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@SamuelWang22/individ?embed=true"></iframe>

### Week 2:
OOP Factorial and Math Function

```
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
```

Imperative Math Function

``` 
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
```

### Week 1:
[dictionary (loops,lists)](https://github.com/Samuelwaang/individ/blob/main/dictionary.py)

```
InfoDb = []
InfoDb.append({
  #list
 "Fruit": "Apple",  
 "Taste": "Sweet",  
 "Grows": "Tree",  
 "ShelfLife": "3 Weeks",  
 "GrowthConditions":["cold in winter","moderate in summer","medium to high humidity","full sun"]  
})  

InfoDb.append({  
 "Fruit": "Lemon",  
 "Taste": "Sour",  
 "Grade": "Tree",  
 "ShelfLife": "3-4 Weeks",  
 "GrowthConditions":["tropical","subtropical humid","slightly acidic soil","full to partial sun"]  
})  

def print_data(n):
    print(InfoDb[n]["Fruit"], InfoDb[n]["Taste"])
    print("\t", "GrowthConditions: ", end="")
    print(", ".join(InfoDb[n]["GrowthConditions"]))
    print()

#for loop
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

#while loopp
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

#recursive loop
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

#prints the loops
def tester():
    print("For loop:")
    for_loop()
    print("While loop:")
    while_loop(0)
    print("Recursive loop:")
    recursive_loop(0)

    
```

[fibonacci](https://github.com/Samuelwaang/individ/blob/main/fibonacci.py) (This is in the math main category in the menu)

```
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
```

### Week 0: 
[menu](https://github.com/Samuelwaang/individ/blob/main/main.py)

```
import animation
import dictionary
main_menu = [
    ["dictionary", dictionary.tester],
]

sub_menu = [
    ["Age Change", "agechange.py"],
]

patterns_sub_menu = [
    ["Keypad", "keypad.py"],
    ["Tree", "tree.py"],
    ["Animation", animation.face],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")

    buildMenu(banner, options)

if __name__ == "__main__":
    menu() 
```

[animation](https://github.com/Samuelwaang/individ/blob/main/animation.py)

```
import time

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def face_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "   /-----\ ")
    print(sp + "  / . | . \ ")
    print(sp + "(|    <    |) ")
    print(sp + "  \ (===) / ")
    print(sp + "   \_____/  ")
    print(RESET_COLOR)

def face():

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        face_print(position)  # call to function with parameter
        time.sleep(.1)
```

tree

```
def tree(n):
  for tr in range(n):
      for space in range(n-tr):
          print(' ', end=' ')
      for leaf in range(2*tr+1):
          print('^',end=' ')
      print()
      for bark in range(n-1):
          print('  ', end=' ')
      print('||')
    
row = int(input('rows: '))
tree(row)
```

Age Change

```
def ageChange(age1, age2):
    #print(age1, age2)
    if (age1 > age2):
        num = age1
        age1 = age2
        age2 = num
    return age1,age2
print( ageChange(16, 21) )
print ( ageChange(21, 16) )
```
[commit](https://github.com/Samuelwaang/individ/commit/51d0c76ccc27f7dd73c6b1596c5f2247ff3562eb)
