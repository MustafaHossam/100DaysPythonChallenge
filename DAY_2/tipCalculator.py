print("Welcome to the Tip Calculator.")
totalBill = float(input("What was the Total Bill? $"))
peopleNumber = int(input("How Many People to split the bill? "))
tipPercent = int(input("What Percentage tip would you like to give? 10, 12, or 15? "))
#tip = str((totalBill*tipPercent)/(100*peopleNumber))
tip = (totalBill*tipPercent)/(100)
totalBill = totalBill + tip
billOfEachPerson = round(totalBill/peopleNumber,2)
print(f"Each person should pay: {billOfEachPerson}")

