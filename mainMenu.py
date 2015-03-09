import sys, os, time, getpass
import NVR,AT,DLR,VR,SE

# Main menu
def main():
    os.system('clear')
    print("Welcome to ARS!")
    print ("1. login")
    print ("0. exit")
    choice = input(">> ")
    if choice == '1':
        login()
    if choice == '0':
        exit()
    print("Invalid selection, please try again.\n")
    main()
    
def login():
    os.system('clear')
    print("Please enter your username")
    username = input(">> ")
    os.system('clear')
    print("Please enter your password")
    password = getpass.getpass(prompt=">> ")
    connect(username, password)


def main_menu():
    os.system('clear')
    
    print ("Welcome,\n")
    print ("Please choose the menu you want to start:")
    print ("1. New Vehicle Registration")
    print ("2. Auto Transaction")
    print ("3. Driver Licence Registration")
    print ("4. Violation Record")
    print ("5. Search Engine")
    print ("\n0. Logout")
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
    sys.exit()

def connect(username,password):
    #here we connec to database
    if username != 'admin' or password != '1234' :
        print("Error wrong username/password")
        main()
    print( "Welcome",username+"!")
    main_menu()
    main()
    




 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': New_Vehicle_Registration,
    '2': Auto_Transaction,
    '3': Drivers_Licence_Registration,
    '4': Violation_Record,
    '5': Search_Engine,
    '9': back,
    '0': main,
}
 
if __name__ == "__main__":
    # Launch main menu
    main()
