import statistics

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    return statistics.median(numeros)

def calcular_moda(numeros):
    return statistics.mode(numeros)

A = [10, 20, 30, 40, 50]
B = [1, 5, 5, 5, 135]
media_A = calcular_media(A)
media_B = calcular_media(B)
mediana_A = calcular_mediana(A)
mediana_B = calcular_mediana(B)
moda_A = calcular_moda(A)
moda_B = calcular_moda(B)

print(f"- Média")
print(f"A: {media_A}")
print(f"B: {media_B}\n")
print(f"- Mediana")
print(f'A: {mediana_A}')
print(f'B: {mediana_B}\n')
print(f"- Moda")
print(f"A: {moda_A}")
print(f"B: {moda_B}\n")