import numpy as np
Name = input("ให้นักเรียนพิมพ์ชื่อของตนเอง : ")
surname = input("นามสกุลของตนเอง : ")
age = int(input("อายุของตนเอง : "))
age_sister = int(input("อายุของน้อง : "))

print(f"ชื่อ : {Name} data type : {type(Name)}")
print(f"นามสกุล : {surname} data type : {type(surname)}")
print(f"อายุ : {age} ปี data type : {type(age)}")
print(f"อายุน้องสาว : {age_sister} ปี data type : {type(age_sister)}")
print(f"อายุต่างกับน้องสาว : {np.abs(age - age_sister)} ปี")


#OUTPUT
"""
อายุของน้อง : 80
ชื่อ : ABCDEFG data type : <class 'str'>
นามสกุล : AAAAAA data type : <class 'str'>
อายุ : 100 ปี data type : <class 'int'>
อายุน้องสาว : 80 ปี data type : <class 'int'>
อายุต่างกับน้องสาว : 20 ปี
"""
"""
ให้นักเรียนพิมพ์ชื่อของตนเอง : ABCDEFG
นามสกุลของตนเอง : AAAAAA
อายุของตนเอง : 12
อายุของน้อง : 100
ชื่อ : ABCDEFG data type : <class 'str'>
นามสกุล : AAAAAA data type : <class 'str'>
อายุ : 12 ปี data type : <class 'int'>
อายุน้องสาว : 100 ปี data type : <class 'int'>
อายุต่างกับน้องสาว : 88 ปี
"""