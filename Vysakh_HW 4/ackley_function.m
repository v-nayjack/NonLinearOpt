% Vysakh Venugopal (M10665532) Assignment #4 - Problem 4

%%%%%%%%%%%%%%%%% ACKLEY FUNCTION %%%%%%%%%%%%%%%%%%%%%
function F = ackley_function(x)
% ackley_function
% x: input data ([x,y])
F = -20.*exp(-0.2.*(0.5.*(x(1).^2+x(2).^2)).^0.5)-exp(0.5.*(cos(2*pi*x(1))+cos(2*pi*x(2))))+exp(1)+20;
end

