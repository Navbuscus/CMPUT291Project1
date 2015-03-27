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

def title():
    os.system('clear')
    print("New Vehicle Registration")
    print("-----------------------------------")

def registerVehicle():
    primOwner = addOwner(True)
    secOwner = "null"

    while True:
        title()
        print("Would you like to add a secondary owner? (Y/N): ")
        choice = input(">> ")
        choice = choice.lower()
        if choice == 'y':
            secOwner = addOwner(False)
            break
        elif choice == 'n':
            break
        else:
            print("Error: invalid choice")


    while True:
        title()
        print("Please enter the Vehicle's Serial Number (VSN):")
        serial_no = input(">>  ").strip()
        if(1 <= len(serial_no) <= 15):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = '%s'" % serial_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("Error: VSN %s is already in our database. Please enter a new VSN.")   
                time.sleep(2)
        else:
            print("Error: invalid input. MIN 1 character and MAX 15 characters")
            time.sleep(2)

    
    while True:
        title()
        print("Please enter the Maker of the Vehicle")
        maker = input(">> ")
        maker = maker.lower().strip()
        if 1 <= len(maker) <= 20:
            break
        print("Error: invalid input. MIN 1 character  MAX 20 characters")
        time.sleep(2)
    
    
    while True:
        title()
        print("Please enter the Model of the Vehicle")
        model = input(">> ")
        model = model.lower().strip()
        if 1 <= len(model) <= 20:
            break
        print("Error: invalid input.MIN 1 character MAX 20 characters")
        time.sleep(2)

    while True:
        title()
        print("Please enter the Year of the Vehicle: ")
        year = input(">> ")
        try:
            year = int(year)
            if( 1000 <= year <= 9999):
                break;
            else:
                print("Error: invalid input, please enter 4 character value")
                time.sleep(2)
        except ValueError:
            print("Error:invalid input, please enter a number")
            time.sleep(2)

   
    while True:
        title()
        print("Please enter the Color of the Vehicle")
        color = input(">> ")
        color = color.lower().strip()
        if 1 <= len(color) <= 10:
            break
        print("Error: invalid input. MIN 1 character MAX 10 characters")
        time.sleep(2)

    mainMenu.cursor.execute("SELECT type, type_id FROM vehicle_type")
    data = mainMenu.cursor.fetchall()
    vehicleType = dict((x.lower().strip(),y) for x,y in data)
    while True:
        title()
        print("Please enter the type of the vehicle, from the following list: ")
        for row in vehicleType:
            print("* "+row)
        print("")
        vtype = input(">> ")
        vtype = vtype.lower().strip()
        if vtype in vehicleType:
            type_id = vehicleType.get(vtype)
            break;
        else: 
            print("Error: invalid vehicle type")
            time.sleep(2)
            continue;
    


    insert = """INSERT into VEHICLE (SERIAL_NO,MAKER,MODEL,YEAR,COLOR,TYPE_ID)
    values (:SERIAL_NO,:MAKER,:MODEL,:YEAR,:COLOR,:TYPE_ID)"""
    mainMenu.cursor.execute(insert,{'SERIAL_NO':serial_no,'MAKER':maker,'MODEL':model,'YEAR':year,'COLOR':color,'TYPE_ID':type_id})  
    

    insert = """INSERT into OWNER (OWNER_ID, VEHICLE_ID,IS_PRIMARY_OWNER)
    values (:OWNER_ID,:VEHICLE_ID,'y')"""
    mainMenu.cursor.execute(insert,{'OWNER_ID':primOwner,'VEHICLE_ID':serial_no})

    if(secOwner != "null"):
        insert = """INSERT into OWNER (OWNER_ID, VEHICLE_ID,IS_PRIMARY_OWNER)
    values (:OWNER_ID,:VEHICLE_ID,'n')"""
        mainMenu.cursor.execute(insert,{'OWNER_ID':secOwner,'VEHICLE_ID':serial_no,})

    mainMenu.connection.commit()  
    title()
    print("Vehicle Registered!")
    time.sleep(2)
    registerAgain()
    return

def addOwner(primary):
    while True:
        title()
        owner = "secondary"
        if(primary):
            owner = "primary"
        print("Please enter the Social Insurance Number of the "+owner+" owner: ")

        pSin = input(">> ").strip()
        if(1 <= len(pSin) <= 15):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = '%s'" % pSin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                while True:
                    os.system('clear')
                    print("New Vehicle Registration")
                    print("-----------------------------------")
                    print("Error: that person is not in our database. Would you like to register this person? (Y/N):")
                    choice = input(">> ")
                    choice = choice.lower()
                    if choice == "y":
                        mainMenu.registerPerson("New Vehicle Registration")
                        break
                    elif choice == "n":
                        print("Please Enter a SIN that is in our database")
                        time.sleep(2)
                        break
                    else:
                        print("Error: invalid choice")
            else:
                break;
        else:
            print("Error: invalid input. MIN 1 character MAX 15 characters")
            time.sleep(2)
    return pSin

def registerAgain():
    main()


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
