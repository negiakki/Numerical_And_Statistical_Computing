def forward_diff_table(x, y):
    n = len(y)
    diff = [y.copy()]
    for i in range(1, n):
        temp = []
        for j in range(n - i):
            temp.append(diff[i-1][j+1] - diff[i-1][j])
        diff.append(temp)
    return diff

def newton_forward(x, y, value):
    diff = forward_diff_table(x, y)
    n = len(x)
    h = x[1] - x[0]
    u = (value - x[0]) / h

    result = y[0]
    u_term = 1
    fact = 1

    for i in range(1, n):
        u_term *= (u - i + 1)
        fact *= i
        result += (u_term * diff[i][0]) / fact

    return result

x = [0, 1, 2, 3]
y = [1, 2, 4, 8]

print(newton_forward(x, y, 1.5))
