while True:
    try:
        # Leitura da entrada
        N = int(input())
        trainings = []

        # Leitura dos treinos
        for _ in range(N):
            T, D = map(int, input().split())
            trainings.append((T, D))

        # Verificação dos recordes
        records = [1]  # O dia 1 é sempre um recorde
        max_speed = trainings[0][1] / trainings[0][0]  # Velocidade média do primeiro treino

        for i in range(1, N):
            T, D = trainings[i]
            speed = D / T

            if speed > max_speed:
                records.append(i + 1)
                max_speed = speed

        # Impressão dos recordes
        for record in records:
            print(record)

    except EOFError:
        break