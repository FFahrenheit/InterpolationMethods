""""Use requestData method to fill with your own data
but I recommend to fill it statically in the array"""

epsilon = 4

import math

def main():
    print("\t\tDiferenciacion numerica\n\n")
    
    #        Xn    f(Xn)
    data = [[2000,13.782],
           [2200,12.577],
           [2400,11.565],
           [2600,10.704]]

	#   Valor a encontrar
    x = 2300

    n = len(data)
    polynomials = n-1
    k = getOffset(data,x)

    dif = calculateDividedDiferences(data)
    print("-"*70)

    for i in range(polynomials):
        derivative = math.factorial(i+1)*dif[0][i+1]
        print(f"{i+1}! * {dif[0][i+1]:.4e}")
        print(f"d^{i+1}x/dy^{i+1} = {derivative:.4e}")

    while(True):
        n = int(input("Ingrese el orden del polinomio a evaluar: "))
        m = int(input("Ingrese el numero de diferencia a evaluar: "))
        if n > len(dif)-1 :
            print("Fuera de rango")
            break
        elif m > len(dif[0]) - n:
            print("Fuera de rango")
            break
        else:
            print(f"{math.factorial(n)}*{dif[m-1][n]:.4e}")
            derivative = math.factorial(n)*dif[m-1][n]
            print(f"d^{i+1}x/dy^{i+1} = {derivative}")


#Se asume que la data esta ordenada
def getOffset(data,x):
    n = len(data)
    for i in range(n-1):
        if data[i][0] < x and x < data[i+1][0]:
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

"""
data -> diferencias divididas
limit -> terminos multiplicados
x -> Valor a obtener
"""
def getMultiplication(data,limit,x):
    total = 1
    for i in range(limit+1):
        print(f"({x}-{data[i][0]})",end='')
        total *= (x-data[i][0])
    return total

"""
data => valores de la tabla
term = termino a obtener
n = grado de la diferencia dividida
"""
def getDividedDifference(data,term,n):
    print("(%.4e)"%data[term][n+1],end='')
    return data[term][n+1]

"""
Se calculan las diferencias divididas en un solo 
"""
def calculateDividedDiferences(data):
    n = len(data)
    dif = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(dif)): #Filling with zeros to be able to print
        for j in range(len(dif[0])):
            dif[i][j] = 0
    
    for i in range(n):  #Fill the first column with a0 values f(x) my friends will call it
        dif[i][0] = data[i][1]
    
    for i in range(n):   #Repeat n-1 times because we already have a0 
        diff = i+1 #First iteration we'll need n-1 values, but second time we'll need n-2 rows
        for j in range(n-diff): 
            print("(%.4e-%.4e)/(%d - %d)" % (dif[j+1][i],dif[j][i],data[j+diff][0],data[j][0]))
            ak = (dif[j+1][i] - dif[j][i])/(data[j+diff][0]-data[j][0]) #a[k] calculation 
            if round(ak,epsilon) != 0:
                ak = round(ak,epsilon)
            print("a[%d][%d] = %e\n"%(i,j,ak))
            dif[j][i+1] = ak
    printMatrix(dif) #Print the resultant matrix
    return dif

def printMatrix(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            print("%0.4e"%data[i][j],end='\t')
        print("\n")

def requestData():
	n = int(input("Ingrese tamaño de puntos: "))
	data = [[0 for i in range(2)] for j in range(n)] 

	for i in range(n):
		data[i][0] = float(input(f"Ingrese valor de x{i}: "))
		data[i][1] = float(input(f"Ingrese valor de f({i}): "))
	
	return data

if __name__ == "__main__":
	main()