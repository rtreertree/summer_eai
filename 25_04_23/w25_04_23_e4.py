hour , minute = int(input("Hour: ")), int(input("Minute: "))


bill = 0
if hour == 0 and minute < 60:
    bill = 0
else:
    if minute > 0:
        hour += 1
    bill = hour * 30

print(f"Bill : {bill}")

#OUTPUT 
"""
Hour: 1
Minute: 30
Bill : 60
"""