clear
clc
close
%% Inputs

F = @(x) rosenbrock_obj(x);
n = input('Choose any one dimension from (2, 3, 5, and 7)\n');
switch n
    case 2
        x0 = [0.5 0.5];
    case 3
        x0 = [0.6 0.5 0.7];
    case 5
        x0 = [0.6 0.5 0.7 0.5 0.5];
    case 7
        x0 = [0.6 0.5 0.7 0.5 0.5 0.6 0.5];
    otherwise
        disp('Enter the initial guess array of your choice');
end
beta = 0.1;
r0 = 0.25;
v0 = 1;
v0_eq = 1; v0_ineq = 1;
dim = length(x0);
%% Problem 4a
c4a = @(x)norm(x).^2 -1;
[xmin_prob4a] = augLagrangianEquality(F,c4a,x0,r0,v0,beta);

%% Problem 4b
C = horzcat(-1,ones(1,dim-1)); c4b = @(x) norm(x-C)^2 - 1;
[xmin_prob4b] = augLagrangianEquality(F,c4b,x0,r0,v0,beta);

%% Problem 4c
c4c = @(x)1-norm(x).^2;
[xmin_prob4c] = augLagrangianInequality(F,c4c,x0,r0,v0,beta);

%% Problem 4d
C = horzcat(-1,ones(1,dim-1)); c4d = @(x) 1 - norm(x-C)^2;
[xmin_prob4d] = augLagrangianInequality(F,c4d,x0,r0,v0,beta);

%% Problem 4e 
C = 0.5.*horzcat(-1,ones(1,dim-1));
c_eq = @(x) norm(x-C).^2 - 1;
c_ineq = @(x) 1-(norm(x)).^2;
[xmin_prob4e] = augmented_lagrangian(F,c_eq,c_ineq,x0,v0_eq,v0_ineq,r0,beta);
% answer = vertcat(xmin_prob4a,xmin_prob4b,xmin_prob4c,xmin_prob4d,xmin_prob4e);
