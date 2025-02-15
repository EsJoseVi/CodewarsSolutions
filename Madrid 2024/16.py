data = input().split(",")
direction = data[-1:][0]
data = list(map(int,data[:-1]))
if direction == "U" or direction == "D":
    print(*data, sep=",")
else:
    data.sort()
    if direction == "L":
        print(*data[::-1],sep=",")
    else:
        print(*data,sep=",")