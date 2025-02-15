numbers = ("one", "two", "three", "four", "five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fiveteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","fourty","fivety","sixty","seventy","eighty","ninety")
operations = ("plus", "subtract","multipliedBy", "dividedBy")
numerone , operation, numbertwo = input().split()

operation = operations.index(operation)

def w2i(w):
    if "-" not in w:
        return numbers.index(w) + 1
    else:
        w = w.split("-")
        f = (numbers.index(w[0]) - 17) * 10
        f += numbers.index(w[1]) + 1
        return f
def n2o(w1,w2,n):
    if n == 0:
        return(f"{w1}+{w2}={w1+w2}")
    if n == 1:
        return(f"{w1}-{w2}={w1-w2}")
    if n == 2:
        return(f"{w1}*{w2}={w1*w2}")
    return(f"{w1}/{w2}={round(w1/w2)}")
numerone = w2i(numerone)
numbertwo = w2i(numbertwo)
print(n2o(numerone,numbertwo,operation)) 