# 3. Encontrar mayor y menor

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)

print("\nLista:", numeros)
print("Número mayor:", max(numeros))
print("Número menor:", min(numeros))
