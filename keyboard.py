hour = int(input("Enter hour (0-23): "))

a = -0.1
b = 2.8
c = 5
temperature = a * hour * hour + b * hour + c
print("Temperature is:", round(temperature, 2), "°C")