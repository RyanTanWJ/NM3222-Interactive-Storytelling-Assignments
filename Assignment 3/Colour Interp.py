import math
def interp(lst, lst2, div):
    r=math.ceil((lst2[0]-lst[0])/(div-2))
    g=math.ceil((lst2[1]-lst[1])/(div-2))
    b=math.ceil((lst2[2]-lst[2])/(div-2))
    for i in range(1,(div-1)):
        print(str(lst[0]+r*i)+","+str(lst[1]+g*i)+","+str(lst[2]+b*i))

