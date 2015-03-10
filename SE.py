import sys, os, time, cx_Oracle,mainMenu

def main():
    os.system('clear')
    print("Search Engine")
    print("-----------------------------------")
    print ("1. Search database")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def search():
    os.system('clear')
    print("Search Engine")
    print("-----------------------------------")
    print("Please enter search term")
    driver = input(">> ")
    print(driver,"is in our database... somewhere")
    searchAgain()
    return

def searchAgain():
    print("----------------------------------")
    print("1. Search database again")
    print("0. Back to main menu")
    choice = input(">> ")
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

def exit():
    return
 

menu_actions = {
    'main':main,
    '1':search,
    '0': exit,
    'searchAgain':searchAgain
}
