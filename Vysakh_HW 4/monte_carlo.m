% Vysakh Venugopal (M10665532) Assignment #4 - Problem 1

%%%%%%%%%%%%%%%%% MONTE CARLO METHOD %%%%%%%%%%%%%%%%%%%%%
function [xmin] = monte_carlo(F,N,dimension,lb,ub)
%MONTE_CARLO finds global optimum of an objective function using Monte
%Carlo method
% F: Objective Function
% N: Number of random points
% dimension : Function dimension
% lb: lower bound of search space
% ub: uower bound of search space

searchSpace = horzcat(lb,ub); % search space generation
input = zeros(N,dimension);   % input initialization
for i = 1:dimension
    input(:,i) = (searchSpace(i+dimension) - searchSpace(i)).*rand(N,1) + searchSpace(i);
end
Fp = zeros(N,1);
for i = 1:N
    Fp(i) = F(input(i,:));
end
[~,idx] = min(Fp);
minimizerIp = input(idx,:); % Finding input that gave the lowest obj. func. value
options = optimoptions(@fminunc,'Display','none','Algorithm','quasi-newton');
xmin = fminunc(F,minimizerIp,options);
end

