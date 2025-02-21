n = int(input())

mango = 1
mambos = 0
celebrate = 3
totalmangos = 0
iteration = 0

while iteration != n:
    totalmangos += mango
    mango += 1
    if totalmangos >= celebrate:
        mambos = mango
        celebrate = mambos + totalmangos
        totalmangos = 0
        iteration += 1
        mango += 1

print(mambos)