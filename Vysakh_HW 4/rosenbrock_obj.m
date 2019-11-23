% Vysakh Venugopal (M10665532) Assignment #4 - Problem 5

%%%%%%%%%%%%%%%%% ROSENBROCK FUNCTION %%%%%%%%%%%%%%%%%%%%%
function [F] = rosenbrock_obj(data)
% rosenbrock_obj is the rosenbrock function for N dimensions
% F: Function
% data : input data

% TESTING IS CARRIED OUT IN A SCRIPT FILE LATER

% Changing structure of x0 to match the implementation
if size(data,2) ~= 1
    data = data';
end

N = length(data);
F = 0;
for i = 1:N-1
    xi = data(i);
    xii = data(i+1);
    sum = 100*(xii-xi^2)^2 + (1-xi)^2;          % a = 1 & b = 100;
    F = F + sum;
end
end
