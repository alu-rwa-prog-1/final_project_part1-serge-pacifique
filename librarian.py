# Calling Audiobook class
from audiobook import Audiobook

# Calling Film
from film import Film

# Class Creation
class Librarian(Film, Audiobook):
    """ This is a Librarian Class with its characteristics
    """
    # Add method
    def add(self, books, audiobooks, films):
        """ This method allow the Librarian to add Item
        """
        print("ADDING AN ITEM PROCESS \n_____________________________")
        type_item = input("PLEASE ENTER THE ITEM YOU ARE GOING TO ADD: ")
        # Adding Audiobook
        if type_item.lower() == "book":
            self.title = input("Please enter the title of the book: ")
            self.genre = input("Please enter the genre of the book: ")
            self.author = input("Who is the author of the book: ")
            self.published_year = input("When was the book published: ")
            self.no_item = int(input("Please enter the number of the book: "))
            self.donor_name = input("Please enter a donor's name or 'None' if it was not donated: ")
            self.selling_price = input("What is the Selling price of the book: ")
            books.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.title)
            print("\n" , len(books))

        # Adding Audiobook
        elif type_item.lower() == "audiobook":
            self.title = input("Please enter the title of the audiobook: ")
            self.genre = input("Please enter the genre of the audiobook: ")
            self.no_item = int(input("Please enter the number of the CDs: "))
            self.donor_name = input("Please enter a donor's name or 'None' if it was not donated: ")
            self.selling_price = input("How much is the audiobook sold for: ")
            self.author = input("Who is the author of the audiobook: ")
            self.published_year = input("When was the audiobook published: ")
            self.rental_price = input("How much is the audiobook rented for:")
            audiobooks.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.title)
            print("\n" , len(audiobooks))

        # Adding Film
        elif type_item.lower() == "film":
            self.title = input("Please enter the title of the film: ")
            self.genre = input("Please enter the genre of the film: ")
            self.type = input("Please enter the type of the film: ")
            self.no_item = int(input("Please enter the number of the CDs: "))
            self.donor_name = input("Please enter a donor's name or 'None' if it was not donated: ")
            self.selling_price = input("How much is the film sold for: ")
            self.released_year = input("When was the film published: ")
            self.rental_price = input("How much is the film rented for:")
            films.append(self)
            print("YOU HAVE SUCCESSFULLY ENTERED:" , self.title)
            print("\n" , len(films))

    # Sell method
    def sell(self, books, audiobooks, films):
        """ This method allow the Librarian to sell Item
        """
        print("SELLING AN ITEM PROCESS \n_____________________________")
        typeitem = input("PLEASE ENTER THE ITEM YOU ARE GOING TO SELL: ")
        if typeitem.lower() == "book":
            titlebook = input("PLEASE ENTER THE BOOK YOU WANT TO SELL: ")
            if titlebook:
                for x in books:
                    if titlebook == x.title:
                        print(x.title , "PRICE IS " , x.selling_price)
                        x.no_item = x.no_item - 1
                        print("THEY ARE" , x.no_item , "COPIES OF " , x.title)

        elif typeitem.lower() == "audiobook":
            titleaudiobook = input("PLEASE ENTER THE AUDIOBOOK YOU WANT TO SELL: ")
            if titleaudiobook:
                for x in audiobooks:
                    if titleaudiobook == x.title:
                        print(x.title , "PRICE IS " , x.selling_price)
                        x.no_item = x.no_item - 1
                        print("THEY ARE" , x.no_item , "COPIES OF " , x.title)

        elif typeitem.lower() == "film":
            titlefilm = input("PLEASE ENTER THE FILM YOU WANT TO SELL: ")
            if titlefilm:
                for x in films:
                    if titlefilm == x.title:
                        print(x.title , "PRICE IS " , x.selling_price)
                        x.no_item = x.no_item - 1
                        print("THEY ARE" , x.no_item , "COPIES OF " , x.title)

    # Renting method
    def rent(self, audiobooks, films):
        """ This method allow the Librarian to rent Item
        """ 
        print("RENTING AN ITEM PROCESS \n_____________________________")
        typeitem = input("PLEASE ENTER THE ITEM YOU ARE GOING TO RENT: ")
        if typeitem.lower() == "audiobook":
            titleaudiobook = input("PLEASE ENTER THE AUDIOBOOK YOU WANT TO RENT:")
            if titleaudiobook:
                for x in audiobooks:
                    if titleaudiobook == x.title:
                        print(x.title , "RENTING PRICE IS " , x.rental_price)
                        x.no_item = x.no_item - 1
                        print("THEY ARE" , x.no_item , "COPIES OF " , x.title)

        elif typeitem.lower() == "film":
            titlefilm = input("PLEASE ENTER THE FILM YOU WANT TO RENT: ")
            if titlefilm:
                for x in films:
                    if titlefilm == x.title:
                        print(x.title , "RENTING PRICE IS " , x.rental_price)
                        x.no_item = x.no_item - 1
                        print("THEY ARE" , x.no_item , "COPIES LEFT OF " , x.title)


    # Lend method
    def lend(self, books):
        """ This method allow the Librarian to lend Item
        """
        titlebook = input("PLEASE ENTER THE BOOK YOU WANT TO LEND: ")
        if titlebook:
            for x in books:
                if titlebook == x.title:
                    print("THIS BOOK CAN BE BORROWED FOR 30 DAYS")
                    x.no_item = x.no_item - 1
                    print("THEY ARE" , x.no_item , "COPIES OF " , x.title)

    # View method
    def view(self, books, audiobooks, films):
        """ View method help the Librarian to view Item
        """
        print("YOU CAN VIEW ALL ITEMS FROM HERE \n--------------------------------")
        toview = input("WHICH ITEMS DO YOU WANT TO VIEW: ")
        if toview.lower() == "books":
            print("\n ALL AVAILABLE BOOKS IN THE LIBRARY:", len(books), "\n")
            for i in books:
                print("BOOK TITLE: " , i.title)
                print("BOOK GENRE: " , i.genre)
                print("BOOK AUTHOR: " , i.author)
                print("BOOK PUBLISHED YEAR: " , i.published_year)
                print("NUMBER OF", i.title , "LEFT", i.no_item ,": ")
                print("BOOK DONOR NAME: " , i.donor_name)
                print("BOOK SELLING PRICE: " , i.selling_price)

        elif toview.lower() == "audiobooks":
            print("\n ALL AVAILABLE BOOKS IN THE LIBRARY...... :", len(audiobooks), "\n")
            for i in audiobooks:
                print("BOOK TITLE: " , i.title)
                print("BOOK GENRE: " , i.genre)
                print("BOOK AUTHOR: " , i.author)
                print("BOOK PUBLISHED YEAR: " , i.published_year)
                print("NUMBER OF", i.title , "LEFT", i.no_item ,": ")
                print("BOOK DONOR NAME: " , i.donor_name)
                print("BOOK SELLING PRICE: " , i.selling_price)

        if toview.lower == "films":
            print("\n ALL AVAILABLE BOOKS IN THE LIBRARY...... :", len(films), "\n")
            for i in films:
                print("BOOK TITLE: " , i.title)
                print("BOOK GENRE: " , i.genre)
                print("BOOK AUTHOR: " , i.author)
                print("BOOK PUBLISHED YEAR: " , i.released_year)
                print("NUMBER OF", i.title , "LEFT", i.no_item ,": ")
                print("BOOK DONOR NAME: " , i.donor_name)
                print("BOOK SELLING PRICE: " , i.selling_price)
