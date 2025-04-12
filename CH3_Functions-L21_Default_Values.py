# www.boot.dev/lessons/3963019a-a8ce-45c0-b988-3e6e4121aa36
# 
# Assignment
# 
# Complete the get_punched and get_slashed
#  functions. They should both:
# 
# Take 2 integers as arguments, health and armor
# Change the armor parameter to have a default value of 0
# 

# get_punched
#  Create a damage variable equal to 50 minus the armor
#  - the armor reduces the damage
#  Create a new_health variable equal to the input health minus damage
#  - we apply the damage
#  Return new_health
# 
# get_slashed
#  Create a damage variable equal to 100 minus the armor
#  Create a new_health variable equal to the input health minus damage
#  Return new_health
# 


def get_punched(health, armor):
    # ?
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor):
    # ?
    damage = 100 - armor
    new_health = health - damage
    return new_health


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)