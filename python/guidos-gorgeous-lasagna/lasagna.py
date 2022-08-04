# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME=40
# TODO: consider defining the 'PREPARATION_TIME' constant 
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME_PER_LAYER=2


# define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time:int):

    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

# def 'preparation_time_in_minutes()' function  
def preparation_time_in_minutes(layers):

    """Function that takes the actual minutes the lasagna has been in the oven""" 
    return layers * PREPARATION_TIME_PER_LAYER

# def 'elapsed_time_in_minutes
def elapsed_time_in_minutes(layers:int, bake_time):

    """Function should return the total number of minutes you've been cooking"""
    prep_time = preparation_time_in_minutes(layers)

    return prep_time + bake_time
