f = list(map(int, input().split(",")))
t = list(map(int, input().split(",")))
c = f + t
c.sort()
median = 0
if len(c) % 2 == 1:
    median = c[round(((len(c) - 1) / 2))]
else:
    i = round(((len(c) - 1) / 2))
    j = i - 1
    median = (c[i] + c[j]) / 2

print(f"{median:.2f}")