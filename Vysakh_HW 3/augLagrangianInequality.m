% Vysakh Venugopal Nonlinear Optimization HW #3 - Problem 2
function [xmin] = augLagrangianInequality(F,c,x0,r0,v0,beta)
% augLagrangianInequality calculates the minimum of a function constraint by
% inequality constraints


% Error Message if user inout beta is less than one
if beta >= 1
    disp('The penalty growth constant should be less than one');
end
if size(v0,2) ~= 1
    v0 = v0';
end
maxloop = 200;
done = false;
loop = 0;
while ~done
    % Augmented Lagrangian Function
    F_aug = @(x) F(x) + (1/r0).*(sum((min(0,(c(x)-(r0/2).*v0))).^2));
    
     % Unconstrained Optimization
    options = optimoptions(@fminunc,'Display','none','Algorithm','quasi-newton');
    xk = fminunc(F_aug,x0,options);
    
    % v update
    if c(xk) < (r0/2) * v0
        vk = v0 - ((2/r0)*c(xk));
    else
        vk = 0;
    end
    
    % r update
    rk = beta*r0;
    r0 = rk;
    v0 = vk;
    change = x0-xk;
    x0 = xk;
    loop = loop + 1;
    fprintf('Iteration #%i\n',loop);
    
    % stopping criteria
    if norm(c(xk)) <= 1e-8
        xmin = xk;
        break;
    end
    if abs(change) <= 1e-4
        xmin = xk;
        break;
    end
    if loop >= maxloop
        break;
    end
end
end

    