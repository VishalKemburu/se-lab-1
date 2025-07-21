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
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Not a quadratic equation. Coefficient 'a' must not be zero.")
    else:
        equationroots(a, b, c)

except ValueError:
    print("Please enter valid numeric values.")
