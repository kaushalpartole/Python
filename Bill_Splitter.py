Bill = float(input("What is the total bill? "))
Tip = int(input("How much tip would you like to pay? "))
People = int(input("How many people to split the bill? "))

Each_People_pays = (Bill + (Bill * (Tip/100)))/People
print(f"Each People Pays: {round(Each_People_pays,2)}")