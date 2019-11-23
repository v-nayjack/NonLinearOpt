% Vysakh Venugopal (M10665532) Assignment #2 - Problem 1

%%%%%%%%%%%%%%%%% POWELL'S METHOD %%%%%%%%%%%%%%%%%%%%%
function [min] = powellMethod(F,iniX,L,U)

% powellmethod finds the minimum of a multivariate function using a 
% univariate scan in each direction
% F: Function
% iniX: initial guess - [N * 1] or [1 * N] vector (N: # of dimensions)
% L: Lower limit of the hyperbox ; same dimension as iniX
% R: Upper limit of the hyperbox ; same dimension as iniX
% maxloop: maximum # of iterations as a stopping criteria

% # of variables
N = length(iniX);
maxloop = 20000;

% Initialize search directions; unit vectors along coordinate axes
searchDir = eye(N);

% Stopping tolerance
eps = 1e-8;

loop = 0;
change = 1;

% Set of step size changes
s_set = zeros(N,1);

while change >= eps
    min = iniX;                                     % set z = x0
    for i = 1:N
        f = @(s) F(min + (s.*searchDir(i,:)));      % obj. function of step size s
        a = L(i)-min(i);                            % bisection method lower bracket
        b = U(i)-min(i);                            % bisection method upper bracket
        [s] = bisection_method(f,a,b);              % search
        min = min + s.*searchDir(i,:);              % variable update
        s_set(i) = s;
    end
    [~,index] = max(vecnorm(s_set.*searchDir));     % finding best search direction
    searchDir(index,:) = min-iniX;                  % replacing with best search direction
    change = norm(min-iniX);                        % stopping criteria calculation
    iniX = min;
    loop = loop + 1;
    if loop > maxloop
%         fprintf('The number of iterations reached beyond maximum iteration');
        break;
    end
end
end

        
        
