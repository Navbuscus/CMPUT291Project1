import sys, os, mainMenu, time

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
    print("Please enter the buyer")
    buyer = input(">> ")
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
