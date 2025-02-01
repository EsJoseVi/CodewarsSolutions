import sys
n = int(input())

letters = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
letters = letters[:n]

def large(s,letters,max):
    n = len(s)
    for i, ix in enumerate(letters):
        if ix  not in s and i != n:
            if max == n+1:
                sys.stdout.write(str(s+ix)+"\n")
            else:
                large(s+ix,letters,max)

large("",letters,n)
