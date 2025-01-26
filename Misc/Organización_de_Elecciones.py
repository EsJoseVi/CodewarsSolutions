elec = int(input())

tablemax = int(input())

vot = []
for i in range(elec):
    inp = input()
    inpl = inp.split()
    vot.append([inpl[0].lower(),inp])
vot.sort()
 
r = round(elec/tablemax)
f = elec % tablemax

if f == 0:
    print(r)
else:
    print(r+1)

for i in range(1,r+1):
    print(i)
    print(vot[(i-1) * tablemax][1])
    print(vot[(i * tablemax)-1][1])
if f != 0:
    print(r+1)
    print(vot[r * tablemax][1])
    print(vot[r * tablemax + f-1][1])