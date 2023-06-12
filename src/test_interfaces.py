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
    Edit this function as part of Activity 1A
    This function should return the populations of two isomers at a number of output times as one decays into the other
    :param output_times: 1-D Numpy array of floats containing the times at which the populations of the isomers should be returned. The first time will always be 0. 
    :param initial_number_of_moles: The initial number of moles of Isomer 1 (the decaying isomer). Isomer 2 (the produced isomer) should have an initial population of 0.
    :param decay_rate: The decay rate of the decaying isomer in units of 1/s.
    :returns: Should be a 2-D Numpy array of size (2, n) where n is the number of output times. The value with index [0, 0] is the population of Isomer 1 at t=0 and [1,n] is the number of moles of Isomer 2 at the end of the simulation.
    '''
    import src.system_pre_defined

    system = src.system_pre_defined.SystemPreDefined([initial_number_of_moles, 0], [decay_rate, 0])

    system.solve_system(output_times)

    return(system.y)

def task_1c_endf_file_names_from_nuclear_data(atomic_number, atomic_mass, energy_state):
    '''
    Edit this function as part of Activity 1C
    This function should accept the nuclear data of a isomer and return the corresponding endf file name (without any preceding path)
    Note, you do not need to check if the file actually exists
    :param atomic_number: int providing the atomic number 
    :param atomic_mass: int providing the atomic mass
    :param energy state: int providing the energy_state_number 
    :returns: Should be a string containing the endf filename  corresponding to the nuclear data (without any preceding path), e.g. dec-006_C_016
    '''

    import src.isomer_data

    return(src.isomer_data.IsomerData.filename_from_nuclear_data(atomic_number, atomic_mass, energy_state))