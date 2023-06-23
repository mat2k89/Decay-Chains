import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from abc import ABC


class System(ABC):
    '''
    A base class which solves a generic set of equations relating to a system of isomers
    '''
    @property
    def matrix(self):
        '''
        The matrix of coefficients of the system of equations
        '''
        return self._matrix

    @property
    def results(self):
        '''
        The results of the system of equations
        '''
        return self._results

    @property
    def y(self):
        '''
        The populations of isomer as a function of time
        '''
        return self._results.y

    @property
    def t(self):
        '''
        The times at which the populations are calculated
        '''
        return self._results.t

    @property
    def isomer_names(self):
        '''
        The names of the isomers
        '''
        return self._isomer_names

    def solve_system(self, t_eval: np.array):
        '''
        Solves the system of equations
        :param t_eval: np.array[float] The times at which to evaluate the system of equations
        '''
        def derivatives(t, y):
            '''
            The derivatives of the system of equations
            :param t: float The time at which to evaluate the derivatives
            :param y: np.array[float] The populations of the isomers at time t
            '''
            derivative = np.matmul(self.matrix, y)

            return derivative

        # Set up the time span
        t_span = np.array((t_eval[0], t_eval[-1]))

        # Solve the system of equations
        self._results = scipy.integrate.solve_ivp(derivatives, t_span, self._initial_conditions, t_eval=t_eval)

    def plot_results(self):
        '''
        Plots the isomer populations as a function of time
        '''
        plt.plot(self.t, self.y.transpose(), label=self.isomer_names)

        plt.xlabel("Time(s)")
        plt.ylabel("Number of Moles")
        plt.legend()
        plt.show()
