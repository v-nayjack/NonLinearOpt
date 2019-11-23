% Vysakh Venugopal (M10665532) Assignment #4 - Problem 5
%%%%%%%%%%%%%%%%% ROSENBROCK FUNCTION %%%%%%%%%%%%%%%%%%%%%

clear
clc
close

F = @rosenbrock_obj;

% USING MONTE CARLO METHOD
[xmin_monteCarlo] = monte_carlo(@rosenbrock_obj,500,5,[0 0 0 0 0],[2 2 2 2 2]);

% USING BASIN HOPPING METHOD
[xmin_bh] = basin_hopping(F,[2 3 4 5 6],1);

% USING PARTICLE SWARM OPTIMIZATION
[xmin_pso] = particle_swarm(F,5,500,100,0.5,2,2,[0 0 0 0 0],[2 2 2 2 2]);