

import numpy
import unittest
import os
from Scripts.ErrorOnAverage import ErrorOnAverage




class TestErrorOnAverage(unittest.TestCase):
    '''
    Tests for Flyvbjerg Petersen
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.dataset = numpy.array([
            298.55, 300.89, 300.19, 298.80, 301.63, 300.40, 301.34,
            300.27, 299.28, 300.13, 301.13, 299.09, 300.63, 301.43, 
            299.95, 300.00, 300.40, 301.04, 302.05, 300.75
        ])
        
        self.calculator = ErrorOnAverage()
        
        
    def test_GenerateBlock(self):
        calculator = self.calculator
        temp = self.dataset
        
        first_expected = numpy.array([
            299.720, 299.495, 301.015, 300.805, 299.705,
            300.110, 301.030, 299.975, 300.720, 301.400
        ])
        
        new_block = calculator.GenerateBlock(temp)
        size_expected = numpy.alen(first_expected)
        
        
        self.assertEqual(numpy.alen(new_block), size_expected)
        numpy.testing.assert_almost_equal(new_block, first_expected, 3)
        
        
    def test_CalculateVariance(self):
        calculator = self.calculator
        temp = self.dataset
        
        
        r2, err = calculator.CalculateVariance(temp)
        
        expected_r2 = 0.0447
        expected_err = 0.014503598
        
        self.assertAlmostEqual(r2, expected_r2, 3)
        self.assertAlmostEqual(err, expected_err, 3)
        
        
    def test_CalculateVarianceBlocks(self):
        calculator = self.calculator
        temp = self.dataset
        
        r2, err = calculator.CalculateVarianceBlocks(temp)   
        
        expected_r2 = numpy.array([0.04470, 0.045229, 0.078839, 0.000722])
        expected_err = numpy.array([0.014503598, 0.0213214, 0.055747857, 0.001021438])
        
        numpy.testing.assert_almost_equal(r2, expected_r2, 3)
        numpy.testing.assert_almost_equal(err, expected_err, 3)     
        
        
    def test_CalculateStdBlocks(self):
        calculator = self.calculator
        temp = self.dataset
        
        r, err = calculator.CalculateStdBlocks(temp)
        
        expected_r   = numpy.array([0.211431058, 0.212672479, 0.280783502, 0.026875])
        expected_err = numpy.array([0.034298647, 0.050127384, 0.099271959, 0.019003495])
        
        numpy.testing.assert_almost_equal(r, expected_r, 3)
        numpy.testing.assert_almost_equal(err, expected_err, 3)
    
    
    def test_CalculateFromBlocks(self):
        calculator = self.calculator
        r_block   = numpy.array([
            0.93, 1.15, 1.40, 1.54, 1.52, 1.53, 1.53, 1.60, 1.72, 1.86, 1.04, 0.32
        ])
        
        r = calculator.CalculateFromBlocks(r_block)
        
        self.assertAlmostEqual(r, 1.53, 2)
        
        
    def test_CalculateMean(self):
        calculator = self.calculator
        self.assertRaises(NotImplementedError, calculator.CalculateMean, None)
        
        
    def test_Methodology(self):
        filepath = os.path.dirname(os.path.abspath(__file__))
        filename = '%s/docs/water_full_300K.txt' %filepath
        dataset = numpy.loadtxt(filename, numpy.float, '#', ';') #time, temp, pe, ke, etotal
        
        ke = dataset[:,3]

        calculator = self.calculator
        ke_r, _ = calculator.CalculateStdBlocks(ke)
        
        exp_ke_r = numpy.array([
            0.93, 1.15, 1.40, 1.54, 1.52, 1.53, 1.53, 1.60, 1.72, 1.86, 1.04, 0.32
        ])
        
        
        pe = dataset[:,2]
        
        pe_r, _ = calculator.CalculateStdBlocks(pe)
        
        exp_pe_r = numpy.array([
            1.96, 2.69, 3.62, 4.55, 5.25, 5.87, 7.09, 7.63, 8.08, 9.15, 12.39, 20.10
        ])
        
        numpy.testing.assert_almost_equal(ke_r, exp_ke_r, 2)
        numpy.testing.assert_almost_equal(pe_r, exp_pe_r, 2)
    
        
if __name__ == '__main__':
    unittest.main()