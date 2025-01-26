s = input()
n = int(input())
sol = ""

for i in s:
    if i.isupper():
        if ord(i) - n >= 65 :
            sol += chr(ord(i) - n)
            continue
        else:
            sol += chr(91 + (ord(i) - n - 65)) 
            continue
    sol += i
print(sol)