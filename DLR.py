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
    """
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
    eye = eye.lower()


    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the driver's hair colour")
    hair = input(">> ")
    hair = hair.lower()

    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the driver's adress")
    addr = input(">> ")
    addr = addr.lower()
    
    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please select driver's gender (m/f)")
        choice = input(">> ")
        if(choice == "m"):
            gender = 'm'
            break;
        elif(choice == "f"):
            gender = 'f'
            break;
        else:
            print("Error: invalid selection")
            time.sleep(2)

    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's birthday (YYYYMMDD):")
        bd = input(">>  ")
        if(bd.isdigit() and len(bd) == 8):
            break;
        else:
            print("Error: you must enter your BD as YYYYMMDD")
            time.sleep(2)
    
    statement = "INSERT into PEOPLE values(sin,name,height,weight,eye,hair,addr,gender,bd)"
    mainMenu.cursor.execute(statement)
    """
    sin = '000000000'
    name = 'Fred'
    height = 123.00
    weight = 78.00
    eye = 'blue'
    hair = 'blonde'
    addr = '1234 fake street'
    gender = 'm'
    bdate = '19900101'
    
    #statement = "INSERT into PEOPLE values(sin,name,height,wieght,eye,hair,addr,gender,bd)"
    #mainMenu.cursor.execute(statement)
    insert = """INSERT into PEOPLE (SIN, NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
    values (:SIN,:NAME, :HEIGHT, :WEIGHT, :EYECOLOR, :HAIRCOLOR, :ADDR, :GENDER, TO_DATE(:BIRTHDAY,'YYYYMMDD'))"""
    mainMenu.cursor.execute(insert,{'SIN':sin, 'NAME':name,'HEIGHT':height, 'WEIGHT':weight, 'EYECOLOR':eye,'HAIRCOLOR':hair, 'ADDR':addr, 'GENDER':gender, 'BIRTHDAY':bdate})    
    
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
