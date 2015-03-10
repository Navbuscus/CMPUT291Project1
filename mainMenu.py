import sys, os, time, cx_Oracle
import NVR,AT,DLR,VR,SE


def main():
    connect()
    main_menu()


def connect():
    user = 'ajwu'
    pw = 'a1__5LoYz'   
    connStr=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'  
    try:
        connection  = cx_Oracle.connect(connStr)
        curs = connection.cursor()
    except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print( sys.stderr, "Oracle code:", error.code)
        print( sys.stderr, "Oracle message:", error.message)


# Main menu
def main_menu():
    os.system('clear')
    
    print ("Welcome,\n")
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
            time.sleep(3)
            menu_actions['main_menu']()
    return
 
def New_Vehicle_Registration():
    NVR.main()
    #print ("New Vehicle Registration!\n")
    #print ("9. Back")
    #print ("0. Quit")
    #choice = input(" >>  ")
    #exec_menu(choice)
    back()

 
 

def Auto_Transaction():
    AT.main()
    #print ("Auto Transaction!\n")
    #print ("9. Back")
    #print ("0. Quit")
    #choice = input(" >>  ")
    #exec_menu(choice)
    back()


 # Menu 2
def Drivers_Licence_Registration():
    DLR.main()
    back()


 # Menu 2
def Violation_Record():
    VR.main()
    back()


 # Menu 2
def Search_Engine():
    SE.main()
    back()

 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
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
 
if __name__ == "__main__":
    # Launch main menu
    main()
