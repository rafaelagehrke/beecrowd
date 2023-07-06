while True:
    try:
        # Leitura da entrada
        N, Amin, Amax = map(int, input().split())
        count = 0

        # Contagem dos visitantes que podem andar na montanha-russa
        for _ in range(N):
            height = int(input())
            if Amin <= height <= Amax:
                count += 1

        # Impressão do resultado
        print(count)

    except EOFError:
        break