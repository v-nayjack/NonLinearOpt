import sympy as sp
sp.init_printing()

def univariatescan(function, X0, Alpha=1e-2):
    y = sp.symbols('x')    
    fprime = sp.diff(function,y)
    #print(fprime)
    fdprime = sp.diff(function,y,y)
    #print(fdprime)
    
    # Checking to see if the initial gx**3uess is a maximum
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
    new = function.subs(y, Xk_f)
    old = function.subs(y, Xk)
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
        new = function.subs(y, Xk_f)
        old = function.subs(y, Xk)
        
        if k == 0:
            a = Xk
            b = Xk_f
            break
            
        
        elif k > 0:
            a = min(Xk_b, Xk_f)
            b = max(Xk_b, Xk_f)
            
        k+=1
        
        
    return [a, b]


m = input("Enter an Equation:")
s = sp.simplify(m)
print(s)

x0 = float(input("Please enter an initial guess:"))
#print("The initial guess for the function "+ s + 'is' + x0)

[a, b]=univariatescan(s, x0)

print(a, b)
    