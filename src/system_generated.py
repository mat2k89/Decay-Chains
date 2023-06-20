from src.system import System
import numpy as np
from src.isomer_data import IsomerData


class SystemGenerated(System):
    def __init__(self, initial_populations, data_path_prefix=None):
        self._isomer_data = {}
        self._data_path_prefix = data_path_prefix

        for isomer_name in initial_populations:
            self._add_isomer_and_daughter_data(isomer_name)

        self._isomer_names = np.array(tuple(self._isomer_data.keys()))

        self._setup_initial_conditions(initial_populations)

        self._setup_matrix()

    def _add_isomer_and_daughter_data(self, isomer_name):
        try:
            self._isomer_data[isomer_name]
            return
        except KeyError:
            isomer_data = IsomerData(isomer_name, self._data_path_prefix)
            self._isomer_data[isomer_name] = isomer_data
            if not isomer_data.stable:
                daughter_isomer_name = isomer_data.daughter_name
                self._add_isomer_and_daughter_data(daughter_isomer_name)

    def _get_isomer_index(self, isomer_name):
        for i, stored_name in enumerate(self._isomer_data):
            if stored_name == isomer_name:
                return i
        else:
            raise ValueError("Isomer name not found")

    def _setup_initial_conditions(self, initial_populations):
        self._initial_conditions = np.zeros(len(self._isomer_data))

        for isomer_name, isomer_population in initial_populations.items():
            i = self._get_isomer_index(isomer_name)
            self._initial_conditions[i] = isomer_population

    def _setup_matrix(self):
        self._matrix = np.zeros([len(self._isomer_data)] * 2)

        for isomer_name in self.isomer_names:
            isomer_data = self._isomer_data[isomer_name]
            decay_rate = isomer_data.decay_rate
            parent_index = self._get_isomer_index(isomer_name)
            daughter_name = isomer_data.daughter_name
            daughter_index = self._get_isomer_index(daughter_name)

            self._matrix[parent_index, parent_index] = -decay_rate
            self._matrix[daughter_index, parent_index] = decay_rate
