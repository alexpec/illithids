import numpy
from Scripts.FlyvbjergPetersen_Equilibration import FPEquilibration





class HeatCapacity(object):
    def CalculateHC(self, energyArray, temperature, eneryToSIFactor=4200.0):
        kb = 1.38064852 * 10**-23 #Bolztmann Constant in SI
        
        calculator = FPEquilibration()
        
        r2, err = calculator.CalculateVarianceBlocks(energyArray)
        r,  err = calculator.CalculateStdBlocks(energyArray)
        raise NotImplementedError
        
        
    