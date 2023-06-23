from sample_solution.system import System
import numpy as np


class SystemPreDefined(System):
    '''
    A simple, linear system of isomers with predefined decay rates
    '''
    def __init__(self, initial_conditions: np.array, decay_rates: np.array, isomer_names: np.array = None):
        '''
        :param initial_conditions: np.array[float] The initial populations of the isomers
        :param decay_rates: np.array[float] The decay rates of the isomers
        :param isomer_names: np.array[str] The names of the isomers
        '''

        # Raise an error if the initial conditions and decay rates are not the same length
        if len(initial_conditions) != len(decay_rates):
            raise ValueError("There should be the same number of initial conditions as decay rates")

        # Set up the decay rates and the number of isomers
        decay_rates = np.array(decay_rates)
        n_isomer = len(decay_rates)

        # Set up the matrix
        self._matrix = np.zeros((n_isomer, n_isomer))
        self._matrix[range(n_isomer), range(n_isomer)] = - decay_rates
        self._matrix[range(1, n_isomer), range(n_isomer - 1)] = decay_rates[0:-1]

        # If the initial conditions are not a list, tuple or Numpy array, raise an error
        if not isinstance(initial_conditions, (list, tuple, np.ndarray)):
            raise TypeError("When providing simple decay rates, the initial conditions must be provided as a list, tuple of Numpy array")

        # Convert the initial conditions to a Numpy array
        self._initial_conditions = np.array(initial_conditions)

        # If the initial conditions are not one-dimensional, raise an error
        if self._initial_conditions.ndim != 1:
            raise ValueError("When providing simple decay rates, the initial conditions must be one-dimensional")

        if isomer_names:
            # If isomer names are provided, check that they are the same length as the initial conditions
            if len(isomer_names) != len(decay_rates):
                raise ValueError("If isomer_names is provided, it must have the same number of entries as decay_rates.")
            else:
                # Setup isomer names
                self._isomer_names = np.array(isomer_names)
        else:
            # If isomer names are not provided, set them to "Isomer 0", "Isomer 1", etc.
            self._isomer_names = np.array(tuple("Isomer {}".format(i) for i in range(self._initial_conditions.shape[0])))
