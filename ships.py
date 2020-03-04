# DIFFERENT SHIP CLASSES 

class Ship:
    def __init__(self, ship_length, ship_life, coordinates=0):
        self.ship_length = ship_length
        self.ship_life = ship_life
        self.coordinates = coordinates
        

class Carrier(Ship):
    def __init__(self, name="carrier", map_id = 500):
        super().__init__(ship_length=5, ship_life = 5)
        self.name = name
        self.map_id = map_id

class Battleship(Ship):
    def __init__(self, name="battleship", map_id = 400):
        super().__init__(ship_length=4, ship_life = 4)
        self.name = name 
        self.map_id = map_id       

class Cruiser(Ship):
    def __init__(self, name="cruiser", map_id = 300):
        super().__init__(ship_length=3, ship_life = 3)
        self.name = name
        self.map_id = map_id

class Submarine(Ship):
    def __init__(self, name="submarine", map_id = 300):
        super().__init__(ship_length=3, ship_life = 3)
        self.name = name
        self.map_id = map_id


class Destroyer(Ship):
    def __init__(self, name="destroyer", map_id = 200):
        super().__init__(ship_length=2, ship_life = 2)
        self.name = name
        self.map_id = map_id




