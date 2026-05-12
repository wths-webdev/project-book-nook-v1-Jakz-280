   # Da plan:
'''
list of books
QOL changes
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

# imports and conveinence
import random
def words_only():
    (isinstance(User_input, str))

# global variables
Book_list = []
Removed_list = []
Comedy_genre = ["joke book", "the bad guys"]
Horror_genre = ["five nights at freddys into the pit", "the nightmaries"]
Fiction_genre = ["wonder woman", "batman court of owls", "fullmetal alchemist", "harry potter and the goblet of fire"]
Manga_genre = ["my hero academia", "naruto"]
Info_genre = ["dictonary", "study guide"]
History_genre = ["world war two", "the pyramids"]
Full_library = Comedy_genre + Horror_genre + Fiction_genre + Manga_genre + Info_genre + History_genre
No_option_attempts = 0


# welcome message
print("Welcome to Book Nook!")

print("       ______ ______       ")
print("     _/      Y      \_     ")
print("   / / ~Book | ~~ ~  \ \   ")
print("  / / ~ ~ ~~ |  Nook~ \ \  ")
print(" / /________.|.________\ \ ")
print(" \ \--------`-'--------/ / ")

while True:
    Flavor_text = random.randint(0, 10)
# ask user for input
    print(" ")
    print("Menu:") 
    print(" Type help and hit enter for more info (help)" )
    print(" Add book (add)" )
    print(" Remove book (remove) ")
    print(" Show count (count) ")
    print(" Show books (show) ")
    print(" Show library (library) ")
    print(" Clear all (reset) ")
    print(" Quit (q)" )
    print(" ")
# flavor text
    if Flavor_text == 1:
        print("Our library has everything and nothing!")
    elif Flavor_text == 2:
        print("Look mom! im a peice of flavor text!")
    elif Flavor_text == 3:
        print("All roads lead to books")
    elif Flavor_text == 4:
        print("Now with more paper!")
    elif Flavor_text == 5:
        print("Removed herobrian, i think")
    elif Flavor_text == 6:
        print("Dont worry user, the library has enough books to feed you for a life time, LIBRARIAN GET ME MORE BOOKS THE KIDS HUNGRY")
    elif Flavor_text == 7:
        print("Now without calender errors! i think, does the number count go that high?")
    elif Flavor_text == 8:
        print("help me im running out of ideas for flavor text")
    elif Flavor_text == 9:
        print("We need money to keep our employees happy")
    elif Flavor_text == 10:
        print("books made from the very first tree!")
    else:
        print("i think...a bit of flavor text is missing...")
    print(" ")
    User_input = ((input("enter an option: ").lower()).strip())

    # inform user (help)
    if User_input == "help":
        print("well to summarize everything: ")
        print(" Basics: simply enter any of the options from the menu with your keyboard to perform that action")
        print(" add: used to add books to the list")
        print(" remove: used to remove books from the list")
        print(" count: tells you how many books are in the list")
        print(" show: shows all current books in the list")
        print(" library: this will ask another question asking what genre before showing a list of the books in it")
        print(" reset: this will ask you again for confirmation before removing all books from the list")
        print(" q: this will end the program")
        print("this is an early version and a proper library has not been set, so expect it to be a bit odd (but its mostly intact)")
    
    # ask user for book (add)
    if User_input == "add":
        No_option_attempts = 0
        New_book = ((input("what book would you like to add?: ").lower()).strip())
    # check
        if New_book not in Full_library:
            print("we dont have that book")
    # add to list
        if New_book in Full_library:
            Book_list.append(New_book)
            print(Book_list)
        # success message
            print(New_book, "was added")

    # remove from list (remove)
    elif User_input == "remove":
        No_option_attempts = 0
        Remove_book = ((input("what book would you like to remove?: ").lower()).strip())
        Book_list.remove(Remove_book)
        Removed_list.append(Remove_book)
    # success message
        print(Remove_book, "was removed")
        if Remove_book not in Book_list:
            print("That book is not in the list or was already removed")

    # show amount in list (count)
    elif User_input == "count":
        No_option_attempts = 0
        print("as of now, you have", Book_list.count, "in your list")
        if Book_list.count >= 10:
            print("as of now, you have", Book_list.count, "in your list, thats a lot")
        if Book_list.count >= 20:
            print("as of now you have...", Book_list.count, "which is...why do you need that many??")
        if Book_list.count >= 30:
            print("ok what could you possibly need", Book_list.count, "books for")


    # print out list (show)
    elif User_input == "show":
        print("your list has: ", Book_list)

    # show library (library)
    elif User_input == "library":
        print("(all/comedy/horror/fiction/manga)")
        Selected_genre = ((input("what genre do you want to look at?: ").lower()).strip())
        if Selected_genre == "all":
            print("for everything, we currently have: ", Full_library)
        if Selected_genre == "comedy":
            print("for comedy, we currently have: ", Comedy_genre)
        if Selected_genre == "horror":
            print("for horror, we currently have: ", Horror_genre)
        if Selected_genre == "fiction":
            print("for fiction, we currently have: ", Fiction_genre)
        if Selected_genre == "manga":
            print("for for comics, we currently have: ", Manga_genre)
        

    # Clear inventory (reset)
    elif User_input == "reset":
        Double_check = ((input("are you sure? this will remove ALL current books in your list (y/n)").lower()).strip())
        if Double_check == "n":
            print("clear has been cancled")
        if Double_check == "y":
            Book_list = []
            print("book list has successfully been reset")


    # incorrect option
    else:
        No_option_attempts += 1
        print("thats not an option")
    # incorrect option special text
        if No_option_attempts >= 5:
            print("still not an option")
        if No_option_attempts >= 7:
            print("thats uh, still not an option")
        if No_option_attempts >= 9:
            print("sir", User_input, "isnt on the menu")
        if No_option_attempts >= 11:
            print("hello?? are you reading this??? thats NOT and option")
        if No_option_attempts >= 13:
            print("THAT ISNT A THING, PICK SOMETHING FROM THE LIST BELOW")
        if No_option_attempts >= 15:
            print("please stop")

    # break loop
    if User_input == "q":
        Are_you_sure = ((input("are you sure? (y/n): ").lower()).strip())
        if Are_you_sure == "y":
            absolutly_positive = ((input("ok but this will end the program and you'll have to run it again (y/n): ").lower()).strip())
            if absolutly_positive == "y":
                last_check = ((input("ok but like, are you ABSOLUTLY sure (y/n): ").lower()).strip())
                if last_check == "y":
                    print("ok fine :(")
                    break

# results
print("  Program ended, total history:")
print("Complete list: ", Book_list)
print("Removed books: ", Removed_list)
print("Total amount of books in list: ", Book_list.count)