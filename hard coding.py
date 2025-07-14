def get_temperature(hour):
    a = -0.1
    b = 2.8
    c = 5
    t = hour
    T = a * t * t + b * t + c
    return round(T, 2)

for hour in range(24):
    temp = get_temperature(hour)
    print(f"{hour:02d}:00 - Temperature: {temp}°C")