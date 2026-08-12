def calculate_power(voltage, current, power_factor):
    """
    Calculate active power in kW.
    P = V × I × PF
    """
    return (voltage * current * power_factor) / 1000


def calculate_energy(power_kw, hours):
    """
    Calculate energy consumption in kWh.
    """
    return power_kw * hours