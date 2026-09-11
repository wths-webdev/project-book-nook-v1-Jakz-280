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
# genre's
Book_list = [

    ] 

Removed_list = [

    ]

Comedy_genre = [
    "dog man", 
    "the bad guys",
    ]

Horror_genre = [
    "five nights at freddys into the pit", 
    "the nightmaries",
    ]

Fiction_genre = [
    "wonder woman", 
    "batman court of owls", 
    "gullmetal alchemist", 
    "harry potter and the goblet of fire",
    ]

Manga_genre = [
    "my hero academia", 
    "naruto",
    ]

History_genre = [
    "world war two", 
    "the pyramids",
    ]

Easter_eggs = [

]

Full_library = Comedy_genre + Horror_genre + Fiction_genre + Manga_genre + History_genre

# detail
No_option_attempts = 0
logo_1 = str("       ______ ______        ")
logo_2 = str("    __/      Y      \__     ")
logo_3 = str("   / / ~Book | ~~ ~  \ \    ")
logo_4 = str("  / / ~ ~ ~~ |  Nook~ \ \   ")
logo_5 = str(" /_/________.|.________\_\  ")
logo_6 = str(" \ \--------`-'--------/ /  ")
Flavor_text_list = [
    "Our library has everything and nothing!", 
    "Look mom! im a peice of flavor text!", 
    "All roads lead to books", 
    "Now with more paper!", 
    "Dont worry user, the library has enough books to feed you for a life time, LIBRARIAN GET ME MORE BOOKS THE KIDS HUNGRY", 
    "Now without calender errors! I think, does the number count go that high?", 
    "Help me im running out of ideas for flavor text", 
    "We need money to keep our employees happy", 
    "books made from the very first tree!", 
    "Did I ever tell you about the time Jeff tried to steal from the library? He got jumped before he could reach the door",
    "You changed user! you ACTUALLY changed! You learned how to stop being a chud and read!!",
    "I KNEW THAT DOOR HAD A LOCK ON IT, EVERYBODY KEPT TELLING ME I WAS LOSING MY MIND",
    "Be quiet while in the library, our librarians hate noise",
    "Yo does anyone actually read these",
    "iteleportedbread",
    "Now with cool easter eggs!",
    ]





while True:
        # reset info
    No_option_attempts = 0
    Flavor_text = random.choice(Flavor_text_list)
        # welcome message
    print("<<=============================>>")
    print(" ")
    print("Welcome to Book Nook!")
    print(logo_1)
    print(logo_2)
    print(logo_3)
    print(logo_4)
    print(logo_5)
    print(logo_6)
    print(" ")
    print("<<=============================>>")
        # ask user for input
    print(" ")
    print("Menu:") 
    print(" ▻ Type help and hit enter for more info (help)" )
    print(" ▻ Add book (add)" )
    print(" ▻ Remove book (remove) ")
    print(" ▻ Show count (count) ")
    print(" ▻ Show books (show) ")
    print(" ▻ Show library (library) ")
    print(" ▻ Clear all (reset) ")
    print(" ▻ See found easter eggs (secrets) ")
    print(" ▻ Quit (q)" )
    print(" ")
# flavor text
    print(Flavor_text)
    print(" ")
    User_input = ((input("Enter an option: ").lower()).strip())

    # inform user (help)
    if User_input == "help":
        No_option_attempts = 0
        print("well to summarize everything: ")
        print(" Basics: Simply enter any of the options from the menu with your keyboard to perform that action")
        print(" ▸ add: Used to add books to the list")
        print(" ▸ remove: Used to remove books from the list")
        print(" ▸ count: Tells you how many books are in the list")
        print(" ▸ show: Shows all current books in the list")
        print(" ▸ library: This will ask another question asking what genre before showing a list of the books in it")
        print(" ▸ reset: This will ask you again for confirmation before removing all books from the list")
        print(" ▸ secrets: Some prompts may have special responses! Hint: Some are found through flavor text")
        print(" ▸ q: This will end the program")
        print("This is an early version and a proper library has not been set, so expect it to be a bit odd (but its mostly intact)")
    
    # ask user for book (add)
    if User_input == "add":
        No_option_attempts = 0
        New_book = ((input("What book would you like to add?: ").lower()).strip())
    # check
        if New_book not in Full_library:
            print("We dont have that book")
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
        if Remove_book in Book_list:
         Book_list.remove(Remove_book)
         Removed_list.append(Remove_book)
    # success message
         print(Remove_book, "was removed")
        if Remove_book not in Book_list:
            print("That book is not in the list or was already removed")

    # show amount in list (count)
    elif User_input == "count":
        No_option_attempts = 0
        if len(Book_list) < 10:
            print("as of now, you have", len(Book_list), "in your list")
        elif len(Book_list) >= 10 and len(Book_list) < 20:
            print("as of now, you have", len(Book_list), "in your list, thats a lot")
        elif len(Book_list) >= 20 and len(Book_list) < 30:
            print("as of now you have...", len(Book_list), "which is...why do you need that many??")
        elif len(Book_list) >= 30:
            print("ok what could you possibly need", len(Book_list), "books for")


    # print out list (show)
    elif User_input == "show":
        No_option_attempts = 0
        print("your list has: ", Book_list)

    # show library (library)
    elif User_input == "library":
        No_option_attempts = 0
        print("(all/comedy/horror/fiction/manga/info/history)")
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
            print("for manga, we currently have: ", Manga_genre)
        if Selected_genre == "history":
            print("for for comics, we currently have: ", History_genre)

    # Clear inventory (reset)
    elif User_input == "reset":
        No_option_attempts = 0
        Double_check = ((input("are you sure? this will remove ALL current books in your list (y/n)").lower()).strip())
        if Double_check == "n":
            print("clear has been cancled")
        if Double_check == "y":
            Book_list = []
            print("book list has successfully been reset")

    elif User_input == "secrets":
        No_option_attempts == 0
        print("Secrets found: ", Easter_eggs)

    elif User_input == "iteleportedbread":
        No_option_attempts = 0
        print(" w h a t ")
        ResponseTf2EG = input().lower()
        if ResponseTf2EG == "you told me to":
            print("how. much.")
            ResponseTf2EGtwo = input().lower()
            if ResponseTf2EGtwo == "i have done nothing but teleport bread for the past three days":
                print("WHERE!?!? WHERE HAVE YOU BEEN SENDING IT!?!?!?!?")
                Easter_eggs.append(User_input)

    elif User_input == "tree":
        No_option_attempts == 0
        print("theres a man here")
        Easter_eggs.append(User_input)

    # incorrect option
    else:
        No_option_attempts += 1
        if No_option_attempts >= 1 and No_option_attempts < 5:
            print("<<=============================>>")
            print("thats not an option")
    # incorrect option special text
        elif No_option_attempts >= 5 and No_option_attempts < 7:
            print("<<=============================>>")
            print("still not an option")
        elif No_option_attempts >= 7 and No_option_attempts < 9:
            print("<<=============================>>")
            print("thats uh, still not an option")
        elif No_option_attempts >= 9 and No_option_attempts < 11:
            print("<<=============================>>")
            print("sir", User_input, "isnt on the menu")
        elif No_option_attempts >= 11 and No_option_attempts < 13:
            print("<<=============================>>")
            print("hello?? are you reading this??? thats NOT and option")
        elif No_option_attempts >= 13 and No_option_attempts < 15:
            print("<<=============================>>")
            print("THAT ISNT A THING, PICK SOMETHING FROM THE LIST BELOW")
        elif No_option_attempts >= 15:
            print("<<=============================>>")
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
print("Total amount of books in list: ", len(Book_list))