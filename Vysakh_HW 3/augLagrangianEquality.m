% Vysakh Venugopal Nonlinear Optimization HW #3 - Problem 1
function [xmin] = augLagrangianEquality(F,c,x0,r0,v0,beta)
% augLagrangianEquality calculates the minimum of a function constraint by
% equality constraints

maxloop = 200;
done = false;
loop = 0;
while ~done
    % Augmented Lagrangian Function
    F_aug = @(x) F(x) + (1/r0).*(norm(c(x)-((r0/2).*v0))).^2; 
    
    % Unconstrained Optimization
    options = optimoptions(@fminunc,'Display','none','Algorithm','quasi-newton');
    xk = fminunc(F_aug,x0,options);
    
    % v update
    vk = v0 - 2*c(xk)/r0;
    
    % r update
    rk = beta*r0;
    r0 = rk;
    v0 = vk;
   
    x0 = xk;
    loop = loop + 1;
    fprintf('Iteration #%i\n',loop);
    
    % Stopping criteria
    if norm(c(xk)) <= 1e-8
        xmin = xk;
        break;
    end
    if loop >= maxloop
        break;
    end
end
end

    