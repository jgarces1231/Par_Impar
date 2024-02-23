# Programaga para verificar si un numero es Par o Impar

# Input

X=int(input("digite el valor de x: "))

# Prosessing

r=X%2
if r==0:
    rta="PAR"
else:
    rta="IMPAR"

# Output 
print("El numero " + str(X) + " es " + rta) 
 