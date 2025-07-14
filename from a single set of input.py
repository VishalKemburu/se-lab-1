hours = [0, 6, 12, 14, 18, 23]

def get_temperature(t):
    a = -0.1
    b = 2.8
    c = 5
    return round(a * t * t + b * t + c, 2)

for hour in hours:
    temp = get_temperature(hour)
    print(f"{hour}:00 -> Temperature: {temp}°C")
