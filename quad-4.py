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
    with open("input1.txt", "r") as file:
        line_number = 1
        for line in file:
            try:
                a1, b1, c1 = line.strip().split()
                a = float(a1)
                b = float(b1)
                c = float(c1)

                print(f"\nSet {line_number}: a={a}, b={b}, c={c}")
                if a == 0:
                    print("Not a quadratic equation")
                else:
                    equationroots(a, b, c)

                line_number += 1

            except ValueError:
                print(f"Invalid data in line {line_number}: '{line.strip()}'")
                line_number += 1

except FileNotFoundError:
    print("Input file not found")
