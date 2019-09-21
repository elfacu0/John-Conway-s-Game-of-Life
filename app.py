import copy
def get_generation(cells, generations):
    u = []
    for i in range(20):
        u.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    for i in range(len(cells)):
        for l in range(len(cells[i])):
            u[i+4][l+4] = cells[i][l]
    cellsN = copy.deepcopy(u)
    for g in range(generations):
        u = copy.deepcopy(cellsN)
        for i in range(len(u)):
            for l in range(len(u[i])):
                c = 0
                for a in range(-1,2):
                    for b in range(-1,2):
                        try:
                            if(u[i+a][l+b]==1 and i+a>=0 and l+b>=0):
                                c+=1
                                #print(" i = %i l= %i" % (i+a,l+b))
                        except IndexError:
                            pass
                if(u[i][l] == 1):
                    c -= 1
                
                if(u[i][l] == 0 and c==3):
                    cellsN[i][l] = 1
                    
                if(c > 3 or c < 2):
                    cellsN[i][l] = 0
    mini = 99
    minl = 99
    maxi = 0
    maxl = 0
    for i in range(len(cellsN)):
        for l in range(len(cellsN[i])):
            if(l<minl and cellsN[i][l]==1):
                minl = l
            if(l>maxl and cellsN[i][l]==1):
                maxl = l
            if(i<mini and cellsN[i][l]==1):
                mini = i
            if(i>maxi and cellsN[i][l]==1):
                maxi = i
    f = []
    for i in range(maxi-mini+1):
        f.append(cellsN[i+mini][minl:maxl+1])
    return f