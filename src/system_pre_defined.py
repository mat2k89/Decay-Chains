from system import System
import numpy as np

class SystemPreDefined(System):
    def __init__(self, initial_conditions, decay_rates):
        if len(initial_conditions) != len(decay_rates):
            raise ValueError("There should be the same number of initial conditions as decay rates")
        
        decay_rates = np.array(decay_rates)
        n_isomer = len(decay_rates)

        self._matrix = np.zeros((n_isomer, n_isomer))
        self._matrix[range(n_isomer), range(n_isomer)] = - decay_rates
        self._matrix[range(1, n_isomer), range(n_isomer - 1)] = decay_rates[0:-1]

        if not isinstance(initial_conditions, (list, tuple, np.ndarray)):
            raise TypeError("When providing simple decay rates, the initial conditions must be provided as a list, tuple of Numpy array")
        
        initial_conditions = np.array(initial_conditions)

        if initial_conditions.ndim != 1:
            raise ValueError("When providing simple decay rates, the initial conditions must be one-dimensional")
        
        self._initial_conditions = initial_conditions

        self._isomer_names = np.array(tuple("Isomer {}".format(i) for i in range(initial_conditions.shape[0])))