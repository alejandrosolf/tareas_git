# Precios dados
prices = [0, 1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]  
# índice = largo (prices[1] es el precio del largo 1)

n = 11  # largo de la cuerda

# dp[i] = mejor precio para una cuerda de largo i
dp = [0] * (n + 1)
# cut[i] = tamaño del primer pedazo en la solución óptima
cut = [0] * (n + 1)

for i in range(1, n + 1):
    max_val = -1
    best_first_cut = 0
    for j in range(1, i + 1):
        val = prices[j] + dp[i - j]
        if val > max_val:
            max_val = val
            best_first_cut = j
    dp[i] = max_val
    cut[i] = best_first_cut

# reconstrucción de la solución
solution = []
length = n
while length > 0:
    solution.append(cut[length])
    length -= cut[length]

print("Precio máximo:", dp[n])
print("Descomposición óptima:", solution)
print("Tabla DP:", dp)

