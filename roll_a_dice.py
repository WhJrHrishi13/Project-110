import random

response = "y"
while response == "y":
    number = random.randint(1,6)

    if number == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if number == 2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")

    if number == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")

    if number == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")

    if number == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")

    y = input("press enter to continue and esc to exit")

