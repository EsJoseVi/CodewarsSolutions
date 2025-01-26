data = input().split()
bac = 0
for i in data:
    if i == "D":
        bac += 0.2
        continue
    if i == "E":
        bac -= 0.1
        continue
    if i == "T":
        bac -= 0.05
        continue
    if i == "P":
        bac -= 0.08
        continue
if bac < 0:
    bac = 0

bac = round(bac,2)
if bac > 0.5:
    print(f"Oh no! His BAC is {bac:.2f} g/L and over the limit! He will not be able to give the speech!")
    exit(0)
print(f"His BAC is {bac:.2f} g/L which is under the limit. He will be able to give the speech! Get ready!")
