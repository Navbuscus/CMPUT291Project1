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
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % sin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("SIN: %s, already exists in the DB!"% sin)   
                time.sleep(2)
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
        print("Please enter the driver's birthday (MMDDYYYY):")
        bdate = input(">>  ")
        if(bdate.isdigit() and len(bdate) == 8):
            break;
        else:
            print("Error: you must enter your birthday as MMDDYYY")
            time.sleep(2)
    
    """
    #quick testing
    sin = '000000000'
    name = 'Fred'
    height = 123.00
    weight = 78.00
    eye = 'blue'
    hair = 'blonde'
    addr = '1234 fake street'
    gender = 'm'
    bdate = '01011990'
    """
    
    insert = """INSERT into PEOPLE (SIN, NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
    values (:SIN,:NAME, :HEIGHT, :WEIGHT, :EYECOLOR, :HAIRCOLOR, :ADDR, :GENDER, TO_DATE(:BIRTHDAY,'MMDDYYYY'))"""
    mainMenu.cursor.execute(insert,{'SIN':sin, 'NAME':name,'HEIGHT':height, 'WEIGHT':weight, 'EYECOLOR':eye,'HAIRCOLOR':hair, 'ADDR':addr, 'GENDER':gender, 'BIRTHDAY':bdate})  

    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's license number (LN):")
        licence_no = input(">>  ")
        if( licence_no.isdigit() and len(licence_no) == 12):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT licence_no FROM drive_licence WHERE licence_no = %s" % licence_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("LN: %s, already exists in the DB!"% licence_no)   
                time.sleep(2)
        else:
            print("Error: you must enter a 12 digit integer value")
            time.sleep(2)
            
    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's license Class Number:")
        class_no = input(">>  ")
        
        if(class_no.isdigit()):
            dclass = "Class " + class_no
            break
        else:
            print("Error: you must enter a valid class number")
            time.sleep(2)    

    
    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's license Photo name including its extention (e.g. 'photo.jpg' ")
        photo = input(">> ")
        try:
            f_image = open(photo,'rb')
            break;
        except IOError:
            print("Error: file could not be opened.") 
            print("    Ensure you have given the proper file name (case sensitive) and ")
            print("    File is in program directory")

    image = f_image.read()


    while True:
        os.system('clear')
        print("Drivers License Registration")
        print("-----------------------------------")
        print("Please enter the driver's licence issue date  (MMDDYYYY):")
        idate = input(">>  ")
        if(idate.isdigit() and len(idate) == 8):
            break;
        else:
            print("Error: you must enter your birthday as MMDDYYY")
            time.sleep(2)
    edate=str(int(idate)+5)

    #licence_no = 80085 #boobs 
    
    insert = """INSERT into DRIVE_LICENCE (LICENCE_NO, SIN, CLASS, PHOTO, ISSUING_DATE, EXPIRING_DATE)
    values (:LICENCE_NO, :SIN, :CLASS, :PHOTO, TO_DATE(:ISSUING_DATE,'MMDDYYYY'), TO_DATE(:EXPIRING_DATE,'MMDDYYYY')))"""
    mainMenu.cursor.execute(insert,{'LICENCE_NO':licence_no,'SIN':sin,'CLASS':dclass,'PHOTO':image,'ISSUING_DATE':idate,'EXPIRING_DATE':edate})
    
    mainMenu.connection.commit()    
    
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
