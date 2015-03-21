import sys, os, time, cx_Oracle, mainMenu

def main():
    os.system('clear')
    print("New Vehicle Registration")
    print("-----------------------------------")
    print ("1. Register New Vehicle")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def registerVehicle():
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
        print(" Please enter the Social Insurance Number of the primary owner: ")
        pSin = input(">> ")
        if(pSin.isdigit() and len(pSin) == 9):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % pSin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                while True:
                    print("Error: that person is not in our database. Would you like to register this person? (Y/N):")
                    choice = input(">> ")
                    choice = choice.lower()
                    if choice == "y":
                        registerPerson()
                        break;
                    elif choice == "n":
                        print("Please Enter a SIN that is in our database")
                        time.sleep(2)
                        registerVehicle()
                    else:
                        print("Error: invalid choice")
            else:
                break;
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)



        
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
        print("Please enter the Vehicle's Serial Number (VSN):")
        serial_no = input(">>  ")
        if( serial_no.isdigit() and len(serial_no) == 10):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = %s" % serial_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("serial_no: %s, already exists in the DB!"% sin)   
                time.sleep(2)
        else:
            print("Error: you must enter a 10 digit integer value")
            time.sleep(2)

    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the Maker of the Vehicle")
    maker = input(">> ")
    maker = maker.lower()
    
    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print("Please enter the Model of the Vehicle")
    model = input(">> ")
    model = model.lower()    

    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the Year of the Vehicle: ")
        year = input(">> ")
        try:
            if( float(year) <= 9999):
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
    print("Please enter the Color of the Vehicle")
    colour = input(">> ")
    colour = colour.lower()
    
    mainMenu.cursor.execute("SELECT sin FROM people WHERE sin=123456789")
    print("data: ")
    print(mainMenu.cursor.fetchone())

  
    registerAgain()
    return

def registerAgain():
    print("----------------------------------")
    print("1.register another vehicle")
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
    '1':registerVehicle,
    '0': exit,
    'registerAgain':registerAgain
}
