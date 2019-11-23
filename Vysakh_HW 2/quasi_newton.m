% Vysakh Venugopal (M10665532) Assignment #2 - Problem 2

%%%%%%%%%%%%%%%%% QUASI NEWTON'S METHOD %%%%%%%%%%%%%%%%%%%%%
function [x_min, Fmin] = quasi_newton(F,x0)
% quasi_newton is a gradient based method to calculate minimum of a multivariate
% function
% xmin : minimum variable
% Fmin : Function value @ xmin
% F    : Objective Function
% x0   : Initial guess

% Changing structure of x0 to match the implementation
if size (x0,2) ~= 1
    x0 = x0';
end

N = length(x0);
eps = 1e-6;
maxloop = 50000;
loop = 0;
H0 = eye(N);
done = false;

while ~done
    g0 = gradient(F,x0);                    % Gradient
    pk = -H0*g0;                            % Search Direction
    s = Armijo_Line_search(F,x0,pk);        % Weak Line Search
    xk = x0 + s*pk;
    gk = gradient(F,xk);                    % New gradient
    gammak = gk-g0;                         % Change in gradient
    deltak = xk-x0;                         % Change in variable
    Hk = (eye(N) - ((deltak*gammak')/(gammak'*deltak)))*H0*(eye(N) ...
        - ((gammak*deltak')/(gammak'*deltak))) +...                 % BFGS
        ((deltak*deltak')/(gammak'*deltak));
    x0 = xk;
    H0 = Hk;
    loop = loop +1;
    if norm(gk) <= eps
        x_min = xk;
        Fmin = F(x_min);
        done = true;
    end
    if loop == maxloop
        disp('Iteration exceeded maximum number!');
        break;
    end
    
end
end

