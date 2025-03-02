import random

data = None
rules = []
updates = []
sum_of_middle_vals = 0
sum_of_incorrect_middle_vals = 0

class Rule():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hasValue(self, int):
        if self.x == int or self.y == int:
            return True
        return False
    
    def isValid(self, update):
        try: 
            x_index = update.index(self.x)
            y_index = update.index(self.y)
            if x_index > y_index: #make sure it follows the rule that x is before y
                return False
            return True
        except: #if both vals are not in the list the rule does not apply
            return True

#populate data

with open("day5data.txt","r") as file:
    data = file.readlines()

for line in data:
    if data.index(line) < 1176:
        rules.append(Rule(int(line.split("|")[0]),int(line.split("|")[1])))
    elif data.index(line) > 1176:
        updates.append(line.split(","))

for i in range(len(updates)): #updates to int
    for ii in range(len(updates[i])):
        updates[i][ii] = int(updates[i][ii])


def getMiddle(update):
    return update[int(len(update)/2)]

def rulesWithValue(value):
    l = []
    for rule in rules:
        if rule.hasValue(value):
            l.append(rule)
    return l

def passAllRules(update):
    for value in update:
        for rule in rulesWithValue(value):
            if (rule.isValid(update)):
                pass
            else:
                return False
    return True

def generate_permutations(sequence, current=[]):
    if not sequence:
        if passAllRules(current):
            return current
    else:
        for i in range(len(sequence)):
            # Fix one element (sequence[i]) and permute the rest (sequence[:i] + sequence[i+1:])
            generate_permutations(sequence[:i] + sequence[i+1:], current + [sequence[i]])

# Example usage
numbers = [1, 2, 3]
generate_permutations(numbers)


def reorganizeUpdate(update):
    c = generate_permutations(update)
    print(f"Update Fixed: {c}")
    return c

#actual check
for update in updates:
    if passAllRules(update):
        sum_of_middle_vals += getMiddle(update)
    else:
        sum_of_incorrect_middle_vals += getMiddle(reorganizeUpdate(update))
    
print(f"Sum: {sum_of_middle_vals}")
print(f"Sum Incorrect: {sum_of_incorrect_middle_vals}")