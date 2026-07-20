# 2. Suma de elementos

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)

suma = sum(numeros)

print("\nLista:", numeros)
print("La suma es:", suma)
