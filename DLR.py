import sys, os, time, cx_Oracle, mainMenu,datetime

def main():
    os.system('clear')
    print("Drivers License Registration")
    print("-----------------------------------")
    print ("1. Register new person")
    print ("2. Register new driver's license")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    if choice == "0":
        return
    registerAgain()

def personTitle():
    os.system('clear')
    print("Drivers License Registration")
    print("Registering Person into database")
    print("-----------------------------------")

def registerPerson():
    while True:
        personTitle()
        print("Please enter the person's Social Insurance Number (SIN):")
        sin = input(">>  ")
        if( sin.isdigit() and len(sin) == 9):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT people.sin FROM people WHERE people.sin = %s" % sin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("SIN: %s, already exists in the DB!"% sin)   
                time.sleep(2)
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)
    while True:
        personTitle()
        print("Please enter the person's name")
        name = input(">> ")
        name = name.lower()
        if len(name) <= 40:
            break
        print("Error: Name too large. MAX 40 characters allowed")
        time.sleep(2)

    
    while True:
        personTitle()
        print("Please enter the person's height (cm): ")
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
        personTitle()
        print("Please enter the person's weight (kg): ")
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
    while True:
        personTitle()
        print("Please enter the person's eye colour")
        eye = input(">> ")
        eye = eye.lower()
        if len(eye) <= 10:
            break
        print("Error: value too large. MAX 10 characters allowed")
        time.sleep(2)
    while True:
        personTitle()
        print("Please enter the person's hair colour")
        hair = input(">> ")
        hair = hair.lower()
        if len(hair) <= 10:
            break
        print("Error: value too large. MAX 10 characters allowed")
        time.sleep(2)
    while True:
        personTitle()
        print("Please enter the person's adress")
        addr = input(">> ")
        addr = addr.lower()
        if len(addr) <= 50:
            break
        print("Error: value too large. MAX 50 characters allowed")
        time.sleep(2)
    while True:
        personTitle()
        print("Please select person's gender (m/f)")
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
        personTitle()
        print("Please enter the person's birthday (MMDDYYYY):")
        bdate = input(">>  ")
        try:
            date = datetime.datetime.strptime(bdate,'%m%d%Y')
            break
        except ValueError:
            print("Error: Not a valid date. Please enter date in the 'MMDDYYY' format.")
            time.sleep(2)   
    
    
    insert = """INSERT into PEOPLE (SIN, NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
    values (:SIN,:NAME, :HEIGHT, :WEIGHT, :EYECOLOR, :HAIRCOLOR, :ADDR, :GENDER, TO_DATE(:BIRTHDAY,'MMDDYYYY'))"""
    mainMenu.cursor.execute(insert,{'SIN':sin, 'NAME':name,'HEIGHT':height, 'WEIGHT':weight, 'EYECOLOR':eye,'HAIRCOLOR':hair, 'ADDR':addr, 'GENDER':gender, 'BIRTHDAY':bdate})  
    
    mainMenu.connection.commit()        
    


def driverTitle():
    os.system('clear')
    print("Drivers License Registration")
    print("Registering Drivers License into database")
    print("-----------------------------------")
    
def registerDriver():

    while True:
        driverTitle()
        print("Please enter drivers Social Insurance Number (SIN: ")
        dSin = input(">> ")
        if(dSin.isdigit() and len(dSin) == 9):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % dSin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                while True:
                    print("Error: that person is not in our database. Would you like to register this person? (Y/N):")
                    choice = input(">> ")
                    choice = choice.lower()
                    if choice == "y":
                        registerPerson()
                    elif choice == "n":
                        print("Please Enter a SIN that is in our database")
                        time.sleep(2)
                        registerDriver()
                    else:
                        print("Error: invalid choice")
            else:
                break;
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)
            
    while True:
        driverTitle()
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
        driverTitle()
        print("Please enter the driver's license Class Number:")
        class_no = input(">>  ")
        
        if(class_no.isdigit()):
            dclass = "Class " + class_no
            break
        else:
            print("Error: you must enter a valid class number")
            time.sleep(2)    

    
    while True:
        driverTitle()
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
        driverTitle()
        print("Please enter the driver's licence issue date  (MMDDYYYY):")
        idate = input(">>  ")
        if(idate.isdigit() and len(idate) == 8):
            break;
        else:
            print("Error: you must enter your birthday as MMDDYYY")
            time.sleep(2)
    edate=str(int(idate)+5)
    
    insert2 = """INSERT into DRIVE_LICENCE (LICENCE_NO, SIN, CLASS, PHOTO, ISSUING_DATE, EXPIRING_DATE)
    values (:LICENCE_NO, :SIN, :CLASS, :PHOTO, TO_DATE(:ISSUING_DATE,'MMDDYYYY'), TO_DATE(:EXPIRING_DATE,'MMDDYYYY'))"""
    mainMenu.cursor.execute(insert2,{'LICENCE_NO':licence_no,'SIN':sin,'CLASS':dclass,'PHOTO':image,'ISSUING_DATE':idate,'EXPIRING_DATE':edate})
    
    mainMenu.connection.commit() 

def registerAgain():
    main();


def exec_menu(choice,context):
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions[context]()
    elif ch =='1':
        mainMenu.registerPerson("Drivers License Registration")
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
    '2':registerDriver,
    '0': exit,
    'registerAgain':registerAgain
}
