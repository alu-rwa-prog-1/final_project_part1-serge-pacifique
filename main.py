# Author: Pacifique & Serge
# Library Management System

from item import Item

from book import Book

from audiobook import Audiobook

from film import Film

from librarian import Librarian

books = []
audiobooks = []
films = []

loop = True

while(loop):
    print("\n----LIBRARY MANAGEMENT SYSTEM----\n")
    print("THE FOLLOWING ARE ITEMS IN THE LIBRARY")
    print("1. Book \n2. Audiobook \n3. Film")
    print("\nFOLLOWING ARE ACTIONS YOU CAN MAKE ON ITEMS IN THE LIBRARY: ")
    print("1. ADD \n2. SELL \n3. RENT \n4. LEND \n5. VIEW ITEM")
    action = int(input("\nPLEASE ENTER THE NUMBER OF THE OPERATION YOU WANT TO MAKE: "))
    print("---------------------------------------------------------\n")
    if action == 1:
        new = Librarian()
        new.add(books, audiobooks, films)

    if action == 2:
        buy = Librarian()
        buy.sell(books, audiobooks, films)

    if action == 3:
        torent = Librarian()
        torent.rent(audiobooks, films)

    if action == 4:
        borrow = Librarian()
        borrow.lend(books)

    if action == 5:
        viewitem = Librarian()
        viewitem.view(books, audiobooks, films)






