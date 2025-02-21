#Needs time

hand = list(map(int, input().split(",")))

hand.sort(reverse=True)
conjunto = set()
same = []
start = 0
straight = True
for i,ix in enumerate(hand):
    conjunto.add(ix)
    if i == 0:
        start = ix
    if ix != start - i:
        straight = False

largest = 0
if straight:
    print("Straight")
else:
    if len(conjunto) == 1:
        print("Repoker")
    if len(conjunto) == 2:
        for i in conjunto:
            largest = max([largest,hand.count(i)])
        if largest == 4:
            print("Poker")
        else:
            print("Full House")
    if len(conjunto) == 4:
        print("Pair")
    if len(conjunto) == 5:
        print(f"Highest: {hand[0]}")
    if len(conjunto) == 3:
        for i in conjunto:
            largest = max([largest,hand.count(i)])
        if largest == 3:
            print("Three")
        else:
            print("Two Pairs")