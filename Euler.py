#Modificar yprime para evaluar la operación  y la linea 32 para impresion
epsilon = 4

def main():
    
    #yprime = "y - x**2 + 1"
    yprime = "yi - xi**2+1"
    
    x0 = 0
    y0 = 0.5    #Corresponde a y(x0) = y0
    
    xf = 2    #Valor de x que buscamos para y'(x)
    
    n = 4  #Intervalos 

    h = round((xf-x0)/n,epsilon)
    print(f"h = ({xf}-{x0})/{n}")
    print(f"h = {h}")

    xn = x0 
    yn = y0 #Para empezar

    for i in range(n):
        print("*"*10,"Iteracion ",i+1,"*"*10)
        xi = round(xn,epsilon)
        yi = round(yn,epsilon)

        xn = round(xi + h,epsilon)
        print(f"x[{i+1}] = {xi} + {h} = {xn}")

        yn = round(yi + h * eval(yprime),epsilon)
        print(f"y[{i+1}] = {yi} + ({h})({yi}-{xi}^2 + 1) = {yn}")


if __name__ == "__main__":
	main()