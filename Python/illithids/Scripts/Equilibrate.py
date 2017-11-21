import numpy
import math




class Equilibrate(object):
    '''
    Implements the Automatic Equilibration Detection Method from:
    
    Chodera, J.D (J.Chem.Theory.Comput. 12(4) - 2016) - doi: 10.1021/acs.jctc.5b00784
    
    that gets a simple method to detect the best correlation between the data in order to aquire the
    best bias and variance tradeoff.
    '''
    
    def CalculateCorrelation(self, dataset, tau):
        '''
        Calculates the correlation a_n*a_(n+t)
        
        :param dataset: {numpy.array} 
                The dataset where the correlation will be calculated
        :param tau: {int}
                The offset that will be used in the dataset
        '''
        locDataset = numpy.copy(dataset)
        size = numpy.alen(dataset)
        c = numpy.zeros(size-tau)
        
        for i in xrange(size-tau):
            c[i] = locDataset[i] * locDataset[i+tau]
            
        return c
    
    
    
    def CalculateCt(self, dataset, tau):
        
        mean = self.CalculateCorrelation(dataset, tau)
        mean = numpy.mean(mean)
        
        size = numpy.alen(mean)
        
        a_2_n = numpy.power(dataset,2)
        a_2_n = numpy.mean(a_2_n)
        
        a_n_2 = numpy.mean(dataset)
        a_n_2 = math.pow(a_n_2, 2.0)
         
        c = (mean - a_n_2) / (a_2_n - a_n_2)
            
        return c        
    
    
    def CalculateTau(self, dataset, tau):
        size = numpy.alen(dataset)
        t_size = size - tau
        
        ct = numpy.zeros(t_size)
        
        for i in xrange(tau,size):
            ct[i - tau] = self.CalculateCt(dataset, i)
        
        taui = numpy.linspace(tau, size-1, t_size)
        taui = taui/size
        taui = numpy.ones(t_size) - taui
        taui = taui * ct
        taui = numpy.sum(taui)
        return taui
    
    
    def CalculateG(self, dataset, tau):
        taui = self.CalculateTau(dataset, tau)
        g = 1.0 + 2.0*taui
        
        return g
    
    
    def CalculateNeff(self, dataset, tau):
        size = numpy.alen(dataset)
        g = self.CalculateG(dataset, tau)
        
        
        neff = (size - tau + 1) / g
        return neff
    
    
    def CalculateEquilibrationPoint(self, dataset, offset=1):
        size = numpy.alen(dataset)
        if offset < 1 or offset >= size:
            raise Exception("offset must be greater than 1 and lesser than %i" %(size-1))
        
        
        totalIndexes = numpy.linspace(1,size-1,size-1)
        indexes = numpy.where(totalIndexes % offset == 0)[0]
        
        neffWithOffset = numpy.zeros(numpy.alen(indexes))
        
        for idx, i in enumerate(indexes):
            tau = int(totalIndexes[i])
            neffWithOffset[idx] = self.CalculateNeff(dataset, tau)
        
        neffIndex = indexes[numpy.argmax(neffWithOffset)]
        
        return int(totalIndexes[neffIndex])
        
        
        
        
        raise NotImplementedError