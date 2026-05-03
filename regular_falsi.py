def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return

    c = a
    while True:
        c_old = c
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))

        if abs(c - c_old) < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

print(regula_falsi(1, 2))
