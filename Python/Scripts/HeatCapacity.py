




class HeatCapacity(object):
    def __init__(self):
        pass
    
    def _load_file(self, filename):
        raise NotImplementedError
    
    def Calculate(self, temperature):
        raise NotImplementedError
    