#DAY 1 ADVENT OF CODE

list1 = []
list2 = []
distances = []
total_distance = 0 
#similarity_score = 0

#get input
with open("day1data.txt","r") as file:
    inpt = file.readlines() # list of lines in data file

#split strings
for line in inpt:
    l = line.split("  ")
    list1.append(l[0])
    list2.append(l[1])


#string to int
for i in range(len(list1)):
    list1[i] = int(list1[i])
for i in range(len(list2)):
    list2[i] = int(list2[i])

list1.sort()
list2.sort()


for i in range(len(list1)):
    total_distance += abs(list1[i]-list2[i])

for val1 in list1:
    occurence = 0
    for val2 in list2:
        if val1 == val2:
            occurence += 1
    #similarity_score += (val1 * occurence)

print(f"Total Difference: {total_distance}")
#print(f"Similarity Score: {similarity_score}")