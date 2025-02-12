"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_bake_time = input("How many minutes has the lasagna been in the oven?")
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

    


def preparation_time_in_minutes(number_of_layers):
    """ Calculate the preparation time in minutes.
    takes the number of layers of lasagna as an argument and returns the total
    number of minutes needed to prepare the lasagna.
    I assume that each layer takes 2 minutes to prepare.
      
    """
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time




def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.
    takes the number of layers of lasagna and the number of minutes the lasagna 
    has been in the oven as arguments and returns the total number of minutes that have elapsed.
    """
    elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time



bake_time_remaining()