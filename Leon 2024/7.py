h, g = list(map(float,input().split(":")))

t = h * g * 2

t = t**0.5

max = 120 * (1000/3600)

if t > max:
    print("MUERE")
else:
    print("SOBREVIVE")