import sys, os, time, cx_Oracle, mainMenu

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

    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's Social Insurance Number (SIN):")
        sin = input(">>  ")
        if( sin.isdigit() and len(sin) == 9):
            break;
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)
    


    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the driver's name")
    name = input(">> ")
    name = name.lower()

    
    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's height (cm): ")
        height = input(">> ")
        try:
           float(height)
           if( float(height) <= 999.99):
               break;
           else:
               print("Error: value too large")
               time.sleep(2)
        except ValueError:
            print("Error: please enter a number")
            time.sleep(2)


    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's weight (kg): ")
        weight = input(">> ")
        try:
           float(weight)
           if( float(weight) <= 999.99):
               break;
           else:
               print("Error: value too large")
               time.sleep(2)
        except ValueError:
            print("Error: please enter a number")
            time.sleep(2)

    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the driver's eye colour")
    eye = input(">> ")
    eye = name.lower()


    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the driver's hair colour")
    hair = input(">> ")
    hair = name.lower()

    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the driver's adress")
    addr = input(">> ")
    addr = name.lower()
    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please select driver's gender")
        print("1. Male")
        print("2. Female")
        choice = input(">> ")
        if(choice == "1"):
            gender = 'm'
            break;
        elif(choice == '2'):
            gender = 'f'
            break;
        else:
            print("Error: invalid selection")
            time.sleep(2)


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
