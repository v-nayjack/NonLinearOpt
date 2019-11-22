function [x] = newton_raphson(f,x0)
% Nonlinear Optimization Assignment #1 - Vysakh Venugopal(M10665532)
% newton_raphson calcualtes the  minima of the function with initial guess x0.
%f: function
%x0: initial guess

done = false;
% Step size
h = 0.01;
iter = 0;
while done == false
    df = (f(x0 + h)-f(x0))/h; % First derivatives
    d2f = (f(x0+h)-(2*f(x0))+f(x0-h))/(h^2); % Second derivatives
    x = x0-(df/d2f); %Variable update
    if abs(f(x)-f(x0)) <= 1e-3 %stopping criteria
        done = true;
    end
    x0 = x;
    iter = iter + 1;
    fprintf('Iteration %2d\n',iter);
end

%Plot
figure(3);
fplot(f,'b');
hold on
scatter(x,f(x));
xlabel('x');
ylabel('f(x)');
title('Newton Raphson Method');
legend('Function','Local Minima')