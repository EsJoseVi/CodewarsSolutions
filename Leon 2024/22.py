notes = {"Do":1,"Re":2,"Mi":3,"Fa":4,"Sol":5,"La":6,"Si":7}
data = input().split(",")

result = ""
for i in data:
    added = ""
    if i[0] == "#" or i[0] == "b":
        added = i[0]
        i = i[1:]
    i = notes[i]
    if added == "#":
        i += 10
    if added == "b":
        i *= -1
    result += str(i) + ","

print(result[:-1])