n = int(input())

Three = 0
Five = 0

for i in range(n + 1):
    if i == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        Three += 3
        Five +=  3
        continue
    if  i % 3 == 0:
        Three += 1
    if i % 5 == 0:
        Five += 2

if Five > Three:
    print("Five")
    exit(0)
if Three > Five:
    print("Three")
    exit(0)
print("No one won")
