import numpy
import math


class FPEquilibration(object):
    def GenerateBlock(self, dataset):
        size = numpy.alen(dataset)
        n_ = int(size/2)
        x_ = numpy.zeros(n_)
        
        for i in xrange(n_):
            x_[i] = 0.5*(dataset[2*i]+ dataset[2*i+1])
        
        return x_
    
    
    def CalculateVariance(self, dataset):
        size = numpy.alen(dataset)
        
        mean = numpy.mean(dataset)
        temp_value = numpy.power(dataset - mean,2)
        
        c0 = numpy.sum(temp_value) / size
        
        r2 = c0 / (size -1)
        err = math.sqrt(2.0 / (size - 1)) * c0/(size -1)
        
        return r2, err
    
    
    def CalculateStd(self, dataset):
        size = numpy.alen(dataset)
        
        mean = numpy.mean(dataset)
        temp_value = numpy.power(dataset - mean,2)
        
        c0 = numpy.sum(temp_value) / size
        
        r = math.sqrt(c0 / (size -1))
        err = r * (1.0/math.sqrt(2.0*(size-1)))

        return r, err 
    
    
    def CalculateVarianceBlocks(self, dataset):
        n = numpy.alen(dataset)
        x = numpy.copy(dataset)
        
        
        r2 = []
        err = []
        
        while n >= 2:
            r2_, err_ = self.CalculateVariance(x)
            r2.append(r2_)
            err.append(err_)
            
            x = self.GenerateBlock(x)
            n = numpy.alen(x)
            
        r2 = numpy.array(r2)
        err = numpy.array(err)
        
        return r2, err
    
    def CalculateStdBlocks(self, dataset):
        n = numpy.alen(dataset)
        x = numpy.copy(dataset)
        
        
        r2 = []
        err = []
        
        while n >= 2:
            r2_, err_ = self.CalculateStd(x)
            r2.append(r2_)
            err.append(err_)
            
            x = self.GenerateBlock(x)
            n = numpy.alen(x)
            
        r2 = numpy.array(r2)
        err = numpy.array(err)
        
        return r2, err
    
    
    def CalculateFromBlocks(self, blocks, blocks_err):
        raise NotImplementedError
    
    
    def CalculateMean(self, dataCol):
        raise NotImplementedError