from Scripts.FlyvbjergPetersen_Equilibration import FPEquilibration


import numpy
import unittest
import os




class TestFlyvbjergPetersen_Equilibration(unittest.TestCase):
    '''
    Tests for Flyvbjerg Petersen
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
        main_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = '%s/docs/FP_Equilib.txt' %main_path
        
        self.time_expected = numpy.array([
            5010.,  5020.,  5030.,  5040.,  5050.,  5060.,  5070.,  5080.,
            5090.,  5100.,  5110.,  5120.,  5130.,  5140.,  5150.,  5160.,
            5170.,  5180.,  5190.,  5200.,  5210.,  5220.,  5230.,  5240.,
            5250.,  5260.,  5270.,  5280.,  5290.,  5300.,  5310.,  5320.,
            5330.,  5340.,  5350.,  5360.,  5370.,  5380.,  5390.,  5400.,
            5410.,  5420.,  5430.,  5440.,  5450.,  5460.,  5470.,  5480.,
            5490.,  5500.])
        
        self.temp_expected = numpy.array([
            484.08196466,  471.4899767 ,  470.05767089,  453.64924586,
            452.12358993,  442.76473081,  437.63740928,  439.01098322,
            439.00434017,  422.87143402,  424.40652119,  424.62963404,
            423.12320128,  413.99515924,  407.40405391,  402.01750723,
            404.88065588,  403.75647802,  402.12767319,  400.57892982,
            392.53119955,  398.7008764 ,  394.05174443,  386.37995262,
            392.64189028,  389.63482951,  387.69142105,  387.34042535,
            383.20517886,  383.84953334,  388.12605322,  388.36279022,
            384.25234922,  381.87997424,  380.20792451,  375.734795  ,
            380.49188904,  389.64823287,  378.87056485,  378.78358992,
            379.84960501,  382.16005727,  373.18965302,  383.38065231,
            380.20545745,  378.43930846,  387.36575756,  376.4145764 ,
            374.252078  ,  379.93635444])
        
        self.pe_expected = numpy.array([
            -6496.9684648 , -6519.40797108, -6630.13350378, -6597.27255284,
           -6687.2091099 , -6704.98541458, -6753.52150913, -6859.26743576,
           -6956.02674117, -6898.15321373, -6988.254741  , -7067.02164786,
           -7126.96060625, -7114.59953398, -7114.39029636, -7120.39442469,
           -7195.98139445, -7237.53238466, -7269.81530473, -7303.48257176,
           -7271.40267917, -7364.41018533, -7362.37724124, -7324.62028394,
           -7411.16353099, -7414.93862883, -7424.80948884, -7448.28558416,
           -7433.88700857, -7459.86871182, -7520.26571461, -7546.50543458,
           -7531.41967563, -7528.87092758, -7529.36066099, -7501.96053487,
           -7555.95043263, -7655.37820371, -7575.42419385, -7586.02889324,
           -7606.53633828, -7639.50330214, -7568.1820861 , -7667.54138574,
           -7651.88957365, -7643.8793412 , -7735.72966262, -7649.68372873,
           -7633.29497219, -7688.81822694])
        
        self.ke_expected = numpy.array([
            4327.42619949,  4214.86076097,  4202.05673576,  4055.3744515 ,
            4041.7359276 ,  3958.0728806 ,  3912.2374495 ,  3924.5164442 ,
            3924.45705892,  3780.23776178,  3793.96059569,  3795.95510177,
            3782.4884224 ,  3700.88875298,  3641.9679008 ,  3593.81513967,
            3619.41011193,  3609.36058094,  3594.79996269,  3580.95504973,
            3509.01277275,  3564.16628636,  3522.60560664,  3454.02401239,
            3510.00228694,  3483.12081949,  3465.747818  ,  3462.61010974,
            3425.64328325,  3431.40345748,  3469.63319026,  3471.74948867,
            3435.00440965,  3413.79668368,  3398.84947979,  3358.86216512,
            3401.38796631,  3483.24063815,  3386.89422084,  3386.11671287,
            3395.64630076,  3416.3004717 ,  3336.10999736,  3427.21191927,
            3398.82742569,  3383.03902621,  3462.83656572,  3364.93903654,
            3345.60749169,  3396.42179292])
        
        self.data = FPEquilibration(self.filename)
        
        
    def test_Load(self):
        data = self.data
        
        numpy.testing.assert_almost_equal(data.file[0:50,0], self.time_expected)
        numpy.testing.assert_almost_equal(data.file[0:50,1], self.temp_expected)
        numpy.testing.assert_almost_equal(data.file[0:50,2], self.pe_expected)
        numpy.testing.assert_almost_equal(data.file[0:50,3], self.ke_expected)
        
        
    def test_GenerateBlock(self):
        data = self.data
        temp = data.file[:,1]
        
        first_expected = numpy.array([
            477.786, 461.853, 447.444, 438.324, 430.938, 424.518,
            418.559, 404.711, 404.319, 401.353, 395.616, 390.216,
            391.138, 387.516, 383.527])
        
        new_block = data.GenerateBlock(temp)
        
        size_expected = numpy.alen(first_expected)
        
        numpy.testing.assert_almost_equal(new_block[0:size_expected], first_expected, 3)
        
        
    def test_CalculateSquaredVariance(self):
        data = self.data
        temp = data.file[0:50,1]
        
        r2, err = data.CalculateSquaredVariance(temp)
        
        expected_r2 = 16.336
        expected_err = 3.300
        
        self.assertAlmostEqual(r2, expected_r2, 3)
        self.assertAlmostEqual(err, expected_err, 3)
        
        
    def test_CalculateVariance(self):
        data = self.data
        temp = data.file[0:50,1]
        
        r2, err = data.CalculateVariance(temp)   
        
        expected_r2 = numpy.array([16.336, 32.780, 70.536, 146.032, 304.605])
        expected_err = numpy.array([3.300, 9.463, 30.077, 92.359, 304.605])
        
        numpy.testing.assert_almost_equal(r2, expected_r2, 3)
        numpy.testing.assert_almost_equal(err, expected_err, 3)     
        
        
        
        
if __name__ == '__main__':
    unittest.main()