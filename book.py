# Calling the parent class
from item import Item
""" This method is calling the parent class to the child class
"""

# Calling a second parent class
from audiobook import Audiobook
"""This is importing the audiobook file to the book file
"""

# Creating a child class
class Book(Item, Audiobook):
    """This is a child class for our Book(Item, Audiobook) with its characteristics
    """
    pass
