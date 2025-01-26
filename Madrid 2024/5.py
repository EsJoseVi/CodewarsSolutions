n = int(input())

j = 1
sol = ""
for i in range(n-1):
    j += 2
    print(f"[{j} : {2*j}] ",end="")
j += 2
print(f"[{j} : {2*j}]",end="")
    