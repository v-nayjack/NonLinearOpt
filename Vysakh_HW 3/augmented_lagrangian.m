% Vysakh Venugopal Nonlinear Optimization HW #3 - Problem 3
function [xmin] = augmented_lagrangian(F,c_eq,c_ineq,x0,v0_eq,v0_ineq,r0,beta)
% augmented_lagrangian calculates the minimum of a function constraint by
% equality and inequality constraints


% Error Message if user inout beta is less than one
if beta >= 1
    disp('The penalty growth constant should be less than one');
end
if size(v0_eq,2) ~= 1
    v0_eq = v0_eq';
end
if size(v0_ineq,2) ~= 1
    v0_ineq = v0_ineq';
end
maxloop = 200;
done = false;
loop = 0;
while ~done
    
    % Augmented lagrangian
    F_aug = @(x) F(x) + (1/r0).*(norm(c_eq(x)-((r0/2).*v0_eq))).^2 + (1/r0).*(sum((min(0,(c_ineq(x)-(r0/2).*v0_ineq))).^2));
    
    % Unconstrained optimization
    options = optimoptions(@fminunc,'Display','none','Algorithm','quasi-newton');
    xk = fminunc(F_aug,x0,options);
    
    % v update for equality constraints
    vk_eq = v0_eq - 2*c_eq(xk)/r0;
    
    % v update for inequality constraints
    if c_ineq(xk) < (r0/2) * v0_ineq
        vk_ineq = v0_ineq - ((2/r0)*c_ineq(xk));
    else
        vk_ineq = 0;
    end
    
    % r update
    rk = beta*r0;
    r0 = rk;
    v0_ineq = vk_ineq;
    v0_eq = vk_eq;
    change = x0-xk;
    x0 = xk;
    loop = loop + 1;
    fprintf('Iteration #%i\n',loop);
    
    % Stopping criteria
    if norm(c_eq(xk)) <= 1e-8 && norm(c_ineq(xk)) <= 1e-8
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