   # Da plan:
'''
list of books
welcome message
ask user for input
 > ask user for book
 | add to list
 | remove from list
 | show amount in list
 | success message
 | if "show"
 \ print out list
'''

Book_list = []
Removed_list = []
Library = []
No_option_attempts = 0

# list of books


# welcome message
print("Welcome to Book Nook!")

print("       ______ ______       ")
print("     _/      Y      \_     ")
print("   / / ~Book | ~~ ~  \ \   ")
print("  / / ~ ~ ~~ |  Nook~ \ \  ")
print(" / /________.|.________\ \ ")
print(" \ \--------`-'--------/ / ")

while True:
    # ask user for input
    print("Menu:") 
    print(" get help (help)")
    print(" Add book to list (add)")
    print(" Remove book from list (remove) ")
    print(" Show current inventory count (count) ")
    print(" Show books in your current inventory (show) ")
    print(" clear all from inventory (reset) ")
    print(" Quit program (q)")
    User_input = (input("enter an option: ", ))

    # inform user (help)
    if User_input == "help":
        print("well to summarize everything: ")
        print("Basics: simply enter any of the options from the menu with your keyboard to perfor that action")
        print("Well, everything: the function of each one is displayed next to it")
    
    # ask user for book (add)
    if User_input == "add":
        No_option_attempts = 0
        New_book = (input("what book would you like to add?: ", ))
    # add to list
        Book_list.append(New_book)
        print(Book_list)
    # success message
        print(New_book, "was added")

    # remove from list (remove)
    elif User_input == "remove":
        No_option_attempts = 0
        Remove_book = (input("what book would you like to remove?: ", ))
        Book_list.remove(Remove_book)
        Removed_list.append(Remove_book)
    # success message
        print(Remove_book, "was removed")

    # show amount in list (count)
    elif User_input == "count":
        No_option_attempts = 0
        print("as of now, you have", len(Book_list), "in your list")
        if len(Book_list) >= 10 and len(Book_list) <= 20:
            print("as of now, you have", len(Book_list), "in your list, thats a lot")
        if len(Book_list) >= 20 and len(Book_list) <= 30:
            print("as of now you have...", len(Book_list), "which is...why do you need that many??")
        if len(Book_list) >= 30 and len(Book_list) <= 40:
            print("ok what could you possibly need", len(Book_list), "books for")


    # print out list (show)
    elif User_input == "show":
        print("your list has: ", Book_list)

    # Clear inventory (reset)
    elif User_input == "reset":
        Double_check = input("are you sure? this will remove ALL current books in your list (y/n)", )
        if Double_check == "n":
            print("clear has been cancled")
        if Double_check == "y":
            Book_list = []
            print("book list has successfully been reset")


    # incorrect option
    else:
        No_option_attempts += 1
        print("thats not an option")
        if No_option_attempts >= 5:
            print("still not an option")
        if No_option_attempts >= 7 and No_option_attempts <= 5:
            print("thats uh, still not an option")
        if No_option_attempts >= 9 and No_option_attempts <= 7:
            print("sir", User_input, "isnt on the menu")
        if No_option_attempts >= 11 and No_option_attempts <= 9:
            print("hello?? are you reading this??? thats NOT and option")
        if No_option_attempts >= 13 and No_option_attempts <= 11:
            print("THAT ISNT A THING, PICK SOMETHING FROM THE LIST BELOW")
        if No_option_attempts >= 15:
            print("please stop")

    # break loop
    if User_input == "q":
        break

# results
print("   Program ended, total history:")
print("Complete list: ", Book_list)
print("Removed books: ", Removed_list)
print("Total amount of books in list: ", len(Book_list))