# Calling the parent class
from item import Item

# Creating a child class
class Audiobook(Item):
    """This is a class child for our Audiobook with its specifications
    """
    def __init__(self, title = "", genre = "", no_item =0, donor_name="", author="",
                 published_year = 0, rental_price = 0):
        super().__init__(title, genre, no_item, donor_name)
        self.author = author
        self.published_year = published_year
        self.rental_price = rental_price
