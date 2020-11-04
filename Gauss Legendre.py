import math

epsilon = 4

def main():
    print("\t\tGauss Legendre\t\t")

    print("*"*10,"Primer orden","*"*10)

    #a = -0.8
    #b = 1.5

    a = 0
    b = round(math.pi/2,epsilon)

    z = getZ(a,b)
    print(z,"\n")
    x = getX(a,b)
    print(x,"\n")
    dx = getDx(a,b)
    print(dx,"\n")

    #fz = f"(1/math.sqrt(2*math.pi))*math.exp(-{x}**2/2)*{dx}"

    fz = f"math.exp({x})*math.sin({x})"
    w1 = 1
    w2 = 1
    z1 = round(-1/math.sqrt(3),epsilon)
    z2 = round(1/math.sqrt(3),epsilon)

    print(fz)

    z = z1
    dz = 1

    fz1 = round(eval(fz),epsilon)
    print(fz1)
    z = z2
    fz2 = round(eval(fz),epsilon)
    print(fz2)

    r = round(eval(dx)*(w1*fz1+w2*fz2),epsilon)
    print(f"r = {r}")

    print("*"*10,"Segundo orden","*"*10)
    w1 = round(5/9,epsilon)
    w2 = round(8/9,epsilon)
    w3 = w1

    z1 = -1*round(math.sqrt(3/5),epsilon)
    z2 = 0
    z3 = z1*-1

    z = z1
    fz1 = round(eval(fz),epsilon)
    print(fz1)

    z = z2
    fz2 = round(eval(fz),epsilon)
    print(fz2)
    
    z = z3
    fz3 = round(eval(fz),epsilon)
    print(fz3)

    r = round(eval(dx)*(w1*fz1 + w2*fz2 + w3*fz3),epsilon)
    print(f"r = {r}")

def getDx(a,b):
    d = b-a
    r = d/2
    print(f"{r}dz")
    
    return f"({r}*dz)"

def getX(a,b):
    s = a+b
    d = b-a
    print(f"x = ({d}z + {s})/2")
    return f"(({d}*z + {s})/2)"

def getZ(a,b):
    print(f"z = (2x - ({a} + {b}))/({b}-{a})")
    print(f"z = (2x - {a+b}) / {b-a}")
    s = a+b
    d = b-a
    return f"((2*x - {s})/{d})"

if __name__ == "__main__":
	main()