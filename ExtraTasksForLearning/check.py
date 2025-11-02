#Writing a program based on the knowledge i've gotten
#from python syntax to python loops.
   ## TASK - PERSONAL LIBRARY MANAGER
   ## GOAL - create a program to manage my personal
   #         book library using all the python concepts ive learnt.

#Using DICTIONARY
#each set contains different data types, integers, string
#list, boolean and tuple
Mylibrary = {
    "Book1":{
        "title": "No more mr nice guy",
        "pages": 260,
        "genre": ["self-help", "psychology"],
        "available": True,
        "published": (2000,11,30),
    },
    "Book2":{
        "title": "Atomic habits",
        "pages": 306,
        "genre": ["self-help", "non-fiction"],
        "available": True,
        "published": (2018,10,16),
    },
    "Book3":{
        "title": "Think and grow rich",
        "pages": 320,
        "genre": ["self-help", "business"],
        "available": True,
        "published": (1937,10,20),
    },
}
print(Mylibrary)
#this prints Mylibrary in a long straight line

#                  ****

##this is to make the output more presentable
for book, details in Mylibrary.items():
    print(f"{book}:")
    print(f"  Title: {details['title']}")
    print(f"  Pages: {details['pages']}")
    print(f"  Genre: {', '.join(details['genre'])}")
    print(f"  Available: {details['available']}")
    print(f"  Published: {details['published']}")
    print()   # blank line after each book

## now, adding new book to Mylibrary by asking the user
#for the details
print("   These are the books in your library   ")
print()
      ## this loops my request, keeps asking the user if he/she
      ## wants to enter a new book.
while True:
    print()
    request = input("do you want to enter a new book to ur library?  yes/no: ").lower()
    if request not in ("y", "yes", "yeah"):
        print("Alright, till next time i guess :)")
        break
    Title = input("please enter the title of the book: ").title()
    Pages = int(input("please enter the number of pages: "))
    Genre = input("please enter the genre of the book: ")
##Genre_format converts the genre entered into a string
    Genre_f = [g.strip() for g in Genre.split(",")]
    available = True
    published = (2025,11,1)
##adds the entered details into the already existing dictionary
## to auto generate next book key so i dont initiate manually again
    next_book_number = len(Mylibrary) + 1

    Mylibrary[f"book{next_book_number}"] = {
        "title": Title,
        "pages": Pages,
        "genre": Genre_f,
        "available": available,
        "published": published,
    }
##prints the updated library
    for book, details in Mylibrary.items():
        print(f"{book}:")
        print(f"  Title: {details['title']}")
        print(f"  Pages: {details['pages']}")
        print(f"  Genre: {', '.join(details['genre'])}")
        print(f"  Available: {details['available']}")
        print(f"  Published: {details['published']}")
        print()   # blank line after each book