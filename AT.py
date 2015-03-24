import sys, os, time,cx_Oracle,mainMenu 

def main():
    os.system('clear')
    print("Auto Transaction")
    print("-----------------------------------")
    print ("1. Setup auto transaction")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def transaction():
    os.system('clear')
    print("Auto Transaction")
    print("-----------------------------------")
    while True:
        os.system('clear')
        print("Auto Transaction")
        print("-----------------------------------")
        print("Please enter the Vehicle Serial Number (VSN) of the vehicle to be sold")
        vsn = input(">> ")
        if(vsn.isdigit() and len(vsn) == 10):
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = %s" % vsn)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: vehicle no in database. Please enter another VSN")
                time.sleep(2)
            else:
                break
        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)

            
    print("Please enter the seller")
    seller = input(">> ")
    print("Please enter the vehicle");
    vehicle = input(">> ")
    print(buyer," has bought ",seller+"'s ",vehicle,"!")
    transactionAgain()
    return



def transactionAgain():
    print("----------------------------------")
    print("1.Setup another auto transaction")
    print("0. Back to main menue")
    choice = input(">> ")
    exec_menu(choice,'transactionAgain')
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
    '1':transaction,
    '0': exit,
    'transactionAgain':transactionAgain
}
