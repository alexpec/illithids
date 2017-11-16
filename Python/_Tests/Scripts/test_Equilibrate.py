import unittest
from Scripts.Equilibrate import Equilibrate
import numpy
import os



class Test_Equilibrate(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.dataset = numpy.array([
            4636.8385824077, 2600.5847083676, 2716.9130888535, 2648.9129249321, 2707.6731324386, 2670.6155267129,
            2710.4118917329, 2690.4431837054, 2701.8840865962, 2758.5682989772, 2590.8720943699, 2634.2276235889,
            2710.5225428299, 2691.4322618442, 2562.2949282602, 2683.6470421026, 2725.3395846885, 2699.3081445341,
            2655.5106446149, 2643.9308741746, 2660.9996910866, 2705.8522257991, 2660.6525646283, 2714.7873050384,
            2739.6248876386
        ])
        
        
        self.calculator = Equilibrate()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_CalculateCorrelation(self):
        calculator = self.calculator
        
        exp_c01 = numpy.array([
            12058491.5125782, 7065562.63283606, 7196866.1969811, 7172390.35700794, 7231153.90875383, 7238468.08184906,
            7292209.19914673, 7269265.62394481, 7453331.7887952, 7147097.62623347, 6824946.84017474, 7140133.35668279,
            7295187.81822834, 6896243.23427914, 6876295.2052198, 7313849.51517434, 7356531.33757080, 7168041.51090608,
            7020986.57999655, 7035499.23943275, 7200271.9369773, 7199332.66407757, 7223105.80557096, 7437498.86552869

        ])
        
        exp_c12 = numpy.array([
            12568255.5050794, 6999297.5837592, 6961532.62809287, 7108747.33578132, 7379328.77023234, 7208814.24217533,
            7197527.62978752, 7113345.7986111, 7189712.71978426, 7464278.17180616, 6893410.48250930, 7151367.71110059,
            7425815.01684228
        ])
        
        exp_c20 = numpy.array([
            12338626.0354052, 7036797.92151544, 7228761.77773026, 7191235.18075785, 7418008.70121921 
        ])
        
        exp_c24 = numpy.array([12703198.3803271])
        
        
        c_01 = calculator.CalculateCorrelation(self.dataset, 1)
        c_12 = calculator.CalculateCorrelation(self.dataset, 12)
        c_20 = calculator.CalculateCorrelation(self.dataset, 20)
        c_24 = calculator.CalculateCorrelation(self.dataset, 24)
        
        numpy.testing.assert_almost_equal(c_01, exp_c01, 3)
        numpy.testing.assert_almost_equal(c_12, exp_c12, 3)
        numpy.testing.assert_almost_equal(c_20, exp_c20, 3)
        numpy.testing.assert_almost_equal(c_24, exp_c24, 3)

    
    def test_CalculateCt(self):
        calculator = self.calculator
        locDataset = self.dataset
        
        expec_ct = numpy.array([
           -1.477291927, -1.3209198232,  -1.3040913761, -1.1882529109,
           -1.147202335, -0.9903910279,  -0.9051873286, -0.8174341346,
           -0.720321353, -0.8324505783,  -0.3830000531, -0.0737304235,
            0.042644508,  0.2009078624,   1.0349012985,  1.3545450527,
            1.684243519,  2.1649567639,   2.9504462850,  4.3004253030, 
            6.188382919,  9.0144226686,  15.1037917905, 34.1636365690 
        ])
        
        size = numpy.alen(expec_ct)
        ct = numpy.zeros(size)
        
        for i in xrange(1, size+1):
            ct[i-1] = calculator.CalculateCt(locDataset, i)
        
        
        numpy.testing.assert_almost_equal(ct, expec_ct, 3)
        
        

    
    
    def test_CalculateTau(self):
        calculator = self.calculator
        locDataset = self.dataset
        
        expec_taui = numpy.array([
            -0.500, 0.918, 2.133, 3.281, 4.279, 5.197, 5.950, 6.601,
             7.157, 7.618, 8.118, 8.332, 8.371, 8.350, 8.262, 7.848,
             7.360, 6.821, 6.215, 5.507, 4.647, 3.657, 2.575, 1.367
        ])
        
        size = numpy.alen(expec_taui)
        taui = numpy.zeros(size)
         
        for i in xrange(1, size+1):
            taui[i-1] = calculator.CalculateTau(locDataset, i)

        numpy.testing.assert_almost_equal(taui, expec_taui, 3)
        
        

    def test_CalculateG(self):
        calculator = self.calculator
        locDataset = self.dataset
        
        exp_g = numpy.array([
           1.69642078e-13,  2.8364004998,  5.2668929744,  7.5620937964,  9.5583586867, 11.3938824242, 12.8992767866, 
           14.2027465398, 15.3144569628, 16.2364682951, 17.2354089891, 17.6643690487, 17.7410486891, 17.7001099608,
           17.5233110418, 16.6953900030, 15.7201175650, 14.6422017123, 13.4298259245, 12.0136117077, 10.2934415865,
            8.3131590525,  6.149697612,   3.7330909255 
        ])
        
        size = numpy.alen(exp_g)
        g = numpy.zeros(size)
         
        for i in xrange(1, size+1):
            g[i-1] = calculator.CalculateG(locDataset, i)

        
        numpy.testing.assert_almost_equal(g, exp_g, 3)
        
        
        
    def test_CalculateNeff(self):
        calculator = self.calculator
        locDataset = self.dataset
        
        exp_neff = numpy.array([
         299441464585804.25, 8.4614284907, 4.3669009626, 2.9092471731, 2.1970299178, 1.7553279256, 1.4729507952, 
               1.2673605031, 1.1100622138, 0.9854359772, 0.8703013668, 0.7925559051, 0.7327638984, 0.6779618899,
               0.6277352479, 0.5989677389, 0.5725148023, 0.5463659194, 0.5212279027, 0.4994334881, 0.4857461868, 
               0.4811648586, 0.487828864, 0.5357490723
        ])
        
        size = numpy.alen(exp_neff)
        neff = numpy.zeros(size)
         
        for i in xrange(1, size+1):
            neff[i-1] = calculator.CalculateNeff(locDataset, i)

        numpy.testing.assert_almost_equal(neff, exp_neff, 3)
        
        
    def test_CalculateEquilibrationPoint(self):
        calculator = self.calculator
        locDataset = self.dataset
        
        self.assertRaises(Exception, calculator.CalculateEquilibrationPoint, *[locDataset, 0])
        
        self.assertRaises(Exception, calculator.CalculateEquilibrationPoint, *[locDataset, 25])

        tau_1_expec = 1
        tau_1 = calculator.CalculateEquilibrationPoint(locDataset, 1)
        self.assertEqual(tau_1_expec, tau_1)
        
        tau_2_expec = 2
        tau_2 = calculator.CalculateEquilibrationPoint(locDataset, 2)
        self.assertEqual(tau_2_expec, tau_2)
        
        
    def test_Bigdata(self):
        main_path = os.path.dirname(os.path.abspath(__file__))
        filename = '%s/docs/water_full_300K.txt' %main_path
        bigDataset = numpy.loadtxt(filename, numpy.float, '#', ';')
        
        calculator = self.calculator
        dataset = bigDataset[:,3]
        
        exp_t0 = 1000
        t0 = calculator.CalculateEquilibrationPoint(dataset, 1000)
        
        self.assertEqual(exp_t0, t0)
        

if __name__ == '__main__':
    unittest.main()