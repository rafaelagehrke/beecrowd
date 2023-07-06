while True:
    try:
        # Leitura da entrada
        N = int(input())
        words = [input() for _ in range(N)]
        Q = int(input())

        for _ in range(Q):
            query = input()
            suggestions = [word for word in words if word.startswith(query)]
            num_suggestions = len(suggestions)
            max_length = max(len(word) for word in suggestions) if num_suggestions > 0 else -1

            if num_suggestions == 0:
                print(-1)
            else:
                print(num_suggestions, max_length)

    except EOFError:
        break
