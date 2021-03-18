from datetime import date
import datetime
import time
import collections.abc
import random
import sys

#Text based program representing the features that will be utilized in the final inventory management application.
#Features include storing all products while being able to show them in a table, updating the current inventory by 
#adding or subtracting from the total amount, adding a completely new item or deleting an item, focusing on the name
#of the product and it's lot expiration to better keep track of reagents that are due to expire, and user settings features
#that include adding new users and updating user info. 

#@author Michael Yarussi
#@version 1


#dictionary containing total inventory and all of it's associated product infomation.
dict_inventory = {
1: {"Name": "Gloves", "Manufacturer": "NA", "Order ID": "PHGLOVLG", "Amount in stock": 20, "Par": 2, "Lot Number": "123456", "Lot Expiration": datetime.date(2023, 3, 5)}, 
2: {"Name": "BacT Bottles", "Manufacturer": "Biomerieux", "Order ID": "NA", "Amount in stock": 2, "Par": 3, "Lot Number":"789456", "Lot Expiration": datetime.date(2021, 5, 26)}, 
3: {"Name": "pH Buffer 10", "Manufacturer" : "ThermoScientific", "Order ID": "NA", "Amount in stock": 10, "Par":10, "Lot Number": "35678", "Lot Expiration": datetime.date(2020, 3, 14)}
}

#dictionary used for storing information about user history(what they have done in the program when logged in)
dict_tracking = {"User Name" : "" , "Action" : "", "Item": "", "Date and Time": ""}

#dictionary used to store username information
dict_usernames = {"Michael" : "password", "Natalie" : "secret", "Shelby": "passcode"}

#method to reprsent a main menu page
def menu():
    print("-------------------------------------")
    print("Product QC Inventory List")
    print("-------------------------------------")
    print("1.Show All Products")
    print("2.Take Item")
    print("3.Add Item to Stock")
    print("4.Add New Item")
    print("5.Remove Item from Inventory")
    print("6.Lot Numbers and their expirations")
    print("7.User and Account Settings")
    print("8.User History")
    print("9.Exit the program")
    print("-------------------------------------")

#method to represent settings menu page
def settings_menu():
    print('-------------------------------------')
    print("\tUser and Account Settings")
    print('-------------------------------------')
    print("1.Add User")
    print('2.Update Username and Password')
    print('3.Delete User')
    print('4.Return to main menu')
    print('-------------------------------------')

#method used to print all the items in the inventory dictionary
def display_all():
    print("-------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\tInventory List")
    print("-------------------------------------------------------------------------------------------------------")
    for k, v in dict_inventory.items():
        print(k,v)
    print("-------------------------------------------------------------------------------------------------------")

#method used to print all the items in the username dictionary
def display_usernames():
    print("-----------------------------------------")
    print("\tUsernames and Passwords")
    print("-----------------------------------------")
    for k, v in dict_usernames.items():
        print(k,v)
    print("-----------------------------------------")

#method used to print all the user tracking info in the tracking dictionary
def display_userTracking():
    print("-----------------------------------------")
    print("\tRecent User History")
    print("-----------------------------------------")
    for k, v in dict_tracking.items():
        print(k,v)
    print("-----------------------------------------")
def get_exp(d):
    return dict_inventory[d]["Lot Expiration"]


login = input("Username: ")
log_pass = input("Password: ")

#login to get into the program. You can use Michael as username and password as the password.
if login in dict_usernames:
    if log_pass == dict_usernames[login]:     

        while(True):
            menu()
            choice = int(input("What would you like to do?: "))

#Shows all products in stock
            if choice == 1:
                display_all()
#Allows user to take an item from stock
            elif choice == 2:
                now = date.today()
                item_taken = input("Which item was taken from stock?: ")
                #Product id is the key associated with each product (ie: 1, 2 or 3)
                product_id = int(input("What is the product id?: "))
                if product_id in dict_inventory:
                    user_int = int(input(f"How many {item_taken} were taken from stock?: "))
                    dict_inventory[product_id]["Amount in stock"] -= user_int
                    print(f'You have successfully taken {user_int} {item_taken} from stock!')
                    dict_trackingTake = {"User Name: " : login, "Action: " : f"Withdrew {user_int}", "Item: " : item_taken, "Date and Time: " : now.strftime("%y-%m-%d %H:%M:%S")}
                    dict_tracking.update(dict_trackingTake)

                else:
                    print(f"{item_taken} not found in inventory.")
