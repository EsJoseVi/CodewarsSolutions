import math

data = list(map(int,input().split(",")))

money = data[-1:][0]
data = data[:-1]
coins = [200,100,50,20,10,5,2,1]

result = []
for i, ix in enumerate(data):
    n = math.floor(money / coins[i])
    if n > 0:
        if n < ix:
            result.append(ix - n)
            money -= n*coins[i]
        else:
            result.append(0)
            money -= ix*coins[i]
    else:
        result.append(ix)
print(",".join(list(map(str,result))))