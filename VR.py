import sys, os, mainMenu, time, cx_Oracle, random, datetime

def main():
    header()
    print ("1. Issue ticket")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def ticket():   
    
    while True:
        header()        
        # rand gen 9-digit ticket_no
        ticket_no = random.randint(100000000,1000000000)

        # testing for UNIQUE-KEY CONSTRAINT 
        mainMenu.cursor.execute("SELECT ticket.ticket_no FROM ticket WHERE ticket.ticket_no = %d" % ticket_no)
        data = mainMenu.cursor.fetchone()
        if data is None:
            print ("Your ticket_no: %d" % ticket_no)   
            time.sleep(2)
            break;
        
    while True:
        header()
        print("Please enter the Violator's SIN:")
        violator_no = input(">>  ").strip()
        # testing valid input       
        if(1 <= len(violator_no) <= 15):
            mainMenu.cursor.execute("SELECT people.sin FROM people WHERE people.sin = %s" % violator_no)
            data = mainMenu.cursor.fetchone()
            # testing for UNIQUE-KEY CONSTRAINT            
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another SIN")
                time.sleep(2)                
            else:   
                # testing if owns car
                mainMenu.cursor.execute("SELECT v.serial_no FROM people p, owner o, vehicle v WHERE p.sin = o.owner_id AND o.vehicle_id = v.serial_no AND p.sin = %s" % violator_no)
                data = mainMenu.cursor.fetchone()
                if data is None:
                    print("Error: Violator does not own a Vehicle.")
                    time.sleep(2)                
                else:
                    mainMenu.cursor.execute("SELECT v.serial_no, v.maker, v.model, v.year, v.color, v.type_id FROM people p, owner o, vehicle v WHERE p.sin = o.owner_id AND o.vehicle_id = v.serial_no AND p.sin = %s" % violator_no)
                    data = mainMenu.cursor.fetchall()
                    
                    while True:
                        vehic_descript() 
                        serialNo_lst = []                    
                        for row in data:
                            print (">>  %s %s %s %d %s %d" %(row[0].strip(), row[1].strip(), row[2].strip(), row[3], row[4].strip(), row[5]))                        
                            serialNo_lst.append(row[0].strip())
                        
                        print("")
                        vehicle_id = input(">>  ")
                        if str(vehicle_id) not in (serialNo_lst):
                            print("Error: Please enter a Valid vehicle serial no. (VSN) as shown above")
                            time.sleep(2)
                        else:
                            break;
                    break;                   
        else:
            print("Error: Invalid input. MIN 1 character MAX 15 characters")
            time.sleep(2)
            
    while True:
        header()
        print("Please enter the Officer's SIN:")
        office_no = input(">>  ").strip()   
        # testing valid input               
        if(1 <= len(office_no) <= 15):
            if ( office_no == violator_no):
                print("Error: Officer cannot be a Violator.")
                time.sleep(2)
            else:
                mainMenu.cursor.execute("SELECT people.sin FROM people WHERE people.sin = %s" % office_no)
                data = mainMenu.cursor.fetchone()  
                if data is None:
                    print("Error: Officer does not exist in the Database. Please enter another SIN.")
                    time.sleep(2)                
                else:          
                    break;
        else:
            print("Error: Invalid input. MIN 1 character MAX 15 characters")
            time.sleep(2)            
     
    while True:
        mainMenu.cursor.execute("SELECT * FROM ticket_type")
        data = mainMenu.cursor.fetchall()             
        ticket_descript()
        ticket_lst = []                    
        for row in data:
            print (">> %10s $%.2f" %(row[0].strip(), row[1]))                        
            ticket_lst.append(row[0].strip())        
        print("")
        vtype = input(">>  ")
        if str(vtype) not in (ticket_lst):
            print("Error: Please enter a Valid Ticket as shown above")
            time.sleep(2)
        else:
            break;           
     
    while True:
        header()
        print("Please enter the Violation date (MMDDYYYY):")
        vdate = input(">>  ").strip()   
        if( validate(vdate) and vdate.isdigit() and len(vdate)):
            break
    
    while True:
        header()
        print("Please enter the Violation place (20 characters limit):")
        place = input(">>  ").strip()
        if(1 <= len(place)<= 20):
            break
        else:
            print("Error: Exceeds 20 characters, please try again.")
            time.sleep(2)
     
    while True:
        header()
        print("Please enter a description of the Violation (1024 characters limit):")
        descriptions = input(">>  ")   
        if( len(place)<= 1024):
            break
        else:
            print("Error: Exceeds 1024 characters, please try again.")
            time.sleep(2)
    
    insert = """INSERT into TICKET (TICKET_NO, VIOLATOR_NO, VEHICLE_ID, OFFICE_NO, VTYPE, VDATE, PLACE, DESCRIPTIONS)
    values (:TICKET_NO,:VIOLATOR_NO, :VEHICLE_ID, :OFFICE_NO, :VTYPE, TO_DATE(:VDATE,'MMDDYYYY'), :PLACE, :DESCRIPTIONS)"""
    mainMenu.cursor.execute(insert,{'TICKET_NO':ticket_no, 'VIOLATOR_NO':violator_no,'VEHICLE_ID':vehicle_id, 'OFFICE_NO':office_no, 'VTYPE':vtype,'VDATE':vdate, 'PLACE':place, 'DESCRIPTIONS':descriptions})  
    
    mainMenu.connection.commit()        
    
    ticketAgain()
    return

def ticketAgain():
    header()
    print("1. Issue another ticket")
    print("0. Back to main menu")
    choice = input(">> ")
    exec_menu(choice,'ticketAgain')
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

def exit():
    return
 
def header():
    os.system('clear')
    print("Violation Record")
    print("Issuing a traffic ticket and Recording Violation")
    print("-----------------------------------")  
    return

def vehic_descript():
    header()
    print("Please Select 1 of the following vehicle serial numbers (VSN) below:")                            
    print(" ")
    print("  SERIAL_NO DESCRIPTION ")
    print("  --------- --------------------")    
    return

def ticket_descript():
    header()
    print("Please Select 1 of the following Tickets below:")                            
    print(" ")
    print("   TICKET_NO  FINE ")
    print("   ---------- -----")    
    return

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%m%d%Y')
        return True
    except ValueError:
        print ("Error: Incorrect date format, should be (MMDDYYY)")
        time.sleep(2)

menu_actions = {
    'main':main,
    '1':ticket,
    '0': exit,
    'ticketAgain':ticketAgain
}