#Allows user to add an item to the stock
            elif choice == 3:
                item_placed = input("Which item would you like to add to stock?: ")
                product_id = int(input("What is the product id?: "))
                if product_id in dict_inventory:
                    user_int = int(input(f"How many {item_placed} were added to stock?: "))
                    dict_inventory[product_id]["Amount in stock"] += user_int
                    print(f"You have successfully placed {str(user_int)}  {item_placed} into stock!")
                else:
                    print(f"{item_placed} not found in inventory.")
#Allows the user to add a new item to the inventory list
            elif choice == 4:
                name = input("Enter your userame: ")
                for k in dict_usernames:
                    if name in dict_usernames:
                        user_pass = input("Enter your password: ")
                    if user_pass == dict_usernames[name]:
                        value = (random.randint(1,100))
                        NewItem = input("Which item would you like to add?: ")
                        Manu = input("Who is the manufacturer?: ")
                        OrdId = input("What is the order ID?: ")
                        AmtStock = input("How many would you like to add?: ")
                        AmtPar = input("What is the desired amount you would like to keep in stock?: ")
                        LotNum = input("What is the product's Lot Number?: ")
                        date_entry = input("Enter a date in YYYY-MM-DD format: ")
                        year, month, day = map(int, date_entry.split('-'))
                        LotExp = datetime.date(year, month, day)
                        dict_newItem = {value: {"Name": NewItem, "Manufacturer": Manu, "Order ID": OrdId, "Amount in Stock": AmtStock, "Par": AmtPar, "Lot Number": LotNum, "Lot Expiration": LotExp}}
                        dict_inventory.update(dict_newItem)
                        print(f"You have successfully added {NewItem} into the inventory list!")
                        break
                    else:
                        print("Incorrect password entered.")
#Allows user to delete a product from the inventory list
            elif choice == 5:
                user_input = input("Which item would you like to delete?: ")
                dict_inventory.pop(user_input)
                print (f"{user_input} has been successfully deleted.")
#Allows user to see list of items and their experation. Have ability to search by product name and organize into sorted list based on expiration date. 
            elif choice == 6:
                for key in sorted(dict_inventory, key = get_exp):
                    lot_num = dict_inventory[key]["Lot Number"]
                    exp_date = dict_inventory[key]["Lot Expiration"]
                    print(f'Item ID {key!r} : {dict_inventory[key]["Name"]}, with lot number {lot_num} will expire on {exp_date}')
#Access user settings
            elif choice == 7:
                while(True):
                    settings_menu()
                    option = int(input("What would you like to do?: "))
    #Makes new user        
                    if option == 1:
                        new_username = (input("Enter username: "))
                        if new_username not in dict_usernames:
                            print("Username Accepted")
                            new_password = input("Enter password: ")
                        else:
                            print("Username already taken")                   
                            settings_menu()
    #Updates username and password        
                    elif option == 2:
                        display_usernames()
                        old_username = (input("Which username would you like to update?: "))
                        old_password = (input("Password: "))
                        if old_username in dict_usernames:
                            if old_password == dict_usernames[old_username]:
                                update_password = (input("What is the new password?: "))
                                dict_updatePass = {old_username : update_password}
                                dict_usernames.update(dict_updatePass)
                                print("Username and Password successfully updated")
                            else:
                                print("Incorrect Password")            
                    elif option == 3:
                        display_usernames()
                        delete_user = (input('Which user would you like to delete?: '))
                        delete_pass = (input('Password: '))
                        if delete_user in dict_usernames:
                            if delete_pass == dict_usernames[delete_user]:
                                dict_usernames.pop(delete_user)
                                print("User deleted")                
    #Back to main menu        
                    elif option == 4:
                        break
                    else:
                        print("Ivalid entry")

#Prints All user tracking info
            elif choice == 8:
                display_userTracking()

#Closes the program    
            elif choice == 9:
                print("Program will now close")
                break

            else:
                print("Invalid entry")
                break
    else:
        print("Incorrect Username or Password")
