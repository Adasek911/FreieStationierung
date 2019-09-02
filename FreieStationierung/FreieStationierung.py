import math
import numpy as np
RHO = 200 / math.pi

x0 = 5
y0 = 5
ori0 = 5
Liste = []
StrGen = 0.004
RiGen = 0.003
sigma0 = 0.01


class Punkt(object):
       def __init__(self, nr, x, y, ri, s):
           self.X = x
           self.Y = y
           self.RI = ri
           self.S = s
        
           arc = math.atan2(self.Y - y0, self.X - x0) * RHO
           self.ti0 = arc + 400
           #self.ti0 = arc
           self.si0 = math.sqrt((x0 - self.X)*(x0 - self.X) + (y0 - self.Y)*(y0 - self.Y))     
                   

#X0 = 0
#Y0 = 5 
#Ori0 = 5

p1 = Punkt(1,10.40542579,-36.6353169,317.61776,38.0843712054079)
p2 = Punkt(2,40.37045579,-18.48286088,372.666897,44.40033612)
p3 = Punkt(3,25.77614967,-35.403,340.063612,43.7927985)

Liste.append(p1)
Liste.append(p2)
Liste.append(p3)

aMat = np.zeros((6,3))

pMat = np.zeros((6,6))

lVek = np.zeros((6,1))

def Rechnen(Y0, X0, Ori0):
    i = 0
    while i < len(Liste):

        aMat[i][0] = ((Y0 - Liste[i].Y)/Liste[i].S)
        aMat[i][1] = ((X0 - Liste[i].X)/Liste[i].S)
        aMat[i][2] = 0 

        i = i + 1

    i = 0
    while i < len(Liste):

        aMat[i+3][0] = (-(Liste[i].X - X0)/math.pow(Liste[i].S,2))*RHO
        aMat[i+3][1] = ((Liste[i].Y - Y0)/math.pow(Liste[i].S,2))*RHO
        aMat[i+3][2] = -1 

        i = i + 1

    a = 0
    x = 0

    while a < len(Liste):
          while x < len(Liste):
                pMat[a][x] = (math.pow(sigma0,2)/ math.pow(StrGen,2))
                pMat[a+3][x+3] = (math.pow(sigma0,2)/ math.pow(RiGen,2)) 
                x = x + 1
                a = a + 1              

    aMatTrans = np.transpose(aMat)

    b = np.dot(aMatTrans, pMat)

    nMat = np.dot(b, aMat)

    qxxMat = np.linalg.inv(nMat)

    i = 0
    while i < len(Liste):

        lVek[i][0] = (Liste[i].S - Liste[i].si0)
        
        l  = (Liste[i].RI - (Liste[i].ti0 - Ori0))
        if l >= 400:
            return l - 400
        
        lVek[i+3][0] =  l
        i = i + 1

    nVek = np.dot(b,lVek)

    xDach = np.dot(qxxMat, nVek)     
    
    return xDach

for i in range(2):
    B = Rechnen(y0, x0, ori0)    
    xDach = np.array(B)          
    print("xDach ",xDach)    
    print("")
    
    werte0 = np.array([[y0],[x0],[ori0]])      
    print(werte0)
    print("")
    gXdach = np.array([])
    gXdach = werte0 + xDach    
    print(gXdach)
    print("")
    
    y0 = gXdach[0]    
    x0 = gXdach[1]
    ori0 = gXdach[2]
    print(y0, x0, ori0)
    print("")
