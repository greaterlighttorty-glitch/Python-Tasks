celsius = float(input("Enter temperature: "))
for index in range(5):
    temperature = celsius + index

    if temperature < -273:
        print("impossible!")

    else: 
       fahrenheit = (temperature * 9/5) + 32
       print(fahrenheit)
