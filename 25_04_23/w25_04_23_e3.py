temprature = int(input('What\'s the temperature(F) : '))

if temprature >= 32 :
    celcius = (5*(temprature-32))/9
    print("The temperature in celsius is %0.1f" %celcius)
else :
    print("Cool")

#OUTPUT
"""
What's the temperature(F) : 50
The temperature in celsius is 10.0
"""