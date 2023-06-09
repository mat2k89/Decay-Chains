import unittest
import src.test_interfaces as interface
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Test_1A(unittest.TestCase):
    # The comparison tolerances to be used for these tests
    # They are deliberately quite loose, to keep the focus off technicalities of numerical accuracy of ivp solvers
    relative_tolerance = 1e-2
    absolute_tolerance = 1e-2

    def test_test_non_decaying_parent(self):
        '''
        Tests if the correct answer is returned when the parent isomer doesn't decay at all
        '''
        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(np.arange(0, 100, 1), 1, 0)

        # Calculate the reference result
        reference_result = np.zeros([2, 100])
        reference_result[0,:] = 1

        # Compare the results
        np.testing.assert_allclose(program_result, reference_result, self.relative_tolerance)

    def test_test_decaying_parent_slow_decay(self):
        '''
        Tests if the correct answer is returned when the parent isomer decays relatively slowly
        '''
        # Calculate test parameters
        output_times = np.arange(0, 20, 0.1)
        decay_rate = 1e-3
        initial_value = 10

        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(output_times, initial_value, decay_rate)

        # Calculate the reference result using the analytic solution
        reference_result = np.zeros((2, len(output_times)))
        reference_result[0,:] = initial_value * np.exp(-output_times * decay_rate)
        reference_result[1,:] = initial_value - reference_result[0,:]

        print(reference_result)
        print(program_result)

        # Compare the results
        np.testing.assert_allclose(program_result, reference_result, self.relative_tolerance, self.absolute_tolerance)

    def test_test_decaying_parent_fast_decay(self):
        '''
        Tests if the correct answer is returned when the parent isomer decays relatively slowly
        '''
        # Calculate test parameters
        output_times = np.arange(0, 50, 5)
        decay_rate = 1
        initial_value = 100

        # Calculate the result from the supplied program
        program_result = interface.task_1a_simple_decay_chain_populations(output_times, initial_value, decay_rate)

        # Calculate the reference result using the analytic solution
        reference_result = np.zeros((2, len(output_times)))
        reference_result[0,:] = initial_value * np.exp(-output_times * decay_rate)
        reference_result[1,:] = initial_value - reference_result[0,:]

        # Compare the results
        # As the results tend to zero here where small numerical errors are common, we'll compare the absolute difference, rather than relative difference
        np.testing.assert_allclose(program_result, reference_result, self.relative_tolerance, self.absolute_tolerance)