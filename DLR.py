import sys, os, mainMenu, time, cx_Oracle

def main():
    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print ("1. Register new driver")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def register():
    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the drivers name")
    driver = input(">> ")
    print(driver,"has been registered as a driver, yeah i got lazy here")
    registerAgain()
    return

def registerAgain():
    print("----------------------------------")
    print("1.register another driver")
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
