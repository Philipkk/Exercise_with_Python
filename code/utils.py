import numpy as np

class StandardScore:
    """Implement standardization with numpy.
    
    When instance of this class is created it will initialize an empty
    instance. The mu and sigms will be computed until fit() is called.

    transform() will output standardized results as a numpy array.

    fit_transform() will process fit() and transform() in one go.
    """
    
    def __init__(self):
        """Initialization."""
        pass
        
    def fit(self, arr):
        """Convert input as numpy array, then calculate the mu and sigma."""
        self.arr = np.array(arr)
        self.mu = self.arr.mean()
        self.sigma = self.arr.std()

    def transform(self):
        """Perform standardization ."""
        return np.array([(i - self.mu)/self.sigma for i in self.arr])

    def fit_transform(self, arr):
        """Fit to data, followed by standardization."""
        
        self.fit(arr)
        return self.transform()

