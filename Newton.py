""""Use requestData method to fill with your own data
but I recommend to fill it statically in the array"""

epsilon = 4

def main():
    print("\t\tNewton con diferencias divididas\n\n")
    
    #x = 2
    #data = [[1,56.5],[5,113.0],[20,181.0],[40,214.5]]

    #        Xn    f(Xn)
    data = [[20,17.535],
           [40,55.324],
           [60,149.380],
           [80,355.110]]

	#   Valor a encontrar
    x = 30
    #x = 2
    #data = [[1,56.5],[5,113.0],[20,181.0],[40,214.5]]

    n = len(data)
    polynomials = n-1
    k = 0 #Begin, is 0 almost in every case, because if we have n terms we use 0 to get n-1 polynomials

    dif = calculateDividedDiferences(data)
    print("-"*70)

    for i in range(polynomials):
        total = data[k][1]
        print(f"{total} + ", end = '')
        for j in range(i+1):
            if j != 0:
                print(" + ",end='')
            total += getMultiplication(data,j,x) * getDividedDifference(dif,k,j)
        total = round(total,epsilon)
        print(" = %.4f\n"%total)

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
    print("(%.4f)"%data[term][n+1],end='')
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
            print("(%.4f-%.4f)/(%d - %d)" % (dif[j+1][i],dif[j][i],data[j+diff][0],data[j][0]))
            ak = (dif[j+1][i] - dif[j][i])/(data[j+diff][0]-data[j][0]) #a[k] calculation 
            ak = round(ak,epsilon)
            print("a[%d][%d] = %.4f\n"%(i,j,ak))
            dif[j][i+1] = ak
    printMatrix(dif) #Print the resultant matrix
    return dif

def printMatrix(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            print("%f"%data[i][j],end='\t')
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