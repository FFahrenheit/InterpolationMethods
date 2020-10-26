epsilon = 4

def main():
    print("\t\tDiferencias finitas\n\n")
    data = [[50,24.94],
           [60,30.11],
           [70,36.05],
           [80,42.84],
           [90,50.57],
           [100,59.30]]
    
    value = 85

    dif = getFiniteDifferences(data)

    n = len(data)
    
    offset = findOffest(data,value)
    print(offset)
    forward = findDirecion(data,offset)

    if forward:
        polynomials = n - 1 - offset
    else:
        offset += 1
        polynomials = offset 

    
    s = getS(data,value,offset,forward)

    for i in range(polynomials):
        total = data[offset][1]
        print(f"{total} + ", end = '')
        for j in range(i+1):
            if j != 0:
                print(" + ",end='')
            total += getMultiplers(s,j,forward) * getDif(dif,offset,j,forward) / factorial(j+1)
        total = round(total,epsilon)
        print(f" = {total:.4f}")

def getDif(dif,offset,j,forward):
    if forward:
        A = dif[offset][j+1]
    else:
        A = dif[offset-j-1][j+1]
    print("(%.4f)"%A,end='')
    return A

def factorial(n):
    t = 1
    for i in range(1,n+1):
        t *= i
    print(f"/{n}!",end='')
    return t

def getMultiplers(s,n,direction):
    t = 1
    for i in range(n+1):
        if direction:
            t *= (s-i)
            if i == 0:
                print("%.4f"%s,end='')
            else:
                print("(%.4f - %d)"%(s,i),end='')
        else:
            t *= (s+i)
            if i == 0:
                print("%.4f"%s,end='')
            else:
                print("(%.4f + %d)"%(s,i),end='')
    return t

def getS(data,value,off,direction):
    if direction: #Depending of whether is forwards or backwards 
        h = abs(data[off][0] - data[off+1][0])
        print(f"s = ({value} - {data[off][0]})/{h} = ",end='')
        s = (value - data[off][0])/(h)
    else:
        h = abs(data[off][0] - data[off+1][0])
        print(f"s = ({data[off][0]} - {value})/{h} = ",end='')
        s = (data[off][0] - value)/(h)
    
    print(s,end='\n\n')
    return round(s,epsilon)

def getFiniteDifferences(data):
    n = len(data)
    dif = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(dif)): #Filling with zeros to be able to print defined values
        for j in range(len(dif[0])):
            dif[i][j] = 0
    
    for i in range(n):  #Fill the first column with a0 values f(x) my friends will call it
        dif[i][0] = data[i][1]
    
    for i in range(n):   #Repeat n-1 times because we already have a0 
        diff = i+1 #First iteration we'll need n-1 values, but second time we'll need n-2 rows and so on...
        for j in range(n-diff): 
            print(f"{dif[j+1][i]:.4f} - {dif[j][i]:.4f}")
            ak =  round(dif[j+1][i] - dif[j][i],epsilon)
            print("Δ^%d [%d] = %.4f\n"%(i+1,j,ak))
            dif[j][i+1] = ak
    printMatrix(dif) #Print the resultant matrix
    return dif


def findOffest(data, value):
    n = len(data)
    for i in range(n-1):
        if data[i][0] < value and data[i+1][0] > value:
            return i 
    if data[0][0] > value:
        return 0
    else:
        return n-1

def findDirecion(data,offset):
    if offset < len(data) // 2:
        print("\t\tHacia adelante\n\n")
        return True
    else:
        print("\t\tHacia atras\n\n")
        return False

def printMatrix(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            print("%f"%data[i][j],end='\t')
        print("\n") 

if __name__ == "__main__":
	main()