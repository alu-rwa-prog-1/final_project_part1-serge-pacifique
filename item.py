# Creating a class
class Item:
    """ This is a Item class with its characteristics
    """
    def __init__(self, title="", genre="", no_item=0, donor_name="", selling_price=0):
        self.title = title
        self.genre = genre
        self.no_item = no_item
        self.donor_name = donor_name
        self.selling_price = selling_price

