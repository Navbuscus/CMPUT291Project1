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
    primOwner = addOwner(True)
    secOwner = "null"
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
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
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
        print("Please enter the Vehicle's Serial Number (VSN):")
        serial_no = input(">>  ")
        if( serial_no.isdigit() and len(serial_no) == 7):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = %s" % serial_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("serial_no: %s, already exists in the DB!"% sin)   
                time.sleep(2)
        else:
            print("Error: you must enter a 7 digit integer value")
            time.sleep(2)

    os.system('clear')
    print("New Vehicle Registration")
    print("-----------------------------------")
    print("Please enter the Maker of the Vehicle")
    maker = input(">> ")
    maker = maker.lower()
    
    os.system('clear')
    print("New Vehicle Registration")
    print("-----------------------------------")
    print("Please enter the Model of the Vehicle")
    model = input(">> ")
    model = model.lower()    

    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
        print("Please enter the Year of the Vehicle: ")
        year = input(">> ")
        try:
            year = int(year)
            if( 1000 <= year <= 9999):
                break;
            else:
                print("Error: value too large")
                time.sleep(2)
        except ValueError:
            print("Error: please enter a number")
            time.sleep(2)

    os.system('clear')
    print("New Vehicle Registration")
    print("-----------------------------------")
    print("Please enter the Color of the Vehicle")
    color = input(">> ")
    color = color.lower()

    mainMenu.cursor.execute("SELECT type, type_id FROM vehicle_type")
    data = mainMenu.cursor.fetchall()
    vehicleType = dict((x.lower().strip(),y) for x,y in data)

    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
        print("please enter the type of the vehicle, from the following list: ")
        for row in vehicleType:
            print("- "+row)
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
    registerAgain()
    return

def addOwner(primary):
    while True:
        os.system('clear')
        print("New Vehicle Registration")
        print("-----------------------------------")
        owner = "secondary"
        if(primary):
            owner = "primary"
        print("Please enter the Social Insurance Number of the "+owner+" owner: ")

        pSin = input(">> ")
        if(pSin.isdigit() and len(pSin) == 9):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % pSin)
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
                        registerPerson()
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
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)
    return pSin


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
    
    mainMenu.connection.commit()         
    return





def registerAgain():
    os.system('clear')
    print("New Vehicle Registration")
    print("-----------------------------------")
    print("Vehicle Registered!")
    time.sleep(2)
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
