print("Welcome to the tip calculator!")
total_bill=float(input("What was your total bill? ₹"))
tip=int(input("How much tip would you like to give?"))
persons=int(input("How many people to split the bill?"))
total_tip=tip / 100
bill_split=total_bill+total_tip
tip_per_person=round(bill_split/persons,2)
print(f"Eachperson should pay: ₹{tip_per_person}")