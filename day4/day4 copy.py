inputfile = open('day4/day4.txt', 'r')


paths=[]
answer=0
positions=["0,0-0"]
for inp in inputfile:
    fromvalue = inp.split()[0]
    tovalue = inp.split()[2]
    fromx = fromvalue.split(',')[0]
    fromy = fromvalue.split(',')[1]
    tox = tovalue.split(',')[0]
    toy = tovalue.split(',')[1]

    path = []
    ylength=0
    xlength=0
    pathlength=0
    xascending=False
    yascending=False
    ystill=False
    xstill=False
    if fromy > toy:
        ylength=int(fromy)-int(toy)
    elif fromy < toy:
        ylength=int(toy)-int(fromy)
        yascending=True
    elif fromy==toy:
        ystill=True
    if fromx > tox:
        xlength=int(fromx)-int(tox)
    elif fromx < tox:
        xascending=True
        xlength=int(tox)-int(fromx)
    elif fromx==tox:
        xstill=True
    if xlength>ylength:
        pathlength=xlength
    elif xlength<=ylength:
        pathlength=ylength
    
    running=True
    i=1
    currentvalue=fromvalue
    currentx=int(fromx)
    currenty=int(fromy)
    path.append(currentvalue)
    while(running):
        if xascending and not xstill:
            currentx+=1
        elif not xascending and not xstill:
            currentx-=1
        if yascending and not ystill:
            currenty+=1
        elif not yascending and not ystill:
            currenty-=1
        
        currentvalue=str(currentx)+","+str(currenty)
        paths.append(currentvalue)
        i+=1
        if i>pathlength:
            running=False
    #paths.append(path)


print(paths)


for path in paths:
    for position in path:
        found=False
        for i, visitedpos in enumerate(positions):
            visitedposPosition=visitedpos.split("-")[0]
            visitedposvalue=int(visitedpos.split("-")[1])
            if visitedpos.split("-")[0] == position:
                found=True
                visitedposvalue = visitedposvalue + 1
                positions[i]=visitedposPosition+"-"+str(visitedposvalue)
                if visitedposvalue == 2:
                    print(positions[i])
                    answer+=1
        if not found:
            positions.append(position+"-1")
print(positions)
print(answer)
