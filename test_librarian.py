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
    film = Librarian("film")
    self.assertEqual(film.type_item, "film")
    
    
  def rent(self):
    """ Testing code of rent method
    """
    audiobook = Librarian("audiobook")
    self.assertEqual(audiobook.type_item, "audiobook")
    
  def view(self):
    """ Testing code of view method
    """
    audiobook = Librarian("audiobook")
    self.assertNotEqual(audiobook.type_item, "book")
    
  def lend(self):
    """ Testing code of lend method
    """
    film = Librarian("film")
    self.assertEqual(film.type_item, "film")
      
      
    
    
