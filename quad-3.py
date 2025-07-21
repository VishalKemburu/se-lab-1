import math
def equationroots(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        print("Real and different roots:")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif dis == 0:
        print("Real and same roots:")
        print(-b / (2 * a))
    else:
        print("Complex roots:")
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val / (2 * a)
        print(f"{real_part} + {imaginary_part}i")
        print(f"{real_part} - {imaginary_part}i")
try:
    with open("input.txt", "r") as file:
        line = file.readline()
        a1, b1, c1 = line.strip().split()
        a=float(a1)
        b=float(b1)
        c=float(c1)
        if a == 0:
            print("Not a quadratic equation")
        else:
            equationroots(a, b, c)
except FileNotFoundError:
    print("Imput file not found")
except ValueError:
    print("Invalid data in file")
