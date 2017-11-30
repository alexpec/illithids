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

    def test_CalculateAtConstantVolume(self):
        heatCap = self.hc
        energyArray = self.energyArray
        temperature = 300.0
        
        cv_exp = 40.23016
        cv = heatCap.CalculateAtConstantVolume(energyArray, temperature)

        self.assertAlmostEqual(cv, cv_exp, 3)
        
        
    def test_CalculateAtConstantPressure(self):
        heatCap = self.hc
        energyArray = self.energyArray
        temperature = 300.0
        totalAtoms = 3000
        
        
        cp_exp = 65.17355
        cp = heatCap.CalculateAtConstantPressure(energyArray, temperature, totalAtoms)
        
        self.assertAlmostEqual(cp, cp_exp, 3)
    
    
    def test_CalculateHeatCapacityIdealGas(self):
        heatCap = self.hc
        energyArray = self.energyArray
        temperature = 300.0
        
        
        c_exp = 40.23016
        c = heatCap.CalculateHeatCapacityIdealGas(energyArray, temperature)
        
        self.assertAlmostEqual(c, c_exp, 3)
    
    
    
if __name__ == '__main__':
    unittest.main()