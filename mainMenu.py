import sys, os, time, cx_Oracle,datetime,getpass
import NVR,AT,DLR,VR,SE


# Main menu
def main_menu():
    os.system('clear')
    
    print ("Welcome, %s\n" %user)
    print ("Please choose the menu you want to start:")
    print ("1. New Vehicle Registration")
    print ("2. Auto Transaction")
    print ("3. Driver Licence Registration")
    print ("4. Violation Record")
    print ("5. Search Engine")
    print ("\n0. Exit")
    choice = input(" >>  ")
    exec_menu(choice)
 
    return
 
# Execute menu
def exec_menu(choice):
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            time.sleep(1)
            menu_actions['main_menu']()
    return
 
def New_Vehicle_Registration():
    NVR.main()
    back()
    
def Auto_Transaction():
    AT.main()
    back()
    
def Drivers_Licence_Registration():
    DLR.main()
    back()

def Violation_Record():
    VR.main()
    back()

def Search_Engine():
    SE.main()
    back()
 
# Back to main menu
def back():
    main_menu()
 
# Exit program
def exit():
    cursor.close()
    connection.close()    
    sys.exit()
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': New_Vehicle_Registration,
    '2': Auto_Transaction,
    '3': Drivers_Licence_Registration,
    '4': Violation_Record,
    '5': Search_Engine,
    '9': back,
    '0': exit,
}


def title(header):
    os.system('clear')
    print(header)
    print("Registering new person")
    print("-----------------------------------")


def registerPerson(header):
    #SIN#
    while True:
        title(header)
        print("Please enter the person's Social Insurance Number (SIN):")
        sin = input(">>  ")
        if( sin.isdigit() and len(sin) == 9):
            # testing for UNIQUE-KEY CONSTRAINT 
            cursor.execute("SELECT people.sin FROM people WHERE people.sin = %s" % sin)
            data = cursor.fetchone()
            if data is None:
                break;
            else:
                print("SIN: %s, already exists in the DB!"% sin)   
                time.sleep(2)
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)

    #NAME#
    while True:
        title(header)
        print("Please enter the person's name")
        name = input(">> ")
        name = name.lower()
        if len(name) <= 40:
            break
        print("Error: Name too large. MAX 40 characters allowed")
        time.sleep(2)

    #HEIGHT#
    while True:
        title(header)
        print("Registering New Person")
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

    #WEIGHT#
    while True:
        title(header)
        print("Registering New Person")
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

    #EYE#
    while True:
        title(header)
        print("Registering New Person")
        print("Please enter the person's eye colour")
        eye = input(">> ")
        eye = eye.lower()
        if len(eye) <= 10:
            break
        print("Error: value too large. MAX 10 characters allowed")
        time.sleep(2)
   
    #HAIR#
    while True:
        title(header)
        print("Registering New Person")
        print("Please enter the person's hair colour")
        hair = input(">> ")
        hair = hair.lower()
        if len(hair) <= 10:
            break
        print("Error: value too large. MAX 10 characters allowed")
        time.sleep(2)

    #ADDRESS#
    while True:
        title(header)
        print("Registering New Person")
        print("Please enter the person's address")
        addr = input(">> ")
        addr = addr.lower()
        if len(addr) <= 50:
            break
        print("Error: value too large. MAX 50 characters allowed")
        time.sleep(2)

    #GENDER#
    while True:
        title(header)
        print("Registering New Person")
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
  
    #DATE#
    while True:
        title(header)
        print("Please enter the person's birthday (MMDDYYYY):")
        bdate = input(">>  ")
        try:
            date = datetime.datetime.strptime(bdate,'%m%d%Y')
            break
        except ValueError:
            print("Error: Not a valid date. Please enter date in the 'MMDDYYY' format.")
            time.sleep(2)   
    
    #INSERTING INTO DATABASE#
    insert = """INSERT into PEOPLE (SIN, NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
    values (:SIN,:NAME, :HEIGHT, :WEIGHT, :EYECOLOR, :HAIRCOLOR, :ADDR, :GENDER, TO_DATE(:BIRTHDAY,'MMDDYYYY'))"""

    cursor.execute(insert,{'SIN':sin, 'NAME':name,'HEIGHT':height, 'WEIGHT':weight, 'EYECOLOR':eye,'HAIRCOLOR':hair, 'ADDR':addr, 'GENDER':gender, 'BIRTHDAY':bdate})  
    
    connection.commit()
    title(header)
    print("Person successfully added to database!")
    time.sleep(2)
    return

def test(connStr):
    try:
        connection  = cx_Oracle.connect(connStr)
        cursor = connection.cursor() 
        connection.close() 
        return True
    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print("Error: could not connect to the database, please Re-enter your username and password")
        print( sys.stderr, "Oracle code:", error.code)
        print( sys.stderr, "Oracle message:", error.message)
        time.sleep(2)
        return False

print("starting")
time.sleep(5)

while True:
    os.system('clear')
    print("Welcome to the Driver Vehicle Registration System")
    print("Please enter your username below")
    user = input(">> ")
    os.system('clear')
    print("Welcome to the Driver Vehicle Registration System")    
    print("Please enter your password")
    pw = getpass.getpass(">> ")
    connStr=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'  
    if test(connStr): 
        print("bleh")
        time.sleep(5)
        connection  = cx_Oracle.connect(connStr)
        cursor = connection.cursor()
        main_menu()

#if __name__ == "__main__":
#    # Launch main menu           
#    main_menu()
