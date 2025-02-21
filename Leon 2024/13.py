value = ""
palo = ""
for i in range(8):
    line = input()
    if i == 1:
        value = line[2]
    if i == 5:
        line4 = line
    if i == 3:
        line2 = line

if   line2 == ":    /  \\    :" and line4 == ":     \\/     :":
    palo = "Diamonds"
elif line2 == ":   ( \\/ )   :":
    palo = "Hearts"
elif line2 == ":    /  \\    :" and line4 == ":     /\\     :":
    palo = "Spades"
elif line2 == ":   _(  )_   :":
    palo = "Clubs"

if value == "K":
    value = "King"
if value == "Q":
    value = "Queen"
if value == "J":
    value = "Jack"

print(f"{value} of {palo}")