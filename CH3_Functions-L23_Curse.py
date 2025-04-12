# www.boot.dev/lessons/cb3a6f03-90e6-46d7-8647-6c271c05a108
#   
# Assignment
# 

# Complete the curse function. It accepts a weapon_damage parameter
# and returns two values:
# 
# The lesser_cursed damage: reduce the input weapon_damage
# from 100% to 50% (50% reduction).
#    
# The greater_cursed damage: reduce the input weapon_damage from 100% to
# 25% (75% reduction).
# 

# A greater curse is more powerful than a lesser curse, 
# so it reduces the damage more.

def curse(weapon_damage):
    # ?
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25
    return lesser_cursed, greater_cursed




# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()
