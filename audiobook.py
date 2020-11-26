# Calling the parent class
from item import Item

# Creating a child class
class Audiobook(Item):
    def __init__(self, title, genre, no_item, donor_name, author, published_year, rental_price, selling_price):
        super().__init__(title, genre, no_item, donor_name)
        self.author = author
        self.published_year = published_year
        self.rental_price = rental_price
        self.selling_price = selling_price
