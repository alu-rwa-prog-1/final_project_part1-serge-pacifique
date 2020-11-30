import unittest


from librarian import Librarian

class Test_librarian(unittest.TestCase):
  """ This a Librarian Test
  """
  
  def add(self):
    """ This a testing code of the add method
    """
    book = Librarian("book")
    self.assertEqual(book.type_item, "book")
    self.assertNotEqual(book.type_item, "audiobook")
    
    
  def sell(self):
    """ Testing code of sell method
    """
    
    
  def rent(self):
    """ Testing code of rent method
    """
    
  def view(self):
    """ Testing code of view method
    """
    
  def lend(self):
    """ Testing code of lend method
    """
      
      
    
    
