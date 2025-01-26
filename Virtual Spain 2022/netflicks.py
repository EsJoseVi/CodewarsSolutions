data = input().split(",")
n = len(data)
max = 0
total = 0
def time(info):
    t = 0
    t += int(info.split(":")[1])
    t += int(info.split(":")[0]) * 60
    return t
for i in range(n):
    if i == 0:
        max = time(data[0])
        continue
    total += time(data[i])
if total < max:
    remaining = max - total
    print(f"{round(remaining / 60):02}:{remaining % 60:02} hours of viewing remaining.")
else:
    execed = total - max
    print(f"LIMIT EXCEEDED BY {round(execed / 60):02}:{execed % 60:02} hours. Benigno punished!")