def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol=1e-6, max_iter=3):
    for i in range(1, max_iter + 1):
        x1 = x0 - f(x0)/df(x0)

        print(f"Iteration {i}: x = {x1}")

        if abs(x1 - x0) < tol:
            break

        x0 = x1

    return x1

print("Final root after 3 iterations:", newton_raphson(1.5))
