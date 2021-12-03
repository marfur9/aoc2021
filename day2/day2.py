inputfile = open('day2/day2.txt', 'r')
horizontal=0
depth=0
aim=0

for line in inputfile:
    lineParts=line.split()
    if(lineParts[0]=="forward"):
        horizontal+=int(lineParts[1])
        depth+=(aim*int(lineParts[1]))
    elif(lineParts[0]=="down"):
        #depth+=int(lineParts[1])
        aim+=int(lineParts[1])
    elif(lineParts[0]=="up"):
        #depth-=int(lineParts[1])
        aim-=int(lineParts[1])

print(depth*horizontal)