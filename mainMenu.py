import sys, os, time, cx_Oracle
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
    os.system('clear')
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
    print("works inside ")
    NVR.main()
    back()
    
def Auto_Transaction():
    print("works inside ")
    AT.main()
    back()
    
def Drivers_Licence_Registration():
    print("works inside ")
    DLR.main()
    back()

def Violation_Record():
    print("works inside ")
    VR.main()
    back()

def Search_Engine():
    print("works inside ")
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

user = 'ajwu'
pw = 'a1__5LoYz'   

# modified portnumber
connStr=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'  

try:
    connection  = cx_Oracle.connect(connStr)
    cursor = connection.cursor() 
except cx_Oracle.DatabaseError as exc:
    error, = exc.args
    print( sys.stderr, "Oracle code:", error.code)
    print( sys.stderr, "Oracle message:", error.message)
    sys.exit()

if __name__ == "__main__":
    # Launch main menu
    main_menu()
