
# www.boot.dev/lessons/64266f19-9783-44c1-b63b-01f40ae9a0b8 
#

#
# Assignment

# We need to calculate the total damage
# from a combo of three damaging attacks. Complete the
# triple_attack function by returning the sum of its
# parameters, damage_one, damage_two, and damage_three.

# The attacks (attack_one to attack_six) are already passed
# to two triple_attack functions for you, so you do not
# need to use them directly in the function.        

#


def triple_attack(damage_one, damage_two, damage_three):
    total = damage_one + damage_two + damage_three
    return total


# Don't touch below this line

# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")
