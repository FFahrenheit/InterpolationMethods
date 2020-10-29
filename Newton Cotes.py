epsilon = 4
result = 2.9052

import math

def main():
    print("\t\tNewton Cotes\n\n")
    
    limits = [0 for i in range(2)]

    limits[0] = 0
    limits[1] = math.pi/2  #Limites de valores
    
    n = 4 # = input("Ingrese n:")

    h = round((limits[1] - limits[0])/n,epsilon)

    data = getDots(n,limits)

    print("*"*10,"Trapecio compuesto","*"*10)
    getCompositeTrapeze(data,h)

    print("*"*10,"Simpson 1/3 compuesto","*"*10)
    getSimpson1over3(data,h)

    print("*"*10,"Simpson 3/8 compuesto","*"*10)
    getSimpson3over8(data,h)

def getCompositeTrapeze(data,h):
    total = data[0]
    print(f"{h}/2({data[0]} + 2(",end='')
    for i in range(1,len(data)-1):
        if i!= 1:
            print(" + ",end='')
        print(data[i],end='')
        total += 2*data[i]
    print(f") + {data[len(data)-1]}) = ",end='')
    total += data[len(data)-1]
    total = round(total*h/2,epsilon)
    print(total)
    print(f"ERP = {abs((1-abs(total/result))*100):.4f}")
    return total

def getSimpson1over3(data,h):
    total = data[0]
    n = len(data)
    print(f"{h}/3({data[0]} + 4(",end='')
    for i in range(1,n-1,2):
        if i != 1:
            print(" + ",end='')
        print(data[i],end='')
        total += 4*data[i]
    print(") + 2(",end='')
    for i in range(2,n-2,2):
        if i != 2:
            print(" + ",end='')
        print(data[i],end='')
        total += 2*data[i]
    print(f") + {data[n-1]}) = ",end='')
    total += data[n-1]
    total = round(total*h/3,epsilon)
    print(total)
    print(f"ERP = {abs((1-abs(total/result))*100):.4f}")
    return total

def getSimpson3over8(data,h):
    n = len(data)
    total = data[0]
    print(f"3*{h}/8({data[0]} + 3(",end='')
    for i in range(1,n-1):
        if i % 3 != 0:
            if i != 1:
                print(" + ",end='')
            print(data[i],end='')
            total += 3*data[i]
    print(") + 2(",end='')
    for i in range(1,n-3,1):
        if i != 1:
            print(" + ",end='')
        print(data[i*3],end='')
        total += 2*data[i*3]
    
    print(f") + {data[n-1]}) = ",end='')
    total += data[n-1]
    total = round(3/8*total*h,epsilon)
    print(total)
    print(f"ERP = {((1-abs(total/result))*100):.4f}")
    return total


def getDots(n,limits):

    h = (limits[1] - limits[0])/n

    data = [0 for i in range(n+1)]
    for i in range(len(data)):
        x = h*i
        data[i] = round(getFunction(x),epsilon)
        print(f"a{i} = {round(x,epsilon)}",end='\t')
        print(f"f(a{i}) = {data[i]}")
    return data

def getFunction(x):
    return math.exp(x) *math.sin(x)


    
if __name__ == "__main__":
	main()