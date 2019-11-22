function [a,b] = interval_scan(f,x,h)
% Nonlinear Optimization Assignment #1 - Vysakh Venugopal(M10665532)
%interval_scan scans a univariate objective function for an interval that
%contains the local minimum given an initial guess
%f: function
%x: initial guess
%h: step size

% First derivative
df_initial = (f(x + h)-f(x))/h;

% Decide step direction based on derivative sign
if df_initial > 0
    delta = -h;
else
    delta = h;
end
loop = 0;
done = false;
while done == false
    if f(x+delta) > f(x)
        % Upper interval
        a = min(x-(0.5*delta),x+(delta));
        % Lower interval
        b = max(x-(0.5*delta),x+(delta));
        done = true;
    end
    % Variable update
    x = x + delta;
    
    % Step size doubling
    delta = 2*delta;
    loop = loop +1;
end
% If model converges in first iteration
if loop == 0
    a = min(x,x+delta);
    b = max(x,x+delta);
end

% Plot 
fprintf('The model converged in %2d iterations\n',loop);
fprintf('The interval is [%2.4f %2.4f]\n',a,b);
figure(1);
fplot(f,[a-2,b+2],'b');
hold on
plot([a,b],[f(a),f(b)],'--r');
xlabel('x');
ylabel('f(x)');
title('Interval Scan');
legend('Function','Line ab')
str_a = sprintf('a(%1.4g,%1.4g)',a,f(a));
str_b = sprintf('b(%1.4g,%1.4g)',b,f(b));
text([a,b],[f(a),f(b)],{str_a, str_b});
end

