% Vysakh Venugopal (M10665532) Assignment #2 - Problem 3

flagClear = input('Do you want to clear the workspace? (1-Yes & 0-NO)\n');
if flagClear == 1
    clear;
end
flagClc = input('Do you want to clear the command window? (1-Yes & 0-NO)\n');
if flagClc == 1
    clc;
end

%%%%%%%%%%%%%%%%% ROSENBROCK FUNCTION  MINIMIZATION%%%%%%%%%%%%%%%%%%%%%
clear
clc
close 

% Input
x0 = 2.*ones(3,1);
[xmin,Fmin] = newton(@(x)rosenbrock_obj(x),x0);
