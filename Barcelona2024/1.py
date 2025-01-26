import sys

s = True
actual = 0
last = None
for line in sys.stdin:
    actual = int(line)
    if last != None and last > actual:
        s = False
    last = actual
print(s)