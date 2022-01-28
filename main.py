import sys

def transformer(L):
    time = []
    aux = []
    if L[0][0] == '+':
        for i in L[1:]:
            a,b = map(int, i.split('-'))
            a -= int(L[0][1:]) % 24
            b -= int(L[0][1:]) % 24
            t=(a,b)
            aux.append(t)
        time += aux
    else:
        for i in L[1:]:
            a,b = map(int, i.split('-'))
            a += int(L[0][1:]) % 24
            b += int(L[0][1:]) % 24
            t=(a,b)
            aux.append(t)
        time += aux
    return time

t = []
ch = []
lst = []
f = ""

for line in sys.stdin:
    ch = line.split()
    lst = ch[1:]
    t.append(transformer(lst))

for i in range (24):
    j=0
    flag = False
   
    while (flag == False and j < len(t)):    
        k=0
        flag1 = False
        while (flag1 == False and k < len(t[j])):
            if (i in range(t[j][k][0], t[j][k][1])):
                flag1 = True
            k += 1
           
        if (flag1 == True):
            j += 1
        else:
            flag = True
   
   
    if (j == len(t)):
        f += (str(i)+'-'+str(i+1)) + " "

print(f)
