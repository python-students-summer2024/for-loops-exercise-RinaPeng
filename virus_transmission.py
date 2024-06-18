"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""


def calculate_infections(starting_number_infections, reproduction_rate, num_days):
    """
    Predicts the number of infected individuals after a given number of days assuming exponential growth.
    Each day, the number of infections increases by a factor determined by the reproduction rate.
    
    :param starting_number_infections: The initial number of infected individuals.
    :param reproduction_rate: The daily multiplication factor for new infections.
    :param num_days: The total number of days to simulate.
    :return: The estimated number of infected individuals at the end of the simulation, rounded to the nearest integer.
    """
    current_infections = starting_number_infections

    # Loop through each day to calculate the progression of the infection
    for _ in range(num_days):
        current_infections *= reproduction_rate

    # Return the total number of infections rounded to the nearest integer
    return round(current_infections)


