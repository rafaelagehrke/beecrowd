while True:
    try:
        # Leitura da entrada
        N, M = map(int, input().split())
        mat = []

        # Leitura dos pães de queijo no tabuleiro
        for _ in range(N):
            row = list(map(int, input().split()))
            mat.append(row)

        # Função auxiliar para calcular o número de pães de queijo adjacentes
        def count_pao_de_queijo(mat, i, j):
            p = 0
            l = len(mat) - 1
            c = len(mat[i]) - 1
            if i > 0 and mat[i - 1][j] == 1:
                p += 1
            if i < l and mat[i + 1][j] == 1:
                p += 1
            if j > 0 and mat[i][j - 1] == 1:
                p += 1
            if j < c and mat[i][j + 1] == 1:
                p += 1
            return p

        # Construção do tabuleiro do jogo
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 1:
                    print(9, end='')
                else:
                    print(count_pao_de_queijo(mat, i, j), end='')
            print()  # Quebra de linha

    except EOFError:
        break
