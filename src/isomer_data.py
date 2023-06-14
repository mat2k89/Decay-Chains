import os
import math
from src.element_info import ElementInfo

class IsomerData:
    @classmethod
    def filename_from_nuclear_data(cls, atomic_number, atomic_mass, energy_state=0):
        filename = "dec-{}_{}_{}".format(str(atomic_number).zfill(3), ElementInfo.get_element_symbol_from_atomic_number(atomic_number), str(atomic_mass).zfill(3))

        if energy_state:
            filename += "m{}".format(energy_state)

        filename += ".endf"

        return(filename)
    
    @classmethod
    def isomer_name_from_nuclear_data(cls, atomic_number, atomic_mass, energy_state=0):
        isomer_name = "{}{}".format(ElementInfo.get_element_symbol_from_atomic_number(atomic_number), atomic_mass)

        if energy_state:
            isomer_name += "m{}".format(energy_state)

        return(isomer_name)
    
    @classmethod
    def get_nuclear_data_from_name(cls, isomer_name):
        for i, char in enumerate(isomer_name):
            if char.isnumeric():
                n_char_symbol = i
                break

        symbol = isomer_name[:n_char_symbol]

        atomic_number = ElementInfo.get_atomic_number_from_element_symbol(symbol)

        mass_and_group = isomer_name[n_char_symbol:].split("m")

        atomic_mass = int(mass_and_group[0])

        try:
            energy_state = int(mass_and_group[1])
        except IndexError:
            energy_state = 0

        return(atomic_number, atomic_mass, energy_state)
    
    def __init__(self, filepath):
        with open(filepath) as f:
            lines  = f.readlines()

        #Find the decay rate
        for line in lines:
            if line[:16] == "Parent half-life":
                decay_rate_word = line.split(" ")[2]
                decay_rate_unit = line.split(" ")[3]
                break
        else:
            raise ValueError("No decay rate in this file")
        
        if decay_rate_word == "STABLE":
            self._decay_rate = 0.0
            self._decay_atomic_number_change = 0
            self._decay_atomic_mass_change = 0
            return
        
        self._decay_rate = math.log(2) / float(decay_rate_word)
        match decay_rate_unit:
            case "PS":
                self._decay_rate *= 1e12
            case "NS":
                self._decay_rate *= 1e9
            case "US":
                self._decay_rate *= 1e6
            case "MS":
                self._decay_rate *= 1e3
            case "S":
                pass
            case "M":
                self._decay_rate /= 3.6e3
            case "D":
                self._decay_rate /= 8.64e4
            case "Y":
                self._decay_rate /= 3.1536e7
            case _:
                raise ValueError("Unknown Half-Life Unit '{}'".format(decay_rate_unit))

        # Find the decay mode
        for line in lines:
            if line[:10] == "Decay Mode":
                decay_mode = line.split()[2]
                break
        else:
            raise ValueError("No decay mode in this file")

        match decay_mode:
            case "A":
                self._decay_atomic_number_change = -2
                self._decay_atomic_mass_change = -2
            case "B-":
                self._decay_atomic_number_change = 1
                self._decay_atomic_mass_change = 0
            case "EC":
                self._decay_atomic_number_change = -1
                self._decay_atomic_mass_change = 0
            case _:
                raise ValueError("Unknown decay mode '{}'".format(decay_mode))

    @property
    def decay_rate(self):
        return (self._decay_rate)
    
    @property
    def decay_atomic_number_change(self):
        return (self._decay_atomic_number_change)  
    
    @property
    def decay_atomic_mass_change(self):
        return (self._decay_atomic_mass_change)

