import unittest
from Scripts.HeatCapacity import HeatCapacity
import os
import numpy



class TestHeatCapacity(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        main_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = '%s/docs/water_full_300K.txt' %main_path
        
        self.hc = HeatCapacity()
        
        self.data = numpy.loadtxt(self.filename, numpy.float, '#', ';')
        self.energyArray = self.data[:,4]
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_CalculateHC(self):
        heatCap = self.hc
        energyArray = self.energyArray
        h2oMass = 18.0/1000.0
        temperature = 300.0
        
        cv = heatCap.CalculateAtConstantVolume(energyArray, temperature, h2oMass, temperature)
        
        self.assertRaises(NotImplementedError, heatCap.CalculateHC, *[energyArray,300.0,4200.0])
                
    
    
    
if __name__ == '__main__':
    unittest.main()