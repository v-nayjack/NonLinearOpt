function [c] = bisection_method(f,a,b)
% Nonlinear Optimization Assignment #1 - Vysakh Venugopal(M10665532)
% bisection calulates the local minima of a function using interval [a,b]
% using the bisection method
%f: function
%a: lower interval
%b: upper iterval
%c: minima

% Finding number of iterations
maxloop = 200;
tol = 1e-6;
loop = 0;
done = false;
while done == false
    
    % Bisection
    c = (a+b)/2;
    l = (a+c)/2;
    r = (c+b)/2;
    
    % Updating scheme
    f_set=[f(a),f(b),f(c),f(l),f(r)];
    
    if isequal(min(f_set),f(a)) || isequal(min(f_set),f(l))
        b=c;
    elseif  isequal(min(f_set),f(b)) || isequal(min(f_set),f(r))
        a=c;
    else
        a=l;
        b=r;
    end
    
    loop = loop +1;
    
    % Stopping criteria
    if abs(b-a) <= tol
        break;
    elseif loop >= maxloop
        break;
    end
end
end
