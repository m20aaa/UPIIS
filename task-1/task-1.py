def power(base, exp):
    if (exp == 0):
        return 1
    if (exp == 1):
        return base
    else:
        return (base * power(base, exp - 1))

base = float(input("Введите число, используя в виде разделителя точку: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))