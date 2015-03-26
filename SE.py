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
    while True:
        header()
        print("Please enter the Driver's Licence Number (DLN):")
        licence_no = input(">>  ")
        # testing valid input       
        if( len(licence_no) <= 15):
            mainMenu.cursor.execute("SELECT drive_licence.sin FROM drive_licence WHERE drive_licence.licence_no = %s" % licence_no)
            data = mainMenu.cursor.fetchall()            
            if data is None:
                print("Error: Driver does not exist in the Database. Please enter another Licence Number.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT t.ticket_no, t.vehicle_id, t.vtype, t.vdate, t.place FROM ticket t WHERE violator_no = %s" % violator_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    VR_descript()
                    for row in data:
                        print(row)
                    print("")
                    stdin = input(">>  ")
                    if stdin == "":
                        break
                break
        else:
            print("Error: Please enter a valid Licence Number.")
            time.sleep(2)    
    
    searchAgain()    

def vrLN():
    while True:
        header()
        print("Please enter the Violator's Driver Licence Number (DLN):")
        licence_no = input(">>  ")
        # testing valid input       
        if( len(licence_no) <= 15):
            mainMenu.cursor.execute("SELECT drive_licence.sin FROM drive_licence WHERE drive_licence.licence_no = %s" % licence_no)
            violator_no = mainMenu.cursor.fetchone()
            mainMenu.cursor.execute("SELECT ticket.violator_no FROM ticket WHERE ticket.violator_no = %s" % violator_no)
            data = mainMenu.cursor.fetchone()            
            # testing for UNIQUE-KEY CONSTRAINT            
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another Licence Number.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT t.ticket_no, t.vehicle_id, t.vtype, t.vdate, t.place FROM ticket t WHERE violator_no = %s" % violator_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    VR_descript()
                    for row in data:
                        print(row)
                    print("")
                    stdin = input(">>  ")
                    if stdin == "":
                        break
                break
        else:
            print("Error: Please enter a valid Licence Number.")
            time.sleep(2)    
    
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
                print("Error: Violator does not exist in the Database. Please enter another SIN.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT t.ticket_no, t.vehicle_id, t.vtype, t.vdate, t.place FROM ticket t WHERE violator_no = %s" % violator_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    VR_descript()
                    for row in data:
                        print(row)
                    print("")
                    stdin = input(">>  ")
                    if stdin == "":
                        break
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

def VR_descript():
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
