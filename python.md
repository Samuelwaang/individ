{% include navigation.html %}

[My Replit](https://replit.com/@SamuelWang22/individ#main.py) 

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@SamuelWang22/individ?lite=true"></iframe>

### Week 0: 
[menu](https://github.com/Samuelwaang/individ/blob/main/main.py)

```import animation
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
