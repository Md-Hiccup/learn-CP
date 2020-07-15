"""
Birthday Paradox    -   [https://www.geeksforgeeks.org/birthday-paradox/]

1. How many people must be there in a room to make the probability 100% that at-least two people in the room have same birthday?
Answer: 367 (since there are 366 possible birthdays, including February 29).
The above question was simple. Try the below question yourself.

2. How many people must be there in a room to make the probability 50% that at-least two people in the room have same birthday?
Answer: 23

    Formula =  math.ceil(math.sqrt(2*365*math.log(1/(1-p))))

"""

import math

# Returns approximate number of people for a given probability
def find_bday(p):
    # P(same) = 1 - P(diff)
    # P(diff) = 1 - P(same)
    # P(diff) = Sqrt( 2*365* ln(1/(1-p)) )
    return math.ceil(math.sqrt(2 * 365 * math.log(1 / (1 - p))))


get_val = find_bday(0.50)

print(f'Total People: {get_val}')