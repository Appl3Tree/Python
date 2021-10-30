#!/usr/bin/env python3

###################### Scope ###############################

# Global Scope
print('   Global Scope')
player_health = 10
enemies = 1
def increase_enemies():
    print(f'enemies inside function: {enemies}')
    return enemies + 1

enemies = increase_enemies()
print(f'enemies outside function: {enemies}')

# Modifying Global Scope
print('    Modifying Global Scope')
def global_increase_enemies():
    global enemies
    enemies =+ 1
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')


# Local Scope
print('    Local Scope')
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# There is no Block Scope
print('    There is no Block Scope')
game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Global Constants
print('    Global Constants')
PI = 3.14159
URL = 'https://www.google.com'


