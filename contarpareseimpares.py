# 1. Contar pares e impares

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)

pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nLista:", numeros)
print("Pares:", pares)
print("Impares:", impares)
