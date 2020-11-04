def main():
	print("\t\tLagrange polynomials\n\n")

	#x = 2
	#data = [[1,56.5],[5,113.0],[20,181.0],[40,214.5]]

	#        Xn    f(Xn)
	data = [[20,17.535],[40,55.324],[60,149.380],[80,355.110]]

	#   Valor a encontrar
	x = 30

	data = [[1.9,14.4],[3.7,28.7],[5.5,43.1],[7.3,52.7]]

	x = 4.5

	
	n = len(data)
	polynomials = n-1

	for i in range(polynomials):
		total = 0
		for j in range(i+2):
			if j != 0:
				print("\n + ",end='')
			print(data[j][1],end='')
			u = upsidePart(data,i+2,j,x)
			print("/(",end='')
			d = downsidePart(data,i+2,j,x)
			print(")",end = '')
			total += data[j][1]*u/d
		print(" = %.4f\n"%total)


#Data = values
#t -> Veces a repetir 
#k -> Termino a obtener
#x -> Valor de x
def upsidePart(data,t,k,x):
	total = 1
	for i in range(t):
		if i != k:
			total *= (x-data[i][0])
			print (f"({x} - {data[i][0]})",end='')
	return total

def downsidePart(data,t,k,x):
	total = 1
	for i in range(t):
		if i != k:
			total *= (data[k][0]-data[i][0])
			print (f"({data[k][0]} - {data[i][0]})",end='')
	return total

def requestData():
	n = int(input("Ingrese tamaño de puntos: "))
	data = [[0 for i in range(2)] for j in range(n)] 

	for i in range(n):
		data[i][0] = float(input(f"Ingrese valor de x{i}: "))
		data[i][1] = float(input(f"Ingrese valor de f({i}): "))
	
	return data
	

if __name__ == "__main__":
	main()