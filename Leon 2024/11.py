things = {"D":0.2, "E":-0.1, "T":-0.05, "P":-0.08}

data = input().split(" ")

alcohol = 0
for i in data:
    alcohol += things[i]

if alcohol < 0:
    alcohol = 0

if alcohol > 0.5:
    print(f"Oh no! His BAC is {alcohol:.2f} g/L and over the limit! He will not be able to give the speech!") 
else:
    print(f"Oh no! His BAC is {alcohol:.2f} g/L which is under the limit. He will be able to give the speech! Get ready!")

