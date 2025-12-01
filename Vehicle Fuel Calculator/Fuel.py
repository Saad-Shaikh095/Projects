# Vehicle & Fuel Calculator

print("------ Vehicle Fuel Calculator ------")

# Take mileage (average)
mileage = float(input("Enter vehicle mileage (km per litre): "))

# Menu
print("""
Choose an option:
1. Calculate petrol you get from money
2. Calculate money required for petrol (litres)
3. Calculate distance possible with given litres
4. Calculate litres needed for a given distance
""")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    price_per_litre = float(input("Enter petrol price per litre: "))
    money = float(input("Enter money you have: "))
    litres = money / price_per_litre
    print(f"\nPetrol you will get: {litres:.2f} L")

elif choice == 2:
    price_per_litre = float(input("Enter petrol price per litre: "))
    litres_needed = float(input("Enter litres you want to fill: "))
    cost = litres_needed * price_per_litre
    print(f"\nTotal money required: ₹{cost:.2f}")

elif choice == 3:
    litres = float(input("Enter litres of petrol in vehicle: "))
    distance = litres * mileage
    print(f"\nDistance possible: {distance:.2f} km")

elif choice == 4:
    distance = float(input("Enter distance you want to travel: "))
    litres_needed = distance / mileage
    print(f"\nPetrol required: {litres_needed:.2f} L")

else:
    print("Invalid choice! Please select 1–4.")
