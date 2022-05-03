# programa para determinar si dados 3 numeros enteros, la suma de los 2 primeros es igual al tercero

print("--------------------------------")
print("--- SUMA DE LOS DOS PRIMEROS ---")
print("----------- ES IGUAL -----------")
print("---------- AL TERCERO ----------")
print("--------------------------------")

#input

X = int(input("Primer numero:"))
Y = int(input("Segundo numero:"))
Z = int(input("Tercer numero: "))
 
# processing

z1 = X + Y

if z1 == Z:
    print("\nLos dos primeros numeros son iguales al tercero")
else:
    print("\nLa suma de los dos primeros numeros es diferente al tercer numero")


# output