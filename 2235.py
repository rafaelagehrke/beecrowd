A, B, C = map(int, input().split())

if (A-B == 0):
    print("S")
elif (A-C == 0):
     print("S")
elif(B-C == 0):
     print("S")
elif((A+B)-C == 0):
     print("S")
elif((B+C)-A == 0):
     print("S")
elif((A+C)-B == 0):
     print("S")
else:
    print("N")