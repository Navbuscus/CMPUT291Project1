import sys, os, time, cx_Oracle, mainMenu,datetime, random

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

def driverTitle():
    os.system('clear')
    print("Drivers License Registration")
    print("Registering Drivers License into database")
    print("-----------------------------------")
    
def registerDriver():

    while True:
        driverTitle()
        print("Please enter drivers Social Insurance Number (SIN: ")
        dSin = input(">> ").strip()
        if(1 <= len(dSin) <= 15):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = '%s'" % dSin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                while True:
                    print("Error: that person is not in our database. Would you like to register this person? (Y/N):")
                    choice = input(">> ")
                    choice = choice.lower()
                    if choice == "y":
                        mainMenu.registerPerson("Drivers Licence Registration")
                        break;
                    elif choice == "n":
                        print("Please Enter a SIN that is in our database")
                        time.sleep(2)
                        registerDriver()
                    else:
                        print("Error: invalid choice")
            else:
                mainMenu.cursor.execute("SELECT sin FROM drive_licence WHERE sin = %s" % dSin)
                data = mainMenu.cursor.fetchone()
                if data is None:
                    break;
                else:
                    print("Error: This person already has a drivers license. please enter a different SIN.")
                    time.sleep(2)
        else:
            print("Error: Invalid input.MIN 1 character MAX 15 characters")
            time.sleep(2)
            
    while True:
        driverTitle()
        print("Please enter the driver's license number (LN):")
        licence_no = input(">>  ").strip()
        if(1 <= len(licence_no) <= 15):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT licence_no FROM drive_licence WHERE licence_no = %s" % licence_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("LN: %s, already exists in the DB!"% licence_no)   
                time.sleep(2)
        else:
            print("Error: Invalid input. MIN 1 character MAX 15 characters")
            time.sleep(2)
            
    while True:
        driverTitle()
        print("Please enter the driver's license Class Number:")
        class_no = input(">>  ").strip()
        
        if(class_no.isdigit() and int(class_no) in range(1,8)):
            dclass = "Class " + class_no
            break
        else:
            print("Error: you must enter a valid class number between 1 and 7")
            time.sleep(2)    

    while True:
        driverTitle()
        print("Please enter driving condition(leave blank if none)")
        dCondition = input(">> ").lower().strip()
        if 1<= len(dCondition) <= 1024:
            break
        print("Error: value too large. MAX 1024 characters allowed")
        time.sleep(2)
        
    while True:
        c_id = random.randint(100000000,999999999) 
        mainMenu.cursor.execute("SELECT c_id FROM driving_condition WHERE c_id = %d" %c_id)
        result = mainMenu.cursor.fetchone()
        if result is None:
            break


    while True:
        driverTitle()
        print("Please enter the driver's license Photo name including its extention (e.g. 'photo.jpg' ")
        photo = input(">> ").strip()
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
        print("Please enter the drivers licence issue date (MMDDYYYY):")
        idate = input(">>  ").strip()
        try:
            date = datetime.datetime.strptime(idate,'%m%d%Y')
            break
        except ValueError:
            print("Error: Not a valid date. Please enter date in the 'MMDDYYY' format.")
            time.sleep(2)   



    while True:
        driverTitle()
        print("Please enter the drivers licence expiration date (MMDDYYYY):")
        edate = input(">>  ").strip()
        try:
            date = datetime.datetime.strptime(edate,'%m%d%Y')
            break
        except ValueError:
            print("Error: Not a valid date. Please enter date in the 'MMDDYYY' format.")
            time.sleep(2)   



    insert2 = """INSERT into DRIVE_LICENCE (LICENCE_NO, SIN, CLASS, PHOTO, ISSUING_DATE, EXPIRING_DATE)
    values (:LICENCE_NO, :SIN, :CLASS, :PHOTO, TO_DATE(:ISSUING_DATE,'MMDDYYYY'), TO_DATE(:EXPIRING_DATE,'MMDDYYYY'))"""
    mainMenu.cursor.execute(insert2,{'LICENCE_NO':licence_no,'SIN':dSin,'CLASS':dclass,'PHOTO':image,'ISSUING_DATE':idate,'EXPIRING_DATE':edate})
    
    insert = """INSERT into DRIVING_CONDITION (C_ID,DESCRIPTION)
    values (:C_ID,:DESCRIPTION)"""
    mainMenu.cursor.execute(insert, {'C_ID':c_id,'DESCRIPTION':dCondition})

    insert =  """INSERT into restriction (LICENCE_NO,R_ID)
    values (:LICENCE_NO,:R_ID)"""
    mainMenu.cursor.execute(insert,{'LICENCE_NO':licence_no,'R_ID':c_id})

    mainMenu.connection.commit() 

    driverTitle()
    print("Drivers Licence registered!")
    time.sleep(2)

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
