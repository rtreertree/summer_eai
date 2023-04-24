import numpy as np

#1
print(25)
#2
print("%.6f"%100)
#3
print(np.pi)
#4
print(12.5)
#5
a, b = 2, 3
print(f"{a} x {b} = {a*b}")
#6
a, b = 2, 3
print(f"{a} + {b} = {b} + {a} = {a+b}")
#7
a, b, c = 2, 3, 5
print(f"{a}({b}+{c}) = ({a}x{b})+({a}x{c})")
#8
a, b, f = 2.4, 2.5, "%.2f"
print(f"{f%b}-{f%a} = {f%(b-a)}")
#9
birthday = 25
print(f"ฉันเกิดวันที่ {birthday} ธันวาคม")
#10
a, f = 3.5, "%.2f"
print(f"เขามีเงินมากกว่าฉัน {f%a} บาท")
#11
a = 5
print(f"ฉันได้กำไร {a} %")
#12
a, b = 2, 3.5
print(f"เมื่อวานฉันขาดทุน {a}%\nวันนี้ฉันได้กำไร {b}%")