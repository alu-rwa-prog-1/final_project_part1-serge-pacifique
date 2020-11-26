# Calling the parent class
from item import Item

# Calling a second parent class
from audiobook import Audiobook

# Creating a child class
class Film(Item, Audiobook):
    def __init__(self, title, genre,no_item, donor_name, type, released_year):
     super().__init__(title, genre,no_item, donor_name)
     self.type = type
     self.released_year = released_year