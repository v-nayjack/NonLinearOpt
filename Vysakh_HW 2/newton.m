% Vysakh Venugopal (M10665532) Assignment #2 - Problem 2

%%%%%%%%%%%%%%%%% NEWTON'S METHOD %%%%%%%%%%%%%%%%%%%%%
function [x_min, Fmin] = newton(F,x0)
% newton is a gradient based method to calculate minimum of a multivariate 
% function
% xmin : minimum variable
% Fmin : Function value @ xmin
% F    : Objective Function
% x0   : Initial guess

% Changing structure of x0 to match the implementation
if size (x0,2) ~= 1
    x0 = x0';
end

% Tolerance
eps = 1e-6;

% Maxloop
maxloop = 50000;
loop = 0;
done = false;

while ~done
    g0 = gradient(F,x0);                % Gradient
    G0 = hessian(F,x0);                 % Hessian    
    [~,p] = chol(G0);                   % Metric using Cholesky Factorization
    if p==0 && rank(G0) == size(G0,1)   % if positive definite
        pk = -G0\g0;                    % Newton's correction
    else
        pk = -g0;                       % Steepest descent
    end
    s = Armijo_Line_search(F,x0,pk);    % Weak line search
    xk = x0 + s*pk;                     % Update
    x0 = xk;
    loop = loop +1;
    if norm(g0) <= eps
        x_min = xk;
        Fmin = F(x_min);                % Stopping criteria
        done = true;
    end
    if loop == maxloop
        disp('Went overboard');
    end
end
end

    