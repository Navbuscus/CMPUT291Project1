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
            mainMenu.cursor.execute("SELECT p.name FROM drive_licence d, people p WHERE p.sin = d.sin AND  p.name = '%s'" %name)
            data = mainMenu.cursor.fetchone()            
            if data is None:
                print("Error: Person cannot be found in the Database. Please enter another Name.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT d.licence_no FROM drive_licence d, people p WHERE p.sin = d.sin AND  p.name = '%s'" %name)
                data = mainMenu.cursor.fetchall()                   
                descript()
                for unique_licence_no in data:
                    mainMenu.cursor.execute("SELECT DISTINCT p.name, d.licence_no, p.addr, p.birthday, d.class, c.description, d.expiring_date FROM drive_licence d, people p, restriction r, driving_condition c WHERE d.licence_no = '%s' AND p.sin = d.sin AND r.licence_no = d.licence_no AND r.r_id = c.c_id" % unique_licence_no)
                    data = mainMenu.cursor.fetchall()
                    for row in data:
                        print("*  Name: %s, Licence No: %s, Address: %s, Birthday: %s, Type: %s, Description: %s, Expiry Date: %s"%(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strftime("%b-%d-%Y"),row[4], row[5], row[6].strftime("%b-%d-%Y")))
                        
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
            mainMenu.cursor.execute("SELECT licence_no FROM drive_licence WHERE licence_no = '%s'" % licence_no)
            data = mainMenu.cursor.fetchone()            
            if data is None:
                print("Error: Driver's Licence not registered in the database. Please enter another Licence Number.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT DISTINCT p.name, d.licence_no, p.addr, p.birthday, d.class, c.description, d.expiring_date FROM drive_licence d, people p, restriction r, driving_condition c WHERE d.licence_no = %s AND p.sin = d.sin AND r.licence_no = d.licence_no AND r.r_id = c.c_id" % licence_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    descript()
                    for row in data:
                        print("*  Name: %s, Licence No: %s, Address: %s, Birthday: %s, %s, Description: Type: %s, Expiry Date: %s"%(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strftime("%b-%d-%Y"),row[4], row[5], row[6].strftime("%b-%d-%Y")))
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
            mainMenu.cursor.execute("SELECT drive_licence.sin FROM drive_licence WHERE drive_licence.licence_no = '%s'" % licence_no)
            violator_no = mainMenu.cursor.fetchone()
            mainMenu.cursor.execute("SELECT ticket.violator_no FROM ticket WHERE ticket.violator_no = '%s'" % violator_no)
            data = mainMenu.cursor.fetchone()            
            # testing for UNIQUE-KEY CONSTRAINT            
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another Licence Number.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT t.ticket_no, t.vehicle_id, t.vtype,  tt.fine, t.vdate, t.place FROM ticket t, ticket_type tt WHERE violator_no = %s AND tt.vtype = t.vtype " % violator_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    descript()
                    for row in data:
                        print("*  Ticket Number: %d, VSN: %s, Violation Type: %s, Fine: $%.2f, Date: %s, Description: %s"%(row[0], row[1].strip(), row[2].strip(), float(row[3]), row[4].strftime("%b-%d-%Y"),row[5]))
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
            mainMenu.cursor.execute("SELECT ticket.violator_no FROM ticket WHERE ticket.violator_no = '%s'" % violator_no)
            data = mainMenu.cursor.fetchone()
            # testing for UNIQUE-KEY CONSTRAINT            
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another SIN.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT t.ticket_no, t.vehicle_id, t.vtype,  tt.fine, t.vdate, t.place FROM ticket t, ticket_type tt WHERE violator_no = %s AND tt.vtype = t.vtype " % violator_no)
                data = mainMenu.cursor.fetchall()
                while True:
                    descript()
                    for row in data:
                        print("*  Ticket Number: %d, VSN: %s, Violation Type: %s, Fine: $%.2f, Date: %s, Description: %s"%(row[0], row[1].strip(), row[2].strip(), float(row[3]), row[4].strftime("%b-%d-%Y"),row[5]))                        
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
    while True:
        header()
        print("Please enter the Vehicle Serial Number (VSN):")
        vehicle_id = input(">>  ")
        # testing valid input       
        if( len(vehicle_id) <= 15):
            mainMenu.cursor.execute("SELECT vehicle_id FROM ticket WHERE vehicle_id = '%s'" % vehicle_id)
            data = mainMenu.cursor.fetchone()
            # testing for UNIQUE-KEY CONSTRAINT            
            if data is None:
                print("Error: Vehicle does not exist in the Database. Please enter another VSN.")
                time.sleep(2)                
            else:
                mainMenu.cursor.execute("SELECT COUNT(a.vehicle_id), AVG(a.price) FROM auto_sale a WHERE vehicle_id = %s" %vehicle_id)
                data1 = mainMenu.cursor.fetchall()
                mainMenu.cursor.execute("SELECT COUNT(t.vehicle_id) FROM ticket t WHERE vehicle_id = %s" %vehicle_id)
                data2 = mainMenu.cursor.fetchall()   
                data1.extend(data2)
                while True:
                    descript()
                    print("*  Handed-Over: %d, Average Price: $%.2f, Number of Violations: %d"%(data1[0][0], float(data1[0][1]), data1[1][0]))
                    print("")
                    stdin = input(">>  ")
                    if stdin == "":
                        break                
                break
        else:
            print("Error: Please enter a valid Vehicle Serial Number (VSN).")
            time.sleep(2)    
    
    searchAgain()   
    
def searchAgain():
    header()
    print ("1. Return to Search Menu.")
    print ("0. Back.")
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
    print ("0. Back.")     

def descript():
    header()
    print("Press the 'Enter' key when you're done with your Search session.")                            
    print(" ")
    print("   SEARCH RESULTS ")
    print("   --------------")    
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
