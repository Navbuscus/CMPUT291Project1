import sys, os, time,cx_Oracle,mainMenu, random, datetime 

def title():
    os.system('clear')
    print("Auto Transaction")
    print("-----------------------------------")

def main():
    title()
    print ("1. Setup auto transaction")
    print ("0. Back")
    choice = input(" >>  ")
    exec_menu(choice, 'main')
    return

def transaction():
    while True:
        t_id = random.randint(100000000,999999999) 
        mainMenu.cursor.execute("SELECT transaction_id FROM auto_sale WHERE transaction_id = %d" %t_id)
        result = mainMenu.cursor.fetchone()
        if result is None:
            break
    print("Transaction ID: "+t_id)
    time.sleep(2)
    while True:
        title()
        print("Please enter the Vehicle Serial Number (VSN) of the vehicle to be sold")
        vsn = input(">> ").strip()
        if(1 <= len(vsn) <= 15):
            mainMenu.cursor.execute("SELECT serial_no FROM vehicle WHERE serial_no = %s" % vsn)
            data = mainMenu.cursor.fetchone()
            if data is None:
                print("Error: vehicle no in database. Please enter another VSN")
                time.sleep(2)
            else:
                break
        else:
            print("Error: Invalid input. Min 1 character MAX 15 characters")
            time.sleep(2)
            
    while True:
        title()
        print("Please enter the Social Insurance Number (SIN) of the vehicle's seller")
        sSin = input(">> ").strip()
        if(1 <= len(sSin) <= 15):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % sSin)
            dSin = mainMenu.cursor.fetchone()
            if dSin is None:
                print("Error: Seller not in database. Please entera different SIN")
                time.sleep(2)
            else:
                mainMenu.cursor.execute("SELECT owner_id FROM owner WHERE vehicle_id = %s" % vsn)
                owners = mainMenu.cursor.fetchall()
                if dSin in owners:
                    break
                else:
                    print("Error: seller entered does not own this vehicle.")
                    time.sleep(2)

        else:
            print("Error: Invalid input. Min 1 character MAX 15 characters")
            time.sleep(2)
        
    while True:
        title()
        print("Please enter the Social Insurance Number (SIN) of the vehicle's primary buyer")
        bSin = input(">> ").strip()
        if(1 <= len(bSin) <= 15):
            mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % bSin)
            data = mainMenu.cursor.fetchone()
            if data is None:
                while True:
                    title()
                    print("Error: Buyer not in database. Would you like to add them? (Y/N):")
                    choice = input(">> ")
                    if choice.lower() == "y":
                        mainMenu.registerPerson("Auto Transaction")
                        print("Please Re-enter buyer's sin")
                        time.sleep(2)
                        break
                    elif choice.lower() == "n":
                        print("Please enter new SIN")
                        time.sleep(2)
                        break
                    else:
                        print("Error: Invalid choice")
                        time.sleep(2)
            else:
                break
        else:
            print("Error: Invalid input. MIN 1 character MAX 15 characters")
            time.sleep(2)

    sSin = "null"
    while True:
        title()
        print("Would you like to add a secondary buyer? (Y/N):")
        choice = input(">> ").lower()
        if choice == 'y': 
            while True:
                title()
                print("Please enter the Social Insurance Number (SIN) of the vehicle's secondayy buyer")
                sSin = input(">> ").strip()
                if(1 <= len(sSin) <= 15):
                    mainMenu.cursor.execute("SELECT sin FROM people WHERE sin = %s" % sSin)
                    data = mainMenu.cursor.fetchone()
                    if data is None:
                        while True:
                            title()
                            print("Error: Buyer not in database. Would you like to add them? (Y/N):")
                            choice = input(">> ")
                            if choice.lower() == "y":
                                mainMenu.registerPerson("Auto Transaction")
                                print("Please Re-enter buyer's sin")
                                time.sleep(2)
                                break
                            elif choice.lower() == "n":
                                print("Please enter new SIN")
                                time.sleep(2)
                                break
                            else:
                                print("Error: Invalid choice")
                                time.sleep(2)
                    else:
                        break
                else:
                    print("Error: Input invalid. MIN 1 character  MAX 15 characters")
                    time.sleep(2)
            break
        elif choice == 'n':
            break
        else:
            print("Error: Invalid input")


    while True:
        title()
        print("Please enter the price (CAD): ")
        price = input(">> ").strip()
        try:
            float(price)
            if( 0 <= float(price) <= 9999999.99):
                break;
            else:
                print("Error: value too large")
                time.sleep(2)
        except ValueError:
            print("Error: please enter a number")
            time.sleep(2)


    while True:
        title()
        print("Please enter transaction date (MMDDYYYY):")
        bdate = input(">>  ").strip()
        try:
            date = datetime.datetime.strptime(bdate,'%m%d%Y')
            break
        except ValueError:
            print("Error: Not a valid date. Please enter date in the 'MMDDYYY' format.")
            time.sleep(2)   
    

    mainMenu.cursor.execute("delete from owner where vehicle_id = %s"%vsn)

    insert = """INSERT into OWNER (OWNER_ID, VEHICLE_ID, IS_PRIMARY_OWNER)  values (:OWNER_ID,:VEHICLE_ID,'y')"""
    mainMenu.cursor.execute(insert,{'OWNER_ID':bSin,'VEHICLE_ID':vsn})


    if sSin != "null":
        insert = """INSERT into OWNER (OWNER_ID, VEHICLE_ID, IS_PRIMARY_OWNER)  values (:OWNER_ID,:VEHICLE_ID,'n')"""
        mainMenu.cursor.execute(insert,{'OWNER_ID':sSin,'VEHICLE_ID':vsn}) 


    insert = """INSERT into AUTO_SALE (TRANSACTION_ID, SELLER_ID, BUYER_ID,VEHICLE_ID, S_DATE, PRICE)
    values (:TRANSACTION_ID, :SELLER_ID, :BUYER_ID,:VEHICLE_ID, TO_DATE(:S_DATE, 'MMDDYYYY'), :PRICE:TRANS)"""
    mainMenu.cursor.execute(insert,{'TRANSACTION_ID':t_id, 'SELLER_ID':sSin , 'BUYER_ID':bSin,'VEHICLE_ID':vsn, 'S_DATE':date, 'PRICE':price})  
    
    mainMenu.connection.commit()  

    transactionAgain()
    return

def transactionAgain():
    title()
    print(" Sale completed!")
    time.sleep(2)
    main()

def exec_menu(choice,context):
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
