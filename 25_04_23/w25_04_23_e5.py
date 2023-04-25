def calculate_bill(isMember, bill):
    d = 1
    if(isMember.lower() == "yes"):
        if(bill >= 500): d = (100 - 5)/100
        elif(bill >= 1000): d = (100 - 10)/100
        elif(bill >= 5000): d = (100 - 15)/100
    return bill * d

isMember = input("is member : ")
bill = int(input("bill : "))
print(f"Your bill is {calculate_bill(isMember, bill)}")

#OUTPUT
"""
is member : yes
bill : 10000
Your bill is 9500.0
"""