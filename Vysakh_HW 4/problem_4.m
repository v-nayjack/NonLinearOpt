% Vysakh Venugopal (M10665532) Assignment #4 - Problem4
%%%%%%%%%%%%%%%%% ROSENBROCK FUNCTION %%%%%%%%%%%%%%%%%%%%%

clear
clc
close

F = @ackley_function;

% USING MONTE CARLO METHOD
% [xmin_monteCarlo] = monte_carlo(F,500,2,[0 0],[2 2])

% USING BASIN HOPPING METHOD
%[xmin_bh] = basin_hopping(F,[0.5 0.5],1)

% USING PARTICLE SWARM OPTIMIZATION
[xmin_pso] = particle_swarm(F,2,500,100,0.5,2,2,[0 0],[2 2]);