import math

PI = 3.14159
G = 9.80665

while True:
    try:
        h = float(input())
        p1, p2 = map(int, input().split())
        n = int(input())

        for i in range(n):
            alfa, v = map(float, input().split())

            alfa = alfa * PI / 180
            Vox = v * math.cos(alfa)
            Voy = v * math.sin(alfa)

            Ts = Voy / G
            H = (Voy * Voy) / (2 * G) + h
            Vfy = math.sqrt(2 * G * H)
            Td = Vfy / G
            Tt = Ts + Td
            D = Vox * Tt

            if D > p1 and D < p2:
                print("{:.5f} -> DUCK".format(D))
            else:
                print("{:.5f} -> NUCK".format(D))
    except:
        break