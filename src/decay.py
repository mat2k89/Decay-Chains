def decay_model(output_times: list, initial_number_of_moles: float, decay_rate: float):

    import numpy as np

    isomer_1_results = []
    isomer_2_results = []    
    for time in output_times:
        isomer_1_results.append(initial_number_of_moles * np.exp(-decay_rate * time))
        isomer_2_results.append(initial_number_of_moles - initial_number_of_moles * np.exp(-decay_rate * time))

    return isomer_1_results, isomer_2_results