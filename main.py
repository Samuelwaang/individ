import animation
import dictionary
import fibonacci
main_menu = [
    
]

week0_sub_menu = [
    ["Age Change", "agechange.py"],
    ["Tree", "tree.py"],
    ["Animation", animation.face],
    ["Keypad", "keypad.py"],
]

week1_sub_menu = [
    ["Fibonacci", fibonacci.tester],
    ["dictionary", dictionary.tester],
]

week2_sub_menu = [

]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", week0_submenu])
    menu_list.append(["Week 1", week1_submenu])
    menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)

def week0_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week0_sub_menu)
def week1_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week1_sub_menu)
def week2_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week2_sub_menu)

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
