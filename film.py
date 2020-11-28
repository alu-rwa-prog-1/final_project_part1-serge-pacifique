# Calling the parent class
from item import Item
""" this importing item file to the film file
"""

# Calling a second parent class
from audiobook import Audiobook
""" this importing the audiobook file to the film file
"""

# Creating a child class
class Film(Item, Audiobook):
    """ This a Film class with its attributes
    """
    def __init__(self, title, genre,no_item, donor_name, type, released_year):
     super().__init__(title, genre,no_item, donor_name)
     self.type = type
     self.released_year = released_year
