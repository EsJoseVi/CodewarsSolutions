name = input()
state = input()

if state == "close":
    print(f"{name}, Opening the door!")
    print(f"New state for the door: open")
if state == "open":
    print(f"{name}, closing the door!")
    print(f"New state for the door: close")
