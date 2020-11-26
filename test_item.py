import unittest

from item import Item

class Test_item(unittest.TestCase):
    def test_init(self):
        Anna = Item("Anna")
        self.assertEqual(Anna.title, "Anna")
