import sys, os, mainMenu, time, cx_Oracle, random

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
        violator_no = input(">>  ")
        # testing for correct input       
        if( violator_no.isdigit() and len(violator_no) == 9):
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
                    print("  SERIAL_NO       MAKER                MODEL                      YEAR COLOR         TYPE_ID")
                    print("  --------------- -------------------- -------------------- ---------- ---------- ----------")
                    data = mainMenu.cursor.fetchall()
                    for row in data:
                        for serial_no, maker, model, year, color, type_id in row:
                            print (">>: %15s %20s %15s %10s %10s %10s" %(serial_no, maker, model, year, color, type_id))
                    time.sleep(10)
                    break;                   
        else:
            print("Error: Please enter a valid SIN")
            time.sleep(2)
    
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

menu_actions = {
    'main':main,
    '1':ticket,
    '0': exit,
    'ticketAgain':ticketAgain
}
