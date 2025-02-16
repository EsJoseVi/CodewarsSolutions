data = input().split(",")

particles = ["","","grand","great grand","great-great grand"]

y = 0
p = 0
for i , ix in enumerate(data):
    if ix == "Y":
        y = i
    try:
        y += int(ix)
        p = int(ix)
    except:
        pass
    
if data[y] == "Y":
    print("ME!")
elif data[y] == "M":
    if p > 0:
        print(f"{particles[abs(p)]}son".upper())
    else:
        print(f"{particles[abs(p)]}father".upper())
else:
    if p > 0:
        print(f"{particles[abs(p)]}doughter".upper())
    else:
        print(f"{particles[abs(p)]}mother".upper())