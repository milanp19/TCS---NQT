# In this challenge, determine the minimum number of chairs needed to accommodate all cricket players in a new team relaxation room. The room does not have any chairs at the beginning.

# There will be a string of simulations. A combination of four characters describes each simulation:

# C, R, U, and L

# • C - A new player arrives in the room. If there is a chair available, the player takes it. Otherwise, a new one is purchased.

# • R - A player goes to play cricket, freeing up a chair.

# • U - A player arrives at the room after playing. If there is a chair available, the player takes it. Otherwise, a new one is purchased.

# • L - A player leaves the room for practice, freeing up a chair.

# Example:

# Given a string representing the simulations: "CRUL". In this case, the simulation is represented in the below table:

str1 = input()

chairs = 0
chair_avail = 0

for s in str1:
    if s in ["C", "U"]:
        if chair_avail > 0:
            chair_avail -= 1
        else:
            chairs += 1
    else:
        chair_avail += 1
        
print(chairs)