from week0 import agechange,keypad,tree,animation
from week1 import dictionary,fibonacci
from week2 import imperativegcd,oop
main_menu = [
    ["Dictionary: Dictionary, Palindrome, Lists and Loops", dictionary.tester],
]

patterns_sub_menu = [
    ["Tree", tree.treeprint],
    ["Animation", animation.face],
    ["Keypad", keypad.keypad],
  
]

oopMath_sub_menu = [
    ["OOP Factorial", oop.factorial_tester],
    ["OOP GCD", oop.gcd_tester],
    ["Age Change", agechange.agePrint],
]

impMath_sub_menu = [
    ["GCD", imperativegcd.printgcd],
    ["Fibonacci", fibonacci.tester],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns: Tree, Animation, Keypad", patterns_submenu])
    menu_list.append(["OOP Math: Factorial, GCD, Age Change", oopMath_submenu])
    menu_list.append(["Imperative Math: GCD, Fibonacci ", impMath_submenu])
    buildMenu(title, menu_list)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)
def oopMath_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, oopMath_sub_menu)
def impMath_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, impMath_sub_menu)

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

