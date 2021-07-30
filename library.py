library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement including library name
print(f'Welcome to {library["name"]}' )
option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        # TODO - List all books
        for book in library['books']:
            print(f"{book['title']} by {book['author']}")

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        book_search = input("Please enter the title of the book ")
        for book in library["books"]:
            if book_search.lower() == book['title'].lower():
                print(f"{book['title']} by {book['author']} found!")
                break
        else:
            print("Book not found")

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        user_author = input("Please enter the name of the author ")
        user_title = input("Please enter the title of the book ")
        library['books'].append({"author": user_author.capitalize(), "title" : user_title.capitalize()})
        print("Book added!")

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book
        book_remove = input("Please enter the title of the book you would like to take out ")
        for book in library["books"]:
            if book_remove.lower() == book['title'].lower():
                library["books"].remove(book)
                print("Book removed!")
                break
        else: print("No book with that title exists in the library")
        

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        book_change = input("Please enter the title of the book you would like to change ")
        for book in library["books"]:
            if book_change.lower() == book['title'].lower():
                book_change_title = input("Please enter a new title for this book ")
                if book_change_title == "":
                    book["title"] = book["title"]
                else:  
                    book["title"] = book_change_title
                author_change = input("Please enter the author for this book ")
                if author_change == "":
                    book["author"] = book["author"]
                else:
                    book["author"] = author_change
                print("Book updated!")
                break
        else: print("No book found!")
                
