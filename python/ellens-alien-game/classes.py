"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    health = 3


    def __init__(self, x_coord, y_coord):

        self.x_coordinate=x_coord
        self.y_coordinate=y_coord
        Alien.total_aliens_created += 1

    def hit(self):
        self.health = max(0, self.health - 1)

    def is_alive(self):
        return self.health>0

    def teleport(self, x_coord, y_coord):
        self.y_coordinate += y_coord
        self.x_coordinate += x_coord
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, location):
        pass



#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(position_data):
    alien_objects = []
    for element in position_data:
        alien_objects.append(Alien(element[0], element[1]))
    return alien_objects
