
from django.test import TestCase
from models import Menu

class MenuTest(TestCase):

    def test_get_item(self):
        menu_item = Menu.objects.create(title="Spaghetti", price=12.50, inventory=10)
        self.assertEqual(menu_item.get_item(), 'Spaghetti : 12.50')
