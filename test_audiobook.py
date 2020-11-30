import unittest

from audiobook import Audiobook(Item)

class Test_audiobook(unittest.TestCase):
  """ This is our test class for audiobook
  """
  
  def test_init(test):
    The 100 = audiobook("The 100")
    self.assertEqual(The 100.title, " The 100")
    Chinua Achebe = audiobook("Chinua Achebe")
    self.assertNotEqual(Chinua Achiebe.author, "Obama")
    2020 = audiobook("2020")
    self.assertEqual(2020.published_year, "2020")
    
     
    
  if __name__ == "__main__"
  unittest.main()
