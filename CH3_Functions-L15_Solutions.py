# www.boot.dev/lessons/6b3ce0b8-b323-4685-bf50-48cfd1c9959d
# 
# Assignment
# 

# Enough about solution mechanics, let's
#  write more code.
# 

# We need to display the current
#  time to our players. The problem is that the time is
#  stored as a number of hours, but we want to display
#  it as a number of seconds. There are 60 seconds in
#  a minute, but how many are in an hour?
# 

# Complete
#  the hours_to_seconds function. It should convert hours
#  to seconds and return the result.                 
# 
# 
def hours_to_seconds(hours):
    # ?
        return hours * 60 * 60

# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)
