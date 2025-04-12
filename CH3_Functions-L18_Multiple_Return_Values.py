# www.boot.dev/lessons/3c5fe40f-41e3-4d7e-a035-be67c8d83536
# 
# 
#  Complete the become_warrior function. It accepts 2
#  inputs: the full_name string, and the power integer.
#  It should return 2 values: a "title" string and a "new
#  power" integer.
# 

# Create the title using f-strings.
#  Combine full_name with "the warrior" in this format:
#       full_name  the warrior
# 

# Create the new_power value that is equal to the input power plus one.
# Return both  title and new_power
# 

def become_warrior(full_name, power):
    # ?
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power


# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()
