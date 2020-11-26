# Calling the parent class
from item import Item

# Calling a second parent class
from audiobook import Audiobook

# Creating a child class
class Book(Item, Audiobook):
    pass