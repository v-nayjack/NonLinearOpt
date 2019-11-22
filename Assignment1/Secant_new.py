import numpy as np
import matplotlib.pyplot as plt

def secant(f, X0, X1, tol= 1e-6, maxiter = 1e3):
    h = tol
    Xn = X1
    Xn_b = X0
    Fp_Xnb = (f(X0+h) - f(X0 - h))/(2*h)
    Fp_Xn = (f(X1+h) - f(X1 - h))/(2*h)
    iterations = 0
    m = np.linspace(-10, 10, 100000)
    F = []
    for i in range(len(m)):
        F.append(f(m[i]))

    while np.abs(Fp_Xn) > tol and iterations < maxiter:
        Fp_Xnb = (f(Xn_b + h) - f(Xn_b - h)) / (2 * h)
        Fp_Xn = (f(Xn + h) - f(Xn - h)) / (2 * h)
        Xn_f = Xn - (((Xn - Xn_b)* Fp_Xn)/(Fp_Xn - Fp_Xnb))
        Fp_Xnf = (f(Xn_f + h) - f(Xn_f - h)) / (2 * h)
        if abs(Fp_Xnf) <= tol:
            iterations = 1
            return Xn_f, iterations
        else:
            Xn_b = Xn
            Xn = Xn_f
        iterations += 1


    plt.plot(m, F, color = "red", linewidth = 2)
    plt.scatter(Xn_f,f(Xn_f), color = "blue", marker='o')
    plt.title("Objective Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()

    return Xn_f, iterations


f = lambda x: x**3 - 3* x**2

x0 = 1.45
x1 = 5.89

minimum, no_of_iterations = secant(f,x0,x1)

if no_of_iterations > 0:
    print("minimum =",minimum, "No. of iterations = ", no_of_iterations)
else:
    print("Solution not found. Try again!")