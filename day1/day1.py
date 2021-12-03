inputfile = open('day1/day1.txt', 'r')
answer = 0
currentNum=0
prevNum=0
#lines = input.readlines()

for line in inputfile:
    currentNum=int(line)
    if(prevNum == 0):
        print("start")
        prevNum=currentNum
    elif(prevNum<currentNum):
        answer += 1
        prevNum=currentNum
    elif(prevNum>currentNum):
        prevNum=currentNum
    elif(prevNum==currentNum):
        print("same depth") 

print(answer)   
