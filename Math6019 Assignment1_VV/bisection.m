function [c] = bisection(f,a,b,tol)
% Nonlinear Optimization Assignment #1 - Vysakh Venugopal(M10665532)
% bisection calulates the local minima of a function using interval [a,b]
% using the bisection method
%f: function
%a: lower interval
%b: upper iterval
%tol: tolerance
%c: minima

% Finding number of iterations
n = log(tol)/log(0.75);

for i = 1:ceil(n)
    
    % Bisection
    c = (a+b)/2;
    l = (a+c)/2;
    r = (c+b)/2;
    % Updating scheme
    if f(l)>f(r)
        a = l;
    elseif f(r)>f(l)
        b = r;
    else
        a = l;
        b = r;
    end
end
fprintf('The minima is at %2f and the value of function is %2.3f\n',c,f(c));
figure(2);
fplot(f,'b');
hold on
plot([a,b],[f(a),f(b)],'--r');
hold on
scatter(c,f(c));
xlabel('x');
ylabel('f(x)');
title('Objective Function');
str_c = sprintf('c(%1.4g,%1.4g)',c,f(c));
text(c,f(c),{str_c})
legend('Function','Line ab','Local Minima')
end
