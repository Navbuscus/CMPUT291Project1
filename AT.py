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
    while True:
        os.system('clear')
        print("Auto Transaction")
        print("-----------------------------------")
        print("Please enter the Vehicle Serial Number (VSN) of the vehicle to be sold")
        vsn = input(">> ")
        if(vsn.isdigit() and len(vsn) == 10):
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = %s", % vsn)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: vehicle no in database. Please enter another VSN")
                time.sleep(2)
            else:
                break
        else:
            print("Error: you must enter a 10 digit integer value")
            time.sleep(2)

            
    while True:
        os.system('clear')
        print("Auto Transaction")
        print("-----------------------------------")
        print("Please enter the Social Insurance Number (SIN) of the vehicle's seller")
        sSin = input(">> ")
        if(sSin.isdigit() and len(sSin) == 10):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % sSin)
            dSin = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: Seller not in database. Please enter sellers SIN")
                time.sleep(2)
            else:
                mainMenu.cursor.execute("SELECT owner_id FROM owner WHERE vehicle_id = %s", %vsn)
                owners = mainMenu.cursor.fetchall()
                for owner in owners:
                    owners.pop(owner)
                    owners.append(owner.strip())
                if dSin in owners:
                    break
                else:
                    print("Error: seller entered does not own this vehicle.")
                    

        else:
            print("Error: you must enter a 9 digit integer value")
            time.sleep(2)

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
