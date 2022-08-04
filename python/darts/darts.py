import math

def score(x, y):

    """
    :param x
    :param y
    :return earned points in a darts match
    """ 
    
    position = math.sqrt((x**2)+(y**2))

    if position > 10:
        return 0
    elif position > 5:
        return 1
    elif position > 1:
        return 5
    else:
        return 10
