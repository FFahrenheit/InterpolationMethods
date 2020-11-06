epsilon = 4

def main():
    
    #yprime = "y - x**2 + 1"
    yprime = "xi - yi"
    
    x0 = 0
    y0 = 2    #Corresponde a y(x0) = y0
    
    xf = 1    #Valor de x que buscamos para y'(x)
    
    n = 5  #Intervalos 

    h = round((xf-x0)/n,epsilon)

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
        print(f"{yi} + ({h})({xi}-{yi}) = {yn}")


if __name__ == "__main__":
	main()