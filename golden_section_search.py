import math

PHI = (1 + math.sqrt(5)) / 2

def golden_section_search(f, a, b, tol=1e-8, max_iter=200):
    """Trova il minimo di una funzione unimodale f(x) in [a, b] tramite Golden Section Search."""
    x1 = b - (b - a) / PHI
    x2 = a + (b - a) / PHI
    f1, f2 = f(x1), f(x2)
    iterations = 0
    while abs(b - a) > tol and iterations < max_iter:
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - (b - a) / PHI
            f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + (b - a) / PHI
            f2 = f(x2)
        iterations += 1
    x_min = (a + b) / 2
    return {"x_min": x_min, "f_min": f(x_min), "iterations": iterations, "interval": (a, b)}

def verify_cassini_identity(n):
    """Verifica F_{n+1}*F_{n-1} - F_n^2 = (-1)^n"""
    fib = [0, 1]
    for i in range(2, n + 3):
        fib.append(fib[-1] + fib[-2])
    lhs = fib[n + 1] * fib[n - 1] - fib[n] ** 2
    rhs = (-1) ** n
    return lhs == rhs, lhs, rhs

if __name__ == "__main__":
    res = golden_section_search(lambda x: (x - 2) ** 2, 0, 5)
    ok, lhs, rhs = verify_cassini_identity(8)
    print("Golden Section Search:", res)
    print(f"Identità di Cassini (n=8): {lhs} == {rhs} -> {ok}")
