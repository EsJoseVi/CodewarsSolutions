'''
TESTE CASE
___________________________
|             |             |
|___          |          ___|
|_  |         |         |  _|
| | |.       ,|.       .| | |
| | | )     ( | )     ( | | |
|_| |'       `|'       `| |_|
|___|         |         |___|
|             |   o         |
|_____________|_____________|
#
'''
n = 0
x = 0
while True:
    n += 1
    l = input()
    for i, j  in enumerate(l):
        if j == "o":
            x = i
    if x != 0:
        break
            
while input() != "#":
    pass

print(f"The ball is in: ({x}, {n})")