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
        # rand gen ticket_no
        ticket_no = random.randint(0,10000000000000)

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
        if( violator_no.isdigit() and len(violator_no) == 9):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT people.violator_no FROM people WHERE people.violator_no = %s" % violator_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another SIN")
                time.sleep(2)                
            else:
                break;
        else:
            print("Error: Please enter a valid SIN")
            time.sleep(2)
    
    while True:
        header()
        print("Please enter the Violator's vehicle serial number (VSN):")
        vehicle_no = input(">>  ")
        if( vehicle_no.isdigit() and len(vehicle_no) == 10):
            # testing for UNIQUE-KEY CONSTRAINT 
            mainMenu.cursor.execute("SELECT vehicle.vehicle_no FROM vehicle WHERE vehicle.vehicle_no = %s" % vehicle_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: Violator does not exist in the Database. Please enter another SIN")
                time.sleep(2)                
            else:
                break;
        else:
            print("Error: Please enter a valid vehicle serial number (VSN)")
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
