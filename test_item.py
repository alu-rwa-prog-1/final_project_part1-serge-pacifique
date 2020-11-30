import unittest

from item import Item

class TestItem(unittest.TestCase):
    def test_init(self):
        testtitle = Item("The 100")
        self.assertEqual(testtitle.title, "The 100")

    # def test_genre(self):
    #     testgenre = Item("", "science fiction")
    #     self.assertEqual(testgenre.title, "", "science fiction")
    #
    # def test_noitems(self):
    #     testnoitem = Item("", "", 1, "", 0)
    #     self.assertNotEqual(testnoitem.title, "", "", 1, "", 0)
    #
    # def test_sellingprice(self):
    #     pass
    #
    # def testnoitems(self):
    #     pass

if __name__ == '__main__':
  unittest.main()


