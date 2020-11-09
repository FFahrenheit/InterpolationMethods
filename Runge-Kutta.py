"""Modificar getFunction y printFunction"""
epsilon = 4

def main():    
    x0 = 0      #x0
    y0 = 0.5    #Corresponde a y(x0) = y0
    
    xf = 2      #Valor de x que buscamos para y(x)
    
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

        xn = xi + h 
        print(f"x{i+1} = {xi} + {h} = {xn}")

        print(f"k1 = f({xi},{yi}) = ",end='')
        k1 = round(getFunction(xi,yi),epsilon)
        print(f"{printFunction(xi,yi)} = {k1}")

        print(f"k2 = f({xi} + {h}/2,{yi} + {h}*{k1}/2) = ",end='')
        k2 = round(getFunction(xi+h/2, yi+h*k1/2),epsilon)
        print(f"{printFunction(xi + h/2,yi+h*k1/2)} = {k2}")

        print(f"k3 = f({xi} + {h}/2,{yi} + {h}*{k2}/2) = ",end='')
        k3 = round(getFunction(xi+h/2,yi + h*k2/2),epsilon)
        print(f"{printFunction(xi+h/2,yi + h*k2/2)} = {k3}")

        print(f"k4 = f({xi} + {h},{yi} + {h}*{k3}) = ",end='')
        k4 = round(getFunction(xi+h, yi + h*k3),epsilon)
        print(f"{printFunction(xi + h, yi + h*k3)} = {k4}")
        
        yn = yi + (h/6)*(k1+2*k2+2*k3+k4)
        print(f"y{i+1} = {yi} + ({h}/6)({k1}+2({k2})+2({k3})+{k4}) = {yn:.4f}")



def printFunction(x,y):
    return f"({y:.4f} - {x:.4f}^2 + 1)"

def getFunction(x,y):
    return y - x**2 + 1

if __name__ == "__main__":
	main()