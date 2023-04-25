def calculate_bill(isMember, bill):
    d = 100
    if(isMember.lower() == "yes"):
        if(bill <= 500):
            d = 100 - 5
        elif(bill <= 1000):
            
            d = 100 - 10
        elif(bill <= 5000):
            d = 100 - 15
    d = d / 100
    return bill * d

isMember = input("is member : ")
bill = int(input("bill : "))

print(f"Your bill is {calculate_bill(isMember, bill)}")