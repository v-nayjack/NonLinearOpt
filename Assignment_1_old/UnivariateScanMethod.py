import sympy as sp
sp.init_printing()

def univariatescan(func, X0, Alpha):
    y = sp.symbols('x')    
    fprime = sp.diff(func,y)
    fdprime = sp.diff(func,y,y)
    # Checking to see if the initial guess is a maximum
    if fdprime.subs(y,X0) < 0: 
        print("Initial guess is a maximum")
        xright = X0+Alpha
        xleft = X0-Alpha
        if fdprime.subs(y,xright) > fdprime.subs(y,xleft):
            X0 = xright
        else:
            X0 = xleft
    # Checking to see if the initial guess is point of inflection       
    if fdprime.subs(y, X0) == 0: 
        print("Initial guess is the point of inflection")
        xright = X0+Alpha
        xleft = X0-Alpha
        if fdprime.subs(y,xright) > fdprime.subs(y,xleft):
            X0 = xright
        else:
            X0 = xleft      
    delt =(-(Alpha) * fprime.subs(y, X0))    
    Xk = X0
    Xk_f = Xk + delt
    new = func.subs(y, Xk_f)
    old = func.subs(y, Xk)
    k = 0
    while old > new:
        # Condition for local minimum
        if fprime.subs(y, X0) == 0 and fdprime.subs(y, X0) > 0: 
            a = Xk
            b = Xk_f
            print ("Initial guess entered is the minimum")
            break
        delt = 2*delt
        Xk_b = Xk
        Xk = Xk_f
        Xk_f = Xk + delt
        new = func.subs(y, Xk_f)
        old = func.subs(y, Xk)
        if k == 0:
            a = min(Xk,Xk_f)
            b = max(Xk,Xk_f)
            break
        elif k > 0:
            a = min(Xk_b, Xk_f)
            b = max(Xk_b, Xk_f)    
        k+=1   
    return [a, b]


x = sp.symbols('x')

func = x**3-3*x**2
x0 = 1.0
alpha = 0.01
a,b=univariatescan(func,x0, alpha)

print(a, b)