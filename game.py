from player import *


# ASSIGN PLAYER1 AND PLAYER2
player_1 = input('Player 1 enter your Name: ')
player_1 = Player(player_1.upper())

player_2 = input('Player 2 enter your Name: ')
player_2 = Player(player_2.upper())
print('\n')



# PLACE SHIPS ON MAP
# (2 types of ships have been commented out for time sake feel free to uncomment)

# Place Carriers on Map
# print(f'{player_1.name},\n {player_1.mymap.grid}\n')
# player_1.position_ship(player_1.mycarrier)
# print(f'{player_2.name},\n {player_2.mymap.grid}\n')
# player_2.position_ship(player_2.mycarrier)

# print(f'{player_1.name},\n {player_1.mymap.grid}')
# player_1.position_ship(player_1.mybattleship)
# print(f'{player_2.name},\n {player_2.mymap.grid}')
# player_2.position_ship(player_2.mybattleship)


# Place Cruisers on map
print(f'{player_1.name},\n {player_1.mymap.grid}')
player_1.position_ship(player_1.mycruiser)
print(f'{player_2.name},\n {player_2.mymap.grid}')
player_2.position_ship(player_2.mycruiser)

# print(f'{player_1.name},\n {player_1.mymap.grid}')
# player_1.position_ship(player_1.mysubmarine)
# print(f'{player_2.name},\n {player_2.mymap.grid}')
# player_2.position_ship(player_2.mysubmarine)



# Place Destroyers on map
# print(f'{player_1.name},\n {player_1.mymap.grid}')
# player_1.position_ship(player_1.mydestroyer)
# print(f'{player_2.name},\n {player_2.mymap.grid}')
# player_2.position_ship(player_2.mydestroyer)


# Create while loop to check whether players have ships left 
while player_1.ships_left != 0 and player_2.ships_left != 0:

    print(player_2.target_map.grid)
    print(f'{player_1.name}: ')
    player_1.fire(player_2)
    print('\n')

    print(player_1.target_map.grid)
    print(f'{player_2.name}: ')
    player_2.fire(player_1)
    print('\n')

if player_1.ships_left == 0:
    print(f'{player_2.name} WINS!')
    print(player_1.target_map.grid)
else:
    print(f'{player_1.name} WINS!')
    print(player_2.target_map.grid)

    





