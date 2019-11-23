% Vysakh Venugopal (M10665532) Assignment #4 - Problem 2

%%%%%%%%%%%%%%%%% BASIN HOPPING METHOD %%%%%%%%%%%%%%%%%%%%%
function [xmin] = basin_hopping(F,x0,T)
%BASINHOP finds global optimum of an objective function using basin hopping
%method
% F: Objective Function
% x0: initial estimate
% T: Temperature

options = optimoptions(@fminunc,'Display','none','Algorithm','quasi-newton');
z0 = fminunc(F,x0,options); % local minimum
Tmin = 1e-8;    % Temperature minimum 
done = false;
maxloop = 1000;
loop = 0;
while ~done
    xstep = x0 + 0.01*rand(1);
    options = optimoptions(@fminunc,'Display','none','Algorithm','quasi-newton');
    zstar = fminunc(F,xstep,options);
    p = exp(-(F(zstar)-F(z0))/T);   % acceptance probability
    if rand(1) <= p
        x0 = xstep;
        z0 = zstar;
    end
    T = T*((0.95)^loop); % temperature update
    if T <= Tmin
        done = true; % stopping criteria
        xmin = z0;
    end
    loop = loop + 1;
    if loop >= maxloop
        fprintf('Loop: %i\n',loop);
        error('Loop exceeded maxloop');
    end
end
end
