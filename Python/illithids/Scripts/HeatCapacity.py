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
        
        eD = energyDataset * energyConversionFactor #Put the energy dataset in SI units
        
        dmq = numpy.var(eD)
        
        cv = dmq / (kb * math.pow(temperature, 2))
        
        return cv
    
    
    def CalculateAtConstantPressure(self, energyDataset, temperature, totalAtoms, energyConversionFactor=1.0):
        kb = 0.0083144621 #Bolztmann Constant in kJ/mol.K
        eD = energyDataset * energyConversionFactor #Put the energy dataset in SI units
        
        cv = self.CalculateAtConstantVolume(eD, temperature, 1.0)
        cp = cv + (totalAtoms) * kb
        
        return cp
    
    
    def CalculateHeatCapacityIdealGas(self, energyDataset, temperature, energyConversionFactor=1.0):
        c = self.CalculateAtConstantVolume(energyDataset, temperature, energyConversionFactor)
        
        return c
        