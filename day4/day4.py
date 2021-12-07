inputfile = open('day4/day4sample.txt', 'r')





for inp in inputfile:
    fromvalue = inp.split()[0]
    tovalue = inp.split()[2]
    fromx = fromvalue.split(',')[0]
    fromy = fromvalue.split(',')[1]
    tox = tovalue.split(',')[0]
    toy = tovalue.split(',')[1]
    