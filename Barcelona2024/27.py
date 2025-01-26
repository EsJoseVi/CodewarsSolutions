n = int(input())

porweFul = True
powers = True

nn = n
for i in range(2,round(n**0.5)):
    t = 0
    while nn % i == 0:
        nn = nn / i
        t += 1
    if t == 1:
        porweFul = False
        break 
    if t % 2 != 0:
        powers = False
    if nn == 1:
        break

if porweFul and powers == False:
    print(f"{n} is an Achilles number")
else:
    print(f"{n} is NOT an Achilles number")
