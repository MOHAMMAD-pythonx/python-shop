import random

print("hads add")
print("(q)for exit")
print("Enter your choes number")
talash = 1
hads = random.randint(1,30)
while True:
    vorodi = input("Enter your number : ")
    if vorodi == "q":
        print("goodbay")
        break
    try:
        add = int(vorodi)
    except ValueError:
        print("jast number")
        continue
    if add == hads :
        print(f"very good {talash}")
        break
    elif add >= hads :
        talash = talash + 1
        print("go down!")
    elif add <= hads :
        talash = talash + 1
        print("go up!")
    
