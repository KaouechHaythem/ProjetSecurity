from register import *
from login import *
def menu():
    print("tap 1 to register")
    print("tap 2 to login")
    print("tap 3 to exit")
    while True :
        choice = input("enter your choice: ")
        i=1
        if (choice== '1'):
            register()
            break
        elif (choice== '2'): 
            login()
            break
        elif(choice == '3'):
            quit()
    
               
        else :
            print("Please enter a valid choice")

menu()

