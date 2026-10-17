from django.test import TestCase
from .models import Chef, Category, MenuItem


class ChefModelTest(TestCase):
    def setUp(self):
        self.chef = Chef.objects.create(name="Gordon Ramsay", specialization="French Cuisine")
    
    def test_chef_creation(self):
        self.assertEqual(self.chef.name, "Gordon Ramsay")


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main")
    
    def test_category_creation(self):
        self.assertEqual(self.category.name, "Main")


class MenuItemModelTest(TestCase):
    def setUp(self):
        self.chef = Chef.objects.create(name="Jamie Oliver")
        self.category = Category.objects.create(name="Starter")
        self.menu_item = MenuItem.objects.create(
            name="Caesar Salad",
            category=self.category,
            chef=self.chef,
            price=8.99,
        )
    
    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.name, "Caesar Salad")
