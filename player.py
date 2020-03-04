import numpy as np
import random
from ships import *
from map import Map

class Player:

    # when Player is initialized create individual maps and ships
    def __init__(self, name, ships_left=1):
        self.ships_left = ships_left
        self.mymap = Map()
        self.target_map = Map()
        self.mycarrier = Carrier()
        self.mybattleship = Battleship()
        self.mycruiser = Cruiser()
        self.mysubmarine = Submarine()
        self.mydestroyer = Destroyer()
        self.name = name

        

        

    # Create a function to fire on opposing Player Ships
    def fire(self, Player):
        # Convert command line input to target coordinates
        target = list(input("Please select coordinates to target: "))
        
        if len(target) < 2:
            target.insert(0, "0")
            
        
        target_value = Player.mymap.grid[int(target[0])][int(target[1])]
        

        # Compare target coordinates with value at that location each type of ship 
        # is given a unique value over 100 as a reference to on the map
        if (target_value > 100):
           print("Hit!!! You hit your oppenent's Ship!")
           if target_value == 500:
               Player.mycarrier.ship_life -= 1
               if Player.mycarrier.ship_life == 0:
                 print(f'You sunk {Player.name}\'s {Player.mycarrier.name}!')
                 Player.ships_left -= 1
           Player.target_map.grid[int(target[0])][int(target[1])] = -1
           if target_value == 400:
               Player.mybattleship.ship_life -= 1
               if Player.mybattleship.ship_life == 0:
                 print(f'You sunk {Player.name}\'s {Player.mybattleship.name}!')
                 Player.ships_left -= 1
           Player.target_map.grid[int(target[0])][int(target[1])] = -1
           if target_value == 350:
               Player.mysubmarine.ship_life -= 1
               if Player.mysubmarine.ship_life == 0:
                 print(f'You sunk {Player.name}\'s {Player.mysubmarine.name}!')
                 Player.ships_left -= 1
           Player.target_map.grid[int(target[0])][int(target[1])] = -1
           if target_value == 300:
               Player.mycruiser.ship_life -= 1
               if Player.mycruiser.ship_life == 0:
                 print(f'You sunk {Player.name}\'s {Player.mycruiser.name}!')
                 Player.ships_left -= 1
           Player.target_map.grid[int(target[0])][int(target[1])] = -1
           if target_value == 200:
               Player.mydestroyer.ship_life -= 1
               if Player.mydestroyer.ship_life == 0:
                 print(f'You sunk {Player.name}\'s {Player.mydestroyer.name}!')
                 Player.ships_left -= 1
           Player.target_map.grid[int(target[0])][int(target[1])] = -1
        else:
            print("You missed!")
            Player.target_map.grid[int(target[0])][int(target[1])] = -5
            
            
    # Function to position player's ships on the map
    def position_ship(self, Ship):
        Ship.coordinates = int(input(f'Please submit starting coordinates for your {Ship.name} on the map. Please keep in mind the ship will take up {Ship.ship_length} spaces: '))
        Ship.coordinates = np.where(self.mymap.grid == Ship.coordinates)
        print('\n')
        # Checks to ensure that ship placed on map doesn't run outside of map boundary or into another ship
        direction_of_ship = input("From the starting coordinates please indicate which direction the ship should extend(use: 'up', 'down', 'left', 'right') keep in mind if the ship extends past the bounds of the map or runs into another ship it will be an invalid selection and you will be prompted again? ")
        print('\n')
        if direction_of_ship == 'up': 
            while(int(Ship.coordinates[0] + 1) - Ship.ship_length) < 0 or any(self.mymap.grid[int((Ship.coordinates[0] + 1) - Ship.ship_length):int(Ship.coordinates[0] + 1), int(Ship.coordinates[1])] > 100) == True:
                Ship.coordinates = int(input("Please pick a starting point that allows room for your ship: "))
                Ship.coordinates = np.where(self.mymap.grid == Ship.coordinates)
                
            self.mymap.grid[int((Ship.coordinates[0] + 1) - Ship.ship_length):int(Ship.coordinates[0] + 1), int(Ship.coordinates[1])] = Ship.map_id

        # Checks to ensure that ship placed on map doesn't run outside of map boundary or into another ship
        if direction_of_ship == 'down': 
            while(int(Ship.coordinates[0] - 1) + Ship.ship_length) > 9 or any(self.mymap.grid[int(Ship.coordinates[0]): int(Ship.coordinates[0] + Ship.ship_length), int(Ship.coordinates[1])] > 100) == True:
                Ship.coordinates = int(input("Please pick a starting point that allows room for your ship: "))
                Ship.coordinates = np.where(self.mymap.grid == Ship.coordinates)
            
            self.mymap.grid[int(Ship.coordinates[0]): int(Ship.coordinates[0] + Ship.ship_length), int(Ship.coordinates[1])] = Ship.map_id

        # Checks to ensure that ship placed on map doesn't run outside of map boundary or into another ship
        if direction_of_ship == 'right': 
            while(int(Ship.coordinates[1] - 1) + Ship.ship_length) > 9 or any(self.mymap.grid[int(Ship.coordinates[0]), int(Ship.coordinates[1]) : int(Ship.coordinates[1] + Ship.ship_length)] > 100) == True:
                Ship.coordinates = int(input("Please pick a starting point that allows room for your ship: "))
                Ship.coordinates = np.where(self.mymap.grid == Ship.coordinates)

            self.mymap.grid[int(Ship.coordinates[0]), int(Ship.coordinates[1]) : int(Ship.coordinates[1] + Ship.ship_length)] = Ship.map_id

        # Checks to ensure that ship placed on map doesn't run outside of map boundary or into another ship
        if direction_of_ship == 'left': 
            while(int(Ship.coordinates[1] + 1) - Ship.ship_length) < 0 or any(self.mymap.grid[int(Ship.coordinates[0]), int((Ship.coordinates[1] + 1) - Ship.ship_length) : int(Ship.coordinates[1] + 1)] > 100) == True:
                Ship.coordinates = int(input("Please pick a starting point that allows room for your ship: "))
                Ship.coordinates = np.where(self.mymap.grid == Ship.coordinates)
    
            self.mymap.grid[int(Ship.coordinates[0]), int((Ship.coordinates[1] + 1) - Ship.ship_length) : int(Ship.coordinates[1] + 1)] = Ship.map_id



     


        

                   