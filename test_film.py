import unittest

from film import Film

class Test_Film(unittest.TestCase):
  """ The Test case for Film
  """
  
  def Test_init(test):
    Action film = Film("Action film")
    self.assertEqual(Action film.type, "Action film")
    2019 = Film("2019")
    self.assertNotEqual(2019.released_year, "2020")
    
    
  if__name__ = "__main__":
    unittest.main()
