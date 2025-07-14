hours = [0, 6, 12, 14, 18, 23]

for hour in hours:
    temp = -0.1 * hour * hour + 2.8 * hour + 5
    print(f"{hour}:00 -> Temperature: {round(temp, 2)}°C")
