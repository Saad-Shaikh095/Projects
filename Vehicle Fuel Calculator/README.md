# 🚗⛽ Vehicle & Fuel Calculator

A simple and user-friendly Python program that helps you calculate petrol usage, cost, and travel distance based on your vehicle mileage.
This tool is perfect for new vehicle owners who want to track fuel efficiency and plan trips smartly.

## 🌟 Features

This calculator offers 4 useful fuel-related operations:

### 1️⃣ Petrol you get from money

Enter petrol price per litre

Enter money you have

The program tells you how many litres you will get

### 2️⃣ Money required for litres

Enter petrol price per litre

Enter litres you want

The program calculates the total cost

### 3️⃣ Distance possible with given litres

Enter how many litres you currently have

Program shows how far (in km) your vehicle can go

### 4️⃣ Litres needed for a distance

Enter the distance you want to travel

Program calculates how many litres you will need

## 🧮 How the Program Works

The program asks for your vehicle mileage first (km per litre).
Then it shows a menu with four options.
Based on the option you choose, it asks for more input and performs the correct calculation.

## 📌 Code Snippet
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

## 🚀 How to Run the Program

Install Python (if not installed)

Save the code in a file:

vehicle_fuel_calculator.py


Open terminal / command prompt

Run the script:

python vehicle_fuel_calculator.py

## 📌 Use Cases

Calculate how much petrol you can buy before a long ride

Estimate the cost of filling your tank

Plan trips based on your mileage

Understand your vehicle’s fuel efficiency

## ❤️ Developer

This project was created by Saad Shaikh.
