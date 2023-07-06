T = int(input())

for t in range(1, T+1):
    conversion = input()
    R, G, B = map(int, input().split())

    if conversion == "eye":
        P = int(0.30*R + 0.59*G + 0.11*B)
    elif conversion == "mean":
        P = int((R + G + B) / 3)
    elif conversion == "max":
        P = max(R, G, B)
    elif conversion == "min":
        P = min(R, G, B)

    print(f"Caso #{t}: {P}")
