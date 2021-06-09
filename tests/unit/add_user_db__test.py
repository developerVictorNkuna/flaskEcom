from unittest import TestCase

import market
from market  import app

class AddUserTest(TestCase):
    def test_register_user(self):
        user = User('Sello Twala')

        # self.assertEqual(user.name, 'test',
        #                  "The name of the item after creation does not equal the constructor argument.")
        # self.assertEqual(Userprice, 19.99,
        #                  "The price of the item after creation does not equal the constructor argument.")

    # def test_item_json(self):
    #     item = ItemModel('test', 19.99)
    #     expected = {
    #         'name': 'test',
    #         'price': 19.99
    #     }
    #
    #     self.assertEqual(
    #         item.json(),
    #         expected,
    #         "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
