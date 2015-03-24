import sys, os, time,cx_Oracle,mainMenu, random 

def title():
    os.system('clear')
    print("Auto Transaction")
    print("-----------------------------------")

def main():
    title()
    print ("1. Setup auto transaction")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def transaction():
    while True:
        title()
        print("Please enter the Vehicle Serial Number (VSN) of the vehicle to be sold")
        vsn = input(">> ")
        if(vsn.isdigit() and len(vsn) == 10):
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = %s" % vsn)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: vehicle no in database. Please enter another VSN")
                time.sleep(2)
            else:
                break
        else:
            print("Error: you must enter a 10 digit integer value")
            time.sleep(2)

            
    while True:
        title()
        print("Please enter the Social Insurance Number (SIN) of the vehicle's seller")
        sSin = input(">> ")
        if(sSin.isdigit() and len(sSin) == 10):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % sSin)
            dSin = mainMenu.cursor.fetchone()
            if dsin is None:
                print("Error: Seller not in database. Please enter sellers SIN")
                time.sleep(2)
            else:
                mainMenu.cursor.execute("SELECT owner_id FROM owner WHERE vehicle_id = %s" % vsn)
                owners = mainMenu.cursor.fetchall()
                for owner in owners:
                    owners.pop(owner)
                    owners.append(owner.strip())
                if dSin in owners:
                    break
                else:
                    print("Error: seller entered does not own this vehicle.")
                    time.sleep(2)

        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)
        
        while True:
            title()
            print("Please enter the Social Insurance Number (SIN) of the vehicle's buyer")
        bSin = input(">> ")
        if(bSin.isdigit() and len(bSin) == 10):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % bSin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: Buyer not in database. Would you like to add them? (Y/N):")
                choice = input(">> ")
                if choice.lower() == "y":
                    registerPerson()
                elif choice.lower() == "n":
                    print("Please enter new SIN")
                    continue
                else:
                    print("Error: Invalid choice")
                    time.sleep(2)

            else:
                break
                mainMenu.cursor.execute("SELECT owner_id FROM owner WHERE vehicle_id = %s" % vsn)
                owners = mainMenu.cursor.fetchall()
                for owner in owners:
                    owners.pop(owner)
                    owners.append(owner.strip())
                if dSin in owners:
                    break
                else:
                    print("Error: seller entered does not own this vehicle.")
                    time.sleep(2)
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)
    while True:
        t_id = randint(100000000,999999999) 
        mainMenu.cursor.execute("SELECT transaction_id FROM auto_sale WHERE transaction_id = %d" %t_id)
        result = cursor.fetchone()
        if result == 0:
            break
    transactionAgain()
    return

def registerPerson():
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("Registering Person into database")
        print("-----------------------------------")
        print("Please enter the person's Social Insurance Number (SIN):")
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
    print("New Vehicle Registration")
    print("Registering Person into database")
    print("-----------------------------------")
    print("Please enter the person's name")
    name = input(">> ")
    name = name.lower()

    
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("Registering Person into database")
        print("-----------------------------------")
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
        os.system('clear')
        print("New Vehicle Registration")
        print("Registering Person into database")
        print("-----------------------------------")
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

    os.system('clear')
    print("New Vehicle Registration")
    print("Registering Person into database")
    print("-----------------------------------")
    print("Please enter the person's eye colour")
    eye = input(">> ")
    eye = eye.lower()

    os.system('clear')
    print("New Vehicle Registration")
    print("Registering Person into database")
    print("-----------------------------------")
    print("Please enter the person's hair colour")
    hair = input(">> ")
    hair = hair.lower()

    os.system('clear')
    print("New Vehicle Registration")
    print("Registering Person into database")
    print("-----------------------------------")
    print("Please enter the person's adress")
    addr = input(">> ")
    addr = addr.lower()
    
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("Registering Person into database")
        print("-----------------------------------")
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
        os.system('clear')
        print("New Vehicle Registration")
        print("Registering Person into database")
        print("-----------------------------------")
        print("Please enter the person's birthday (MMDDYYYY):")
        bdate = input(">>  ")
        if(bdate.isdigit() and len(bdate) == 8):
            break;
        else:
            print("Error: you must enter your birthday as MMDDYYY")
            time.sleep(2)
    
    insert = """INSERT into PEOPLE (SIN, NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
    values (:SIN,:NAME, :HEIGHT, :WEIGHT, :EYECOLOR, :HAIRCOLOR, :ADDR, :GENDER, TO_DATE(:BIRTHDAY,'MMDDYYYY'))"""
    mainMenu.cursor.execute(insert,{'SIN':sin, 'NAME':name,'HEIGHT':height, 'WEIGHT':weight, 'EYECOLOR':eye,'HAIRCOLOR':hair, 'ADDR':addr, 'GENDER':gender, 'BIRTHDAY':bdate})  
    
    mainMenu.connection.commit()        
    return

def transactionAgain():
    print("----------------------------------")
    print("1.Setup another auto transaction")
    print("0. Back to main menue")
    choice = input(">> ")
    exec_menu(choice,'transactionAgain')
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
    '1':transaction,
    '0': exit,
    'transactionAgain':transactionAgain
}
