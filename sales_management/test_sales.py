import unittest
from sales_management.sales import SalesManager

class Test_SalesManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.sales_manager = SalesManager()
    
    def tearDown(self):
        self.sales_manager.sales_records.clear()
    
    def test_record_sale(self):
        self.assertEqual(len(self.sales_manager.sales_records), 0)
        self.sales_manager.record_sale("P0001", 2, 100.0)
        self.assertEqual(len(self.sales_manager.sales_records), 1)
        self.assertEqual(self.sales_manager.sales_records[0]['product_id'], "P0001")
        self.assertEqual(self.sales_manager.sales_records[0]['quantity'], 2)
        self.assertEqual(self.sales_manager.sales_records[0]['price'], 100.0)
    
    def test_total_sales(self):
        self.sales_manager.record_sale("P0001",2,100.0)
        self.sales_manager.record_sale("P0002",1,200.0)
        self.sales_manager.record_sale("P0003",3,50.0)
        excepted_total = (2*100.0) + (1*200.0) + (3*50.0)
        self.assertEqual(self.sales_manager.total_sales(),excepted_total)
        self.assertGreater(self.sales_manager.total_sales(),0)
        self.assertIsInstance(self.sales_manager.total_sales(), float)
        self.assertNotEqual(self.sales_manager.total_sales(), 500.0)

    
if __name__ == '__main__':
    unittest.main()