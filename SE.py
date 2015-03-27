import sys, os, time, cx_Oracle, mainMenu

def main():
    header()
    options()
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def driverName():
    while True:
        header()
        print("Please enter the Driver's Name:")
        name = input(">>  ")
        # testing valid input       
        if( len(name) <= 40):
            print("This is the name: %s" %name)
            mainMenu.cursor.execute("SELECT d.licence_no FROM drive_licence d, people p WHERE p.sin = d.sin AND p.name = %s" % str(name))
            data = mainMenu.cursor.fetchall()            
            if data is None:
                print("Error: Person cannot be found in the Database. Please enter another Name.")
                time.sleep(2)                
            else:
                driver_descript()
                for unique_licence_no in data:
                    mainMenu.cursor.execute("SELECT DISTINCT p.name, d.licence_no, p.addr, p.birthday, d.class, c.description, d.expiring_date FROM drive_licence d, people p, restriction r, driving_condition c WHERE d.licence_no = %s AND p.sin = d.sin AND r.licence_no = d.licence_no AND r.r_id = c.c_id" % unique_licence_no)
                    data = mainMenu.cursor.fetchall()
                    for row in data:
                        print(row)
                        
                while True:
                    print("")
                    stdin = input(">>  ")
                    if stdin == "":
                        break
                break
        else:
            print("Error: Person's name cannot exceed 40 characters. Please try another Name.")
            time.sleep(2)    
    
    searchAgain()    

    
def driverLN():
    while True:
        header()
        print("Please enter the Driver's Licence Number (DLN):")
        licence_no = input(">>  ")
        # testing valid input       
        if( len(licence_no) <= 15):
            mainMenu.cursor.execute("SELECT licence_no FROM drive_licence WHERE licence_no = %s" % licence_no)
            data = mainMenu.cursor.fetchall()            
            if data is None:
                print("Error: Person is not a registered Driver. Please enter another Licence Number.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT DISTINCT p.name, d.licence_no, p.addr, p.birthday, d.class, c.description, d.expiring_date FROM drive_licence d, people p, restriction r, driving_condition c WHERE d.licence_no = %s AND p.sin = d.sin AND r.licence_no = d.licence_no AND r.r_id = c.c_id" % licence_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    driver_descript()
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

def driver_descript():
    header()
    print("Press the 'Enter' key when you're done with your Search session.")                            
    print(" ")
    print("  DRIVER    DESCRIPTION ")
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
