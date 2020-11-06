#Modificar getFunction segun la operacion y los print para mayor entendimiento xd 
epsilon = 6

def main():    
    x0 = 0
    y0 = 0.5    #Corresponde a y(x0) = y0
    
    xf = 2      #Valor de x que buscamos para y'(x)
    
    n = 4       #Intervalos 

    h = round((xf-x0)/n,epsilon)
    print(f"h = ({xf}-{x0})/{n}")
    print(f"h = {h}")

    xn = x0 
    yn = y0         #Para empezar

    for i in range(n):
        print("*"*10,"Iteracion ",i+1,"*"*10)
        xi = round(xn,epsilon)
        yi = round(yn,epsilon)

        xn = round(xi + h,epsilon)
        print(f"x[{i+1}] = {xi} + {h} = {xn}")

        ynt = yi + h*(getFunction(xi,yi))
        ynt = round(ynt,epsilon)

        print(f"y^[{i+1}] = {yi} + ({h})({yi} - {xi}^2 + 1) = {ynt}")

        yn = yi + (h/2)*(getFunction(xi,yi)+getFunction(xn,ynt))
        yn = round(yn,epsilon)

        print(f"y[{i+1}] = {yi} + ({h}/2)(({yi} - {xi}^2 + 1) + ({ynt} - {xn}^2 + 1)) = {yn}")


def printFunction(x,y):
    print(f"({y} - {x}^2 + 1")

def getFunction(x,y):
    return y - x**2 + 1

if __name__ == "__main__":
	main()