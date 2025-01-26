n = list(input())
n.sort()
t =  int(input())
sol = []
for i in range(t):
    inp = list(input())
    inp.sort()
    if n == inp:
       sol.append("Anagrama")
    else:
        sol.append("No")
for i in sol:
    print(i)