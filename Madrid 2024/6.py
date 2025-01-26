def palindrome(s):
    if s == s[::-1]:
        return True
    return False

s = input()

if palindrome(s):
    print(f"{len(s)}, T")
else:
    print(f"{len(s)}, F")