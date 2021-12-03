inputfile = open('day3/day3.txt', 'r')

positions=[]
linenumber=0
for line in inputfile:
    iterator=0
    
    for char in line:
        try: 
            test = positions[iterator]
            if char == "1":
                positions[iterator]+=1
        except IndexError:
                positions.append(0)
                if char == "1":
                    positions[iterator]+=1
        iterator += 1
    linenumber+=1
iterator=0
for position in positions:
    if position > (linenumber/2):
        positions[iterator] = 1
    elif position < (linenumber/2):
        positions[iterator] = 0
    iterator+=1
positions.pop()
print (positions)

gamma=""
epsilon=""
for position in positions:
    if position==1:
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"
print(gamma)
print(epsilon)

print(int(gamma,2)*int(epsilon,2)) #test