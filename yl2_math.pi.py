# Küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu

import math

r = float(input("Sisesta ringi raadius: "))
s = math.pi * r * r
p = int("2") * math.pi * r
s1 = round(s)
print("Ringi pindala on " + str(s1))
p1 = round(p)
print("Ringi ümbermõõt on " + str(p1))
