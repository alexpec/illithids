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
    def CalculateAtConstantVolume(self, energyDataset, temperature, energyConversionFactor=1.0):
        kb = 0.0083144621 #Bolztmann Constant in kJ/mol.K
        
        e_2_m = numpy.power(energyDataset, 2)
        e_2_m = numpy.mean(e_2_m)
        
        e_m_2 = numpy.mean(energyDataset)
        e_m_2 = math.pow(e_m_2, 2.0)
        
        dmq = e_2_m - e_m_2
        dmq = dmq * energyConversionFactor
        
        cv = dmq / (kb * math.pow(temperature, 2))
        
        
        return cv
    
    
    def CalculateAtConstantPressure(self, energyDataset, temperature, totalAtoms, energyConversionFactor=1.0):
        kb = 0.0083144621 #Bolztmann Constant in kJ/mol.K
        Na = 6.02214129 * 10**23
        
        cv = self.CalculateAtConstantVolume(energyDataset, temperature, energyConversionFactor)
        cp = cv + (totalAtoms/Na) * kb
        
        return cp
    
    
    def CalculateHeatCapacityIdealGas(self, energyDataset, temperature, energyConversionFactor=1.0):
        c = self.CalculateAtConstantVolume(energyDataset, temperature, energyConversionFactor)
        
        return c
        