% Vysakh Venugopal (M10665532) Assignment #4 - Problem 3

%%%%%%%%%%%%%%%%% PARTICLE SWARM OPTIMIZATION %%%%%%%%%%%%%%%%%%%%%
function xmin = particle_swarm(F,dimension,particles,maxloop,inertia,phip,phig,lb,ub)
%PARTICLE_SWARM finds global optimum of an objective function using particle swarm
%optimization method
% F: Objective Function
% dimension: Dimension of the problem
% particles: number of particles
% maxloop: Maximum number of iterations
% inertia: inertia coefficient
% phip: weighting coefficient for personal best position
% phig: weighting coefficient for global best position
% lb: lower bound of search space in each dimension
% ub: upper bound of search space in each dimension

searchSpace = horzcat(lb,ub);
x0 = zeros(particles,dimension);    % input initialization
v0 = zeros(particles,dimension);    % velocity initialization
for i = 1:dimension
    x0(:,i) = (searchSpace(i+dimension) - searchSpace(i)).*rand(particles,1) + searchSpace(i);
    v0(:,i) = rand(particles,1);
end
xp = x0;        % local best is set as initial input
Fp = zeros(particles,1);
for i = 1:particles
    Fp(i) = F(xp(i,:));
end
[~,idx] = min(Fp);      % finding minimum input
xg = xp(idx,:);
loop = 1;
while loop <= maxloop
    for i = 1:particles
        v0(i,:) = inertia*v0(i,:) + phip*rand(1)*(xp(i,:) - x0(i,:)) + phig*rand(1)*(xg - x0(i,:));     % velocity update
        x0(i,:) = x0(i,:) + v0(i,:);
        if F(x0(i,:)) < F(xp(i,:))
            xp(i,:) = x0(i,:);
            Fp(i) = F(xp(i,:));
        end
    end
    [~,idx] = min(Fp);
    xg = xp(idx,:);     % global best
    loop = loop + 1;
end
xmin = xg;
end
