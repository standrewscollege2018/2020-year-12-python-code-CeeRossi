#This program is designed so that a user can add/ delete book titles from a list of books
print("Designed and built by Caleb Rossiter")
print("Version 1")


#User login that retains usser account after program closed
welcome = input("Do you have an acount? y/n: ")
if welcome == "n":
    while True:
        username  = input("Enter a username:")
        password  = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "y"
            break
        print("Passwords do NOT match!")

elif welcome == "y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome",login1,)
            break
        print("Incorrect username or password.")
        print("Please try again")


#Main menu
    print("\n=====MENU=====")
    print("1. Display every book")
    print("2. Add a new book")
    print("3. Delete a book")
    print("4. Update a book detailst")
    print("5. Close app")
    
while True:
    
    try:
        choice = int(input("Please choose a menu option: "))
        break
    #detect integer value not entered
    except:
        #display error message
        print("Error: Your input must be a number")
        #redisplay menu so that user can see what options are
        print("\n=====MENU=====")
        print("1. Display all students")
        print("2. Add a student")
        print("3. Delete a student")
        print("4. Update a student")
        print("5. Quit program\n")       


if choice ==1 :
    print("This Works")

elif choice ==2 :
    print("This Works")

elif choice ==3 :
    print("This Works")

elif choice ==4 :
    print("This Works")
        
#exit program
elif choice ==5:
    display_menu = False
    

#invalid menu
else:
    print("invalid menu choice")


