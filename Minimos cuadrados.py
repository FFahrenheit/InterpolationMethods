epsilon = 4

import numpy as np

def main():
    print("\t\tMinimos cuadrados\n\n")

    #        Xn    f(Xn)
    data = [[20,17.535],
           [40,55.324],
           [60,149.380],
           [80,355.110]]
           
    polynomials = 3 #input("Ingrese polinomios a calcular")

    xSum = [0 for i in range(2*polynomials)]
    xYSum = [0 for i in range(polynomials+1)]

    for i in range(polynomials*2):
        xSum[i] = getSummatory(data,i+1)
    
    for i in range(polynomials+1):
        xYSum[i] = getSumXY(data,i)
    
    for i in range(len(xSum)):
        print(f"x^{i+1} = {xSum[i]}")

    for i in range(len(xYSum)):
        print(f"x^{i+1}y = {xYSum[i]}")

    print("\n\n")

    for i in range(polynomials):
        print(f"Solucion polinomio grado {i+1}")
        print("*"*10,"Sistema","*"*10)
        coefMatr = [0 for i in range(i+2)]
        coefSol = [0 for i in range(i+2)]
        for j in  range(i+2):
            coefEq = getEquation(i+1,j,xSum,len(data))
            coefMatr[j] = coefEq 
            coefSol[j] = xYSum[j]
            print(f" = {xYSum[j]}")

        a = np.array(coefMatr)
        b = np.array(coefSol)
        x = np.linalg.solve(a, b)
        print("*"*10,"Soluciones","*"*10)
        for i in range(len(x)):
            print(f"a{i} = {round(x[i],epsilon)}")

        print("*"*10,"Ecuacion","*"*10)

        for i in range(len(x)):
            if i == 0:
                print(f"y = {round(x[i],epsilon)}",end='')
            else:
                print(f" + {round(x[i],epsilon)}x^{i}",end='')
        print("\n")

#Order -> Orden del polinomio
#n -> Numero de ecuacion
#xSum -> Coeficientes x^n
#data -> n (Si se requiere, solo para n=0)
def getEquation(order,n,xSum,terms):
    data = [0 for i in range(order+1)]  #Order 1 -> 2 terms and so on
    for i in range(len(data)): #Filling the array 
        if i == 0 and n == 0:    #Unique case we can't access xSum[-1]
            data[0] = terms
        else:
            data[i] = round(xSum[n-1+i],epsilon)
        if i != 0:
            print(" + ",end='')
        print(f"{data[i]:.4f}a{i}",end='')
    return data 

def getSumXY(data,pow):
    total = 0
    for i in range(len(data)):
        total += data[i][0]**pow *data[i][1]
    return round(total,epsilon)

def getSummatory(data,pow):
    total = 0
    for i in range(len(data)):
        total += data[i][0]**pow
    return round(total,epsilon)

if __name__ == "__main__":
	main()