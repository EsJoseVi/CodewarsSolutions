h , g = list(map(float,input().split(":")))

vf = 2*g*h
vf = vf ** 0.5

if vf > 120 * 10 / 36:
    print("MUERE")
    exit(0)
print("SOBREVIVE")