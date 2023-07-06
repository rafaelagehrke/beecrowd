while True:
    try:
        # Leitura dos dados de entrada
        N = int(input())
        M, L = map(int, input().split())

        # Leitura do baralho de Marcos
        baralho_marcos = []
        for _ in range(M):
            atributos = list(map(int, input().split()))
            baralho_marcos.append(atributos)

        # Leitura do baralho de Leonardo
        baralho_leonardo = []
        for _ in range(L):
            atributos = list(map(int, input().split()))
            baralho_leonardo.append(atributos)

        CM, CL = map(int, input().split())
        A = int(input())

        # Verificação dos atributos escolhidos
        marcos_atributo = baralho_marcos[CM-1][A-1]
        leonardo_atributo = baralho_leonardo[CL-1][A-1]

        # Determinação do vencedor
        if marcos_atributo > leonardo_atributo:
            print("Marcos")
        elif marcos_atributo < leonardo_atributo:
            print("Leonardo")
        else:
            print("Empate")

    except EOFError:
        break