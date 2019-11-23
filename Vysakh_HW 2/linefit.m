% Vysakh Venugopal (M10665532) Assignment #2 - Problem 5

%%%%%%%%%%%%%%%%% TOTAL LEAST SQUARES %%%%%%%%%%%%%%%%%%%%%

function [F] = linefit(a,data)
% linefit finds the objective function whose minimum will give the best fit
% line passing through the origin for a set of noisy data
% data : input data
% a(1) : slope
% a(2) : intercept

z = (data(:,1) + a(1).*data(:,2) - a(1).*a(2))/(a(1).^2 + 1);

F = sum((data(:,1)- z).^2 + (data(:,2)-(a(1).*z + a(2))).^2); % objective function

end