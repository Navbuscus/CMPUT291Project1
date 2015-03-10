import sys, os, mainMenu, time, cx_Oracle

def main():
    os.system('clear')
    print("Vehicle Registration")
    print("-----------------------------------")
    print ("1. Register Vehicle")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def register():
    os.system('clear')
    print("Vehicle Registration")
    print("-----------------------------------")
    print("Please enter the maker of your car")
    maker = input(">> ")

    print("Please enter the model of your car")
    model = input(">> ")

    print("Please enter the year of your car")
    year = input(">> ")

    print("Please enter the color of your car")
    color = input(">> ")
    print("maker:", maker, " model:", model, " year:",year," color:",color)
    print("registering into database...")
    print("successful!")
    registerAgain()
    return

def registerAgain():
    print("----------------------------------")
    print("1. Register Another Vehicle")
    print("0. Back to main menue")
    choice = input(">> ")
    exec_menu(choice,'registerAgain')
    return

def exec_menu(choice,context):
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions[context]()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            time.sleep(1)
            menu_actions[context]()
    return

def exit():
    return
 

menu_actions = {
    'main':main,
    '1':register,
    '0': exit,
    'registerAgain':registerAgain
}
