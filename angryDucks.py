import math

# `PI` and `G` are constants used in the program. `PI` is the mathematical constant pi (approximately
# equal to 3.14159) and `G` is the acceleration due to gravity (approximately equal to 9.80665 meters
# per second squared). These constants are used in the calculations to determine the distance the duck
# will travel after being shot from a gun.
PI = 3.14159
G = 9.80665

# This code is an implementation of a program that calculates the distance a duck will travel after
# being shot from a gun. The program takes in the initial height of the duck, the minimum and maximum
# distances the duck can be shot, and the number of shots to be taken. For each shot, the program
# takes in the angle and velocity of the shot and calculates the distance the duck will travel using
# the given formulas. If the distance is within the minimum and maximum distances, the program prints
# "DUCK", otherwise it prints "NUCK". The program runs in an infinite loop until an exception is
# raised (such as the user entering invalid input or pressing Ctrl+C to exit the program).
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