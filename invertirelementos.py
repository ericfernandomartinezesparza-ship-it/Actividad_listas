# 4. Invertir elementos

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)

invertida = numeros[::-1]

print("\nLista original:", numeros)
print("Lista invertida:", invertida)
