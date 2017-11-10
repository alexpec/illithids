import unittest
from Scripts.HeatCapacity import HeatCapacity



class TestHeatCapacity(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.calculator = HeatCapacity()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_load_file(self):
        self.assertRaises(NotImplementedError, self.calculator._load_file, "filename")
        
        
    def test_calculate(self):
        self.assertRaises(NotImplementedError, self.calculator.Calculate, 300.)
    
    
    
if __name__ == '__main__':
    unittest.main()