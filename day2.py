levels = []

num_safe = 0

with open("day2data.txt","r") as file:
    levels = file.readlines()

for i in range(len(levels)):
    levels[i] = levels[i].split(" ") #split level into different strs
    for ii in range(len(levels[i])): #convert vals to ints
        levels[i][ii] = int(levels[i][ii])

#return true or false
def isOnlyDecreasingIncreasing(level):
    increasing = False
    if level[0] > level [1]:
        increasing = False
    elif level[0] < level [1]:    
        increasing = True
    else:
        return False
    
    if increasing:
        for i in range(len(level) - 1):
            if(level[i] > level[i+1]):
                return False
    else:
        for i in range(len(level) - 1):
            if(level[i] < level[i+1]):
                return False
    return True


def checkDifferRange(level):
    for i in range(len(level) -1):
        if(abs(level[i] - level[i+1]) > 3 or abs(level[i] - level[i+1]) < 1):
            return False
    return True

def checkLevel(level):
    return isOnlyDecreasingIncreasing(level) and checkDifferRange(level)

for level in levels:
    if(checkLevel(level) == False):
        for i in range(len(level)):
            levelwithoutoneval = level.copy()
            del levelwithoutoneval[i]
            if(checkLevel(levelwithoutoneval) == True):
                num_safe += 1
                break
    else:
        num_safe += 1

print(num_safe)

