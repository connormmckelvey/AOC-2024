amt_of_xmas = 0
amt_of_mas = 0
data = []
xmas = "XMAS"
xsize = 0
ysize = 0

#get lines from data
with open("day4data.txt","r") as file:
    data = file.readlines()

#data is now 2d array of characters
for i in range(len(data)):
    newline = []
    for chr in data[i]:
        newline.append(chr)
    data[i] = newline

for i in range(len(data)):
    if i != 139:
        del data[i][-1]

xsize = len(data[0]) #140
ysize = len(data) #140

print(data[139])

def checkUp(x,y):
    for i in range(3):
        if (y - (i + 1) < 0):
            return False
        if(data[y - (i + 1)][x] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkDown(x,y): #(7,139)
    for i in range(3): # 0, 1, 2
        if (y + (i + 1) >= ysize): # y must be < 140
            print(f"Out of Bounds: Y: {y + (i + 1)} {x} {xsize}")
            return False
        if(data[y + (i + 1)][x] == xmas[i + 1]): #xmas index of 1,2,3
            pass
        else:
            return False
    return True

def checkLeft(x,y):
    for i in range(3):
        if(x - (i + 1) < 0):
            return False
        if(data[y][x - (i + 1)] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkRight(x,y):
    for i in range(3):
        if(x + (i + 1) >= xsize):
            return False
        if(data[y][x + (i + 1)] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkUpLeft(x,y):
    for i in range(3):
        if(x - (i + 1) < 0 or y - (i + 1) < 0):
            return False
        if(data[y - (i + 1)][x - (i + 1)] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkUpRight(x,y):
    for i in range(3):
        if(x + (i + 1) >= xsize or y - (i + 1) < 0):
            return False
        if(data[y - (i + 1)][x + (i + 1)] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkDownLeft(x,y):
    for i in range(3):
        if(x - (i + 1) < 0 or y + (i + 1) >= ysize):
            return False
        if(data[y + (i + 1)][x - (i + 1)] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkDownRight(x,y):
    for i in range(3):
        if(x + (i + 1) >= xsize or y + (i + 1) >= ysize):
            return False
        if(data[y + (i + 1)][x + (i + 1)] == xmas[i + 1]):
            pass
        else:
            return False
    return True

def checkMASX(x,y):
    if(x - 1 < 0 or x + 1 >= xsize or y - 1 < 0 or y + 1 >= ysize):
        return False
    if(checkLRX(x,y) and checkRLX(x,y)):
        return True

    
def checkLRX(x,y):
    if data[y - 1][x - 1] == "M":
        if data[y + 1][x+1] == "S":
            return True
        else:
            return False
    elif data[y-1][x-1] == "S":
        if data[y + 1][x+1] == "M":
            return True
        else:
            return False
    else:
        return False

def checkRLX(x,y):
    if data[y - 1][x + 1] == "M":
        if data[y + 1][x-1] == "S":
            return True
        else:
            return False
    elif data[y-1][x+1] == "S":
        if data[y + 1][x-1] == "M":
            return True
        else:
            return False
    else:
        return False

for i in range(len(data)): #y (7,139)
    for ii in range(len(data[i])): #x
        if data[i][ii] == xmas[2] and checkMASX(ii,i):
            amt_of_mas += 1
        elif data[i][ii] == xmas[0]:
            print(f"Y: {i} X: {ii}")
            if checkUp(ii, i):
                amt_of_xmas += 1
            if checkDown(ii, i):
                amt_of_xmas += 1
            if checkRight(ii, i):
                amt_of_xmas += 1
            if checkLeft(ii, i):
                amt_of_xmas += 1
            if checkUpRight(ii, i):
                amt_of_xmas += 1
            if checkUpLeft(ii, i):
                amt_of_xmas += 1
            if checkDownRight(ii, i):
                amt_of_xmas += 1
            if checkDownLeft(ii, i):
                amt_of_xmas += 1

print(amt_of_xmas)
print(amt_of_mas)

