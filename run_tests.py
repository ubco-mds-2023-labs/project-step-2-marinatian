
import unittest
from sales_management.test_sales import Test_SalesManager
from sales_management.test_discounts import Test_DiscountManager
from inventory_management.test_products import TestProductManager
from inventory_management.test_stock import TestStockManager, TestPerishableStockManager


def create_suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(Test_DiscountManager))
    suite.addTests(unittest.makeSuite(Test_SalesManager))
    suite.addTests(unittest.makeSuite(TestProductManager))
    suite.addTests(unittest.makeSuite(TestStockManager))
    suite.addTests(unittest.makeSuite(TestPerishableStockManager))
    runner = unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))

create_suite()