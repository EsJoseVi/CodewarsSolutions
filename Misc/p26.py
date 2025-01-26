## 1900 0091 0019 1009 9001

n = list(input())
n = n[::-1]
p = n[0]
rest = []
for i in range(1,len(n)):
    if p > n[i]:
        n[i-1] = n[i]
        n[i] = p
        rest = n[0:i]
        break
    p = n[i]
rest.sort()
rest = rest[::-1]
rest = rest + n[i:]
print("".join(rest[::-1]))