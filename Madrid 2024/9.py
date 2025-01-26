n = int(input())
s = n
l = 1
for i in range(n):
    print(" "*s+"*"*l)
    l += 2
    s -= 1