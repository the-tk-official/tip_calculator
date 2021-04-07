print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would u like to give? 10, 12 or 15? "))
people = int(input("How many people to split a bill? "))

bill_with_tip = bill / 100 * tip + bill
bill_per_person = bill_with_tip / people

print(f"Each person should pay ${round(bill_per_person, 2)}")
