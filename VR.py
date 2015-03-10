import sys, os, mainMenu, time, cx_Oracle

def main():
    os.system('clear')
    print("Violation Record")
    print("-----------------------------------")
    print ("1. Issue ticket")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def ticket():
    os.system('clear')
    print("Violation Record")
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
