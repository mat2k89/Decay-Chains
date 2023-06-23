from sample_solution.system import System
import numpy as np
from sample_solution.isomer_data import IsomerData


class SystemGenerated(System):
    ''''
    A system of isomers generated from a set of initial populations
    The isomers generated derive from the decay chain of the initial isomers
    '''
    def __init__(self, initial_populations: dict, data_path_prefix: str = None):
        '''
        :param initial_populations: dict[str: float] The initial populations of the isomers
        :param data_path_prefix: str The path to the data files
        '''

        # Set up the dictionary for the isomer data
        self._isomer_data = {}

        # Set up the data path prefix
        self._data_path_prefix = data_path_prefix

        # Add the isomer data for each initial isomer (and daughter, etc.)
        for isomer_name in initial_populations:
            self._add_isomer_and_daughter_data(isomer_name)

        # Set up the isomer names
        self._isomer_names = np.array(tuple(self._isomer_data.keys()))

        # Set up the initial conditions
        self._setup_initial_conditions(initial_populations)

        # Set up the matrix
        self._setup_matrix()

    def _add_isomer_and_daughter_data(self, isomer_name: str):
        '''
        Adds the data for the isomer and its daughter to the system
        This function is recursive, so also adds granddaughters, etc.
        :param isomer_name: str The name of the isomer'''
        try:
            # If the isomer data is already stored, don't add it again
            self._isomer_data[isomer_name]
            return
        except KeyError:
            # If the isomer data is not stored, add it
            isomer_data = IsomerData(isomer_name, self._data_path_prefix)
            self._isomer_data[isomer_name] = isomer_data
            if not isomer_data.stable:
                # If the isomer is not stable, add its daughter
                daughter_isomer_name = isomer_data.daughter_name
                self._add_isomer_and_daughter_data(daughter_isomer_name)

    def _get_isomer_index(self, isomer_name: str):
        '''
        Gets the index of the isomer in the system
        :param isomer_name: str The name of the isomer
        :return: int The index of the isomer
        '''
        for i, stored_name in enumerate(self._isomer_data):
            if stored_name == isomer_name:
                return i
        else:
            # If the isomer name is not found, raise an error
            raise ValueError("Isomer name not found")

    def _setup_initial_conditions(self, initial_populations: dict):
        '''
        Sets up the initial conditions for the system
        :param initial_populations: dict[str: float] The initial populations of the isomers
        '''
        self._initial_conditions = np.zeros(len(self._isomer_data))

        for isomer_name, isomer_population in initial_populations.items():
            i = self._get_isomer_index(isomer_name)
            self._initial_conditions[i] = isomer_population

    def _setup_matrix(self):
        '''
        Sets up the matrix for the system
        '''
        self._matrix = np.zeros([len(self._isomer_data)] * 2)

        for isomer_name in self.isomer_names:
            # Get the relevant data for the isomer
            isomer_data = self._isomer_data[isomer_name]
            decay_rate = isomer_data.decay_rate
            parent_index = self._get_isomer_index(isomer_name)
            daughter_name = isomer_data.daughter_name
            daughter_index = self._get_isomer_index(daughter_name)

            # Set the matrix elements
            self._matrix[parent_index, parent_index] = -decay_rate
            self._matrix[daughter_index, parent_index] = decay_rate
