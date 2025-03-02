final_sum = 0
datalist = []
data = ""
do_mul = True

with open("day3data.txt", "r") as file:
    datalist = file.readlines()

for line in datalist:
    data += line

#s is a string with length 12 characters
#false if not instructions, else returns mul(x,y)
def tryInstructions(s: str):
    n1 = ""
    n2 = ""
    comma_index = 7
    if(s[0:4] == "mul("):
        #getting the first number
        nums_1 = s[4:7]
        for i in range(3):
            if nums_1[i].isnumeric():
                n1 += nums_1[i]
            elif nums_1[i] == "," and i != 0:
                comma_index = i + 4
                break #number one done, reached comma
            else:
                return False #not a number or comma, or the first position is a comma
        nums_2 = s[comma_index+1:comma_index+5]
        for i in range(4):
            if i == 3 and nums_2[i] == ")":
                break
            elif i == 3 and nums_2 != ")":
                return False
            elif nums_2[i].isnumeric():
                n2 += nums_2[i]
            elif nums_2[i] == ")" and i != 0:
                break
            else:
                return False #not a number or comma, or the first position is a comma
        print(f"Found: mul({n1},{n2})")
        return int(n1) * int(n2)
    else:
        return False

for i in range(len(data)):
    result = tryInstructions(data[i:i+12])
    if result == False:
        if data[i:i+4] == "do()":
            do_mul = True
        elif data[i:i+7] == "don't()":
            do_mul = False
    else:
        if do_mul:
            final_sum += result

print(final_sum)