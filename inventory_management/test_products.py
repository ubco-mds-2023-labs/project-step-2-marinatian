import unittest
from inventory_management.products import ProductManager

class TestProductManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up TestProductManager class...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestProductManager class...")

    def setUp(self):
        self.pm = ProductManager()

    def tearDown(self):
        del self.pm

    def test_add_product(self):
        self.pm.add_product(1, "Product1", 100)
        self.assertIn(1, self.pm.products)
        self.assertEqual(self.pm.products[1]["name"], "Product1")
        self.assertEqual(self.pm.products[1]["price"], 100)
        with self.assertRaises(ValueError):
            self.pm.add_product(1, "Product2", 200)

    def test_remove_product(self):
        self.pm.add_product(2, "Product2", 200)
        self.pm.remove_product(2)
        self.assertNotIn(2, self.pm.products)
        with self.assertRaises(KeyError):
            self.pm.remove_product(3)
