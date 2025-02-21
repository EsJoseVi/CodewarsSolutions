text = input()

toreverse = ""
for i in text:
    if i == "A":
        toreverse += "U"
        continue
    if i == "E":
        toreverse += "O"
        continue
    if i == "O":
        toreverse += "E"
        continue
    if i == "U":
        toreverse += "A"
        continue
    if i == "a":
        toreverse += "u"
        continue
    if i == "e":
        toreverse += "o"
        continue
    if i == "o":
        toreverse += "e"
        continue
    if i == "u":
        toreverse += "a"
        continue
    toreverse += i

print(toreverse[::-1])