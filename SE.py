import sys, os, time, cx_Oracle, mainMenu

def main():
    header()
    options()
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def driverName():
    header()
    print ("Please enter the Driver's Name.") 
    name = input(">>  ") 
    searchAgain()
    
def driverLN():
    header()
    print ("Please enter the Driver's Licence Numbr (DLN).") 
    licence_no = input(">>  ") 
    searchAgain() 

def vrLN():
    header()
    print ("Please enter the Driver's Licence Number (DLN).") 
    licence_no = input(">>  ") 
    searchAgain()  

def vrSIN():
    while True:
        header()
        print("Please enter the Violator's SIN:")
        violator_no = input(">>  ")
        # testing valid input       
        if( violator_no.isdigit() and len(violator_no) == 9):
            mainMenu.cursor.execute("SELECT ticket.violator_no FROM ticket WHERE ticket.violator_no = %s" % violator_no)
            data = mainMenu.cursor.fetchone()
            # testing for UNIQUE-KEY CONSTRAINT            
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another SIN")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT * FROM ticket WHERE violator_no = %s" % violator_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    driverName_descript()
                    for row in data:
                        print(row)
                    print("")
                    stdin = input(">>  ")
                    break
        else:
            print("Error: Please enter a valid SIN")
            time.sleep(2)    
    
    searchAgain()   

def vVSN():
    header()
    print ("Please enter the Vehicle Serial Number (VSN).") 
    licence_no = input(">>  ") 
    searchAgain()     
    
def searchAgain():
    header()
    print ("1. Return to Search Menu.")
    print ("0. Exit.")
    choice = input(">> ")
    if choice == "1":
        choice = "main"
    exec_menu(choice,'searchAgain')
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

def header():
    os.system('clear')
    print("Search Engine")
    print("-----------------------------------")

def options():
    print ("1. Search Driver by Name.")
    print ("2. Search Driver by Licence Number (DLN).")
    print ("3. Search Violation Record by Licence Number (DLN).")
    print ("4. Search Violation Record by SIN.")
    print ("5. Search Vehicle History by Vehicle Serial No (VSN).")   
    print ("")
    print ("0. Exit.")     

def driverName_descript():
    header()
    print("Press the 'Enter' key when you're done with your Search session.")                            
    print(" ")
    print("  VIOLATION DESCRIPTION ")
    print("  --------- --------------------")    
    return

                
def exit():
    return

menu_actions = {
    'main':main,
    '1':driverName,
    '2':driverLN,
    '3':vrLN,
    '4':vrSIN,
    '5': vVSN,
    '0': exit,
    'searchAgain':searchAgain
}
