from typing_extensions import Self
import numpy as np

class DenseLayer():

    units = np.empty()
    activation = ''
    imput_shape = []

    def __init__(self):
        self.units = np.empty(100,dtype=np.float64)
