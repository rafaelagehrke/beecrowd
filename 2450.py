def verificar_matriz_escada(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    max_zeros = 0
    valido = True
    for linha in range(num_linhas):
        zeros_consecutivos = 0
        consecutivos = True
        for coluna in range(num_colunas):
            elemento = matriz[linha][coluna]
            if elemento == 0 and consecutivos:
                zeros_consecutivos += 1
            else:
                consecutivos = False
        if linha != 0:
            if (zeros_consecutivos > max_zeros or (zeros_consecutivos == max_zeros and zeros_consecutivos == num_colunas)) and valido:
                max_zeros = zeros_consecutivos
            else:
                max_zeros = 0
                valido = False
        else:
            max_zeros = zeros_consecutivos
    if max_zeros:
        return "S"
    else:
        return "N"
num_linhas, num_colunas = map(int, input().split())
matriz = []
for _ in range(num_linhas):
    linha = list(map(int, input().split()))
    matriz.append(linha)
resultado = verificar_matriz_escada(matriz)
print(resultado)