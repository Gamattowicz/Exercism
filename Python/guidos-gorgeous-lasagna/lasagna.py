EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate the total preparation time.

    :param layers: int number of layers.
    :return: int total preparation time for a given number of layers.

    Function that takes the number of layers of lasagna and returns the number
    of minutes needed to prepare it based on 'PREPARATION_TIME'.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total time needed to prepare and bake lasagna in minutes.

    :param layers: int number of layers.
    :param elapsed_bake_time: int time needed for baking in minutes.
    :return: int total time needed to prepare and bake lasagna in minutes.

    Function that takes the preparation and baking times and return the total needed time in
    minutes.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
