'''Edit the functions in this file as you complete the associated tasks.
Each test should utilise aspects of your code to complete the specified task.
These functions will be called by tests in the test suite to ensure you code is working properly.
'''




def task_0_always_return_0():
    '''This function should always return the value zero'''
    return(0)


def task_0_addition(a, b):
    '''This function should return the sum of the parameters a and b'''
    return(a + b)

def task_1a_simple_decay_chain_populations(output_times, initial_number_of_moles, decay_rate):
    '''
    This function should return the populations of two isomers at a number of output times as one decays into the other
    :param output_times: 1-D Numpy array of floats containing the times at which the populations of the isomers should be returned. The first time will always be 0. 
    :param initial_number_of_moles: The initial number of moles of Isomer 1 (the decaying isomer). Isomer 2 (the produced isomer) should have an initial population of 0.
    :param decay_rate: The decay rate of the decaying isomer in units of 1/s.
    :returns: Should be a 2-D Numpy array of size (2, n) where n is the number of output times. The value with index [0, 0] is the population of Isomer 1 at t=0 and [1,n] is the number of moles of Isomer 2 at the end of the simulation.
    '''
    import src.system_pre_defined

    system = src.system_pre_defined.SystemPreDefined([initial_number_of_moles, 0], [decay_rate, 0])

    return(system.y)