width = int(input("Width : "))
lenght = int(input("Length : "))
if width or lenght > 0 :

    print(f'Area of the square = {width} x {lenght} = {width*lenght}')
else :
    print('Please enter positive integer')

#OUTPUT
"""
Width : 50
Length : 70
Area of the square = 50 x 70 = 3500
"""