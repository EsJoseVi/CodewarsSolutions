def liststrip(l):
    r = []
    for i in l:
        r += i.strip()
    return r

data = input().split(",")
liberated = 0
prision = []
while data[0] != "END":
    data = liststrip(data)
    prision += data
    data = input().split(",")

change = False

for i in prision:
    if change and i == "0":
        liberated += 1
        change = False
    elif change == False and i == "1":
        liberated +=1
        change = True
print(liberated)