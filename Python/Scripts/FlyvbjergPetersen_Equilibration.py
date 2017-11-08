import numpy
import math
import matplotlib.pyplot



class FPEquilibration(object):
    def __init__(self, filename, delimiter=';'):
        '''
        :param filename: {STR} - The file name
        :param delimiter: {STR} - The delimiter of the csv file
        '''
        self.file = numpy.loadtxt(filename, numpy.float, '#', delimiter)
        
        
    def GenerateBlock(self, dataset):
        size = numpy.alen(dataset)
        n_ = int(size/2)
        x_ = numpy.zeros(n_)
        
        for i in xrange(n_):
            x_[i] = 0.5*(dataset[2*i]+ dataset[2*i+1])
        
        return x_
    
    
    def CalculateSquaredVariance(self, dataset):
        size = numpy.alen(dataset)
        
        mean = numpy.mean(dataset)
        temp_value = numpy.power(dataset - mean,2)
        
        c0 = numpy.sum(temp_value) / size
        
        r2 = c0 / (size -1)
        err = math.sqrt(2.0 / (size - 1)) * c0/(size -1)
        
        return r2, err
    
    
    def CalculateVariance(self, dataset):
        n = numpy.alen(dataset)
        x = numpy.copy(dataset)
        
        
        
        r2 = []
        err = []
        
        while n > 2:
            r2_, err_ = self.CalculateSquaredVariance(x)
            r2.append(r2_)
            err.append(err_)
            
            x = self.GenerateBlock(x)
            n = numpy.alen(x)
            
        r2 = numpy.array(r2)
        err = numpy.array(err)
        
        return r2, err
    
    def CalculateEquilibration(self, dataCol):
        dataset = self.file[:,dataCol]
        
        r2, err = self.CalculateVariance(dataset)
        
        r = numpy.sqrt(r2)
        err = numpy.sqrt(err)
        
        return r, err
    
    
    def CalculateMean(self, dataCol):
        dataset = self.file[:, dataCol]
        
        y = numpy.mean(dataset)
        
        return y
        
        
        

if __name__ == '__main__':
    data = FPEquilibration('/home/pecanhaasrp/Desktop/molecular_simulation/water_in_box/energy2.txt')
    equilib_data = 4
    r, err = data.CalculateEquilibration(equilib_data)
    x = numpy.linspace(0, numpy.alen(r), numpy.alen(r))
        
    print data.CalculateMean(equilib_data)
    
    matplotlib.pyplot.figure()
    matplotlib.pyplot.errorbar(x, r, yerr=err)
    matplotlib.pyplot.show()
        
        
        
        
    
        


