try:
    n = int(input())
except:
    print("Wrong")
    exit(0)
if n < 3 or n > 100:
    print("Wrong")
    exit(0)
result = ""
for i in range(1,n+1):
    if i % 3 == 0:
        if i % 5 == 0:
            result += "FizzBuzz "
        else:
            result += "Fizz "
    if i % 5 == 0:
        result += "Buzz "

print(result[:-1])