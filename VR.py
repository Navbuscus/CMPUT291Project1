import sys, os, mainMenu, time, cx_Oracle

def main():
    os.system('clear')
    print("Violation Record")
    print("Issuing a traffic ticket and Recording Violation")
    print("-----------------------------------")
    print ("1. Issue ticket")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def ticket():

    while True:
        os.system('clear')
        print("Violation Record")
        print("Issuing a traffic ticket and Recording Violation")
        print("-----------------------------------")
        print("Please enter the Ticket Number (TN):")
        ticket_no = input(">>  ")
        if( ticket_no.isdigit()):
            # testing for UNIQUE-KEY CONSTRAINT 
            ticket_no = int(ticket_no)
            mainMenu.cursor.execute("SELECT ticket.ticket_no FROM ticket WHERE ticket.ticket_no = %d" % ticket_no)
            data = mainMenu.cursor.fetchone()
            if data is None:
                break;
            else:
                print("TN: %d, already exists in the DB!"% ticket_no)   
                time.sleep(2)
        else:
            print("Error: you must enter an integer value")
            time.sleep(2)

    os.system('clear')
    print("Violation Record")
    print("Issuing a traffic ticket and Recording Violation")
    print("-----------------------------------")
    print("Please enter the drivers name")
    driver = input(">> ")
    print(driver,"has been given a ticket, OH SNAP!")
    ticketAgain()
    return

def ticketAgain():
    print("----------------------------------")
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
 

menu_actions = {
    'main':main,
    '1':ticket,
    '0': exit,
    'ticketAgain':ticketAgain
}
