import numpy
import math





#=======================================================================================================================
# HeatCapacity
#=======================================================================================================================
class HeatCapacity(object):
    '''
    Implements the Cp calculation for ideal gas using methodology from:
    Statistical Thermodynamics: Fundamentals and Applications - Normand M. Laurendau - Cambridge - 2005
    '''
    def CalculateAtConstantVolume(self, energyDataset, temperature, molarMass, energyToSIFactor=4200.0):
        kb = 1.38064852 * 10**-23 #Bolztmann Constant in SI
        
        e_2_m = numpy.power(energyDataset, 2)
        e_2_m = numpy.mean(e_2_m)
        
        e_m_2 = numpy.mean(energyDataset)
        e_m_2 = math.pow(e_m_2, 2.0)
        
        dmq = e_2_m - e_m_2
        dmq = dmq * (energyToSIFactor / molarMass)
        
        cv = dmq / (kb * math.pow(temperature, 2))
        
        raise NotImplementedError        
        
    