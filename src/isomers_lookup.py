import math


def convert_half_life_to_decay_rate(half_life_value, half_life_unit):
    # for pico seconds
    if half_life_unit == "PS":
        decay_rate = math.log(2) / (half_life_value * 10**-12)
    # for nano seconds
    elif half_life_unit == "NS":
        decay_rate = math.log(2) / (half_life_value * 10**-9)
    # for micro seconds
    elif half_life_unit == "US":
        decay_rate = math.log(2) / (half_life_value * 10**-6)
    # for milli seconds
    elif half_life_unit == "MS":
        decay_rate = math.log(2) / (half_life_value * 10**-3)
    # for seconds
    elif half_life_unit == "S":
        decay_rate = math.log(2) / half_life_value
    # for minutes
    elif half_life_unit == "M":
        decay_rate = math.log(2) / (half_life_value * 60)
    # for hours
    elif half_life_unit == "H":
        decay_rate = math.log(2) / (half_life_value * 60 * 60)
    # for days
    elif half_life_unit == "D":
        decay_rate = math.log(2) / (half_life_value * 60 * 60 * 24)
    else:
        decay_rate = 0.0

    return decay_rate


def read_endf_file(filename):
    # prepend "decay_data/" to the filename
    filename = "decay_data/" + filename

    with open(filename, "r") as file:
        lines = file.readlines()

    half_life = None
    decay_mode = None
    atomic_number_change = 0
    atomic_mass_change = 0

    for line in lines:
        if line.startswith("Parent half-life"):
            half_life = line.split()[2]
            print(half_life)

            if half_life == "STABLE":
                decay_rate = 0.0
            else:
                half_life_str = line.split()
                half_life_value = float(half_life_str[2])
                half_life_unit = half_life_str[3]
                decay_rate = convert_half_life_to_decay_rate(
                    half_life_value, half_life_unit
                )

        elif line.startswith("Decay Mode"):
            decay_mode = line.split()[2]
            print(decay_mode)

            if decay_mode == "A":
                atomic_number_change = -2
                atomic_mass_change = -4
            elif decay_mode == "B-":
                atomic_number_change = 1
                atomic_mass_change = 0
            elif decay_mode == "EC":
                atomic_number_change = -1
                atomic_mass_change = 0
            elif decay_mode == "SF":
                atomic_number_change = 0
                atomic_mass_change = 0
            else:
                atomic_number_change = 0
                atomic_mass_change = 0

            break

    return decay_rate, atomic_number_change, atomic_mass_change
