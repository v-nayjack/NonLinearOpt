function [dist] = routing(p,c,r,rho)
% Nonlinear Optimization Assignment #1 - Vysakh Venugopal(M10665532)
%routing calculates the optimal distance along the horizontal line to reach
%target point P such that the circle with center C and radius r is avoided
%p: target point coordinate (xp,yp)
%c: coordinate of the center of circle (xc,yc)
%r: radius of the circle
%rho: penalty

% Parts of the objective function
A = @(dist)(((dist-p(1)).^2) + (p(2).^2));
B = @(dist)(2.*(((p(1)-dist).*(dist-c(1)))-(p(2).*c(2))));
C = @(dist)(((dist-c(1)).^2) + (c(2).^2) - (r.^2));
D = @(dist)((B(dist).^2) - (4.*A(dist).*C(dist)));

% Objective function
F = @(dist) (dist + ((A(dist).^0.5).*(1 + (rho.*abs((D(dist).^0.5)./A(dist))))));

% Optimization
[a,b] = interval_scan(F,5.5,0.01);
[dist] = bisection(F,a,b,1e-3);

%Plots
figure(6);
rectangle('Position',[1 1 2 2],'Curvature',[1,1],'EdgeColor','b');
axis equal;
hold on
scatter([p(1);c(1)],[p(2);c(2)]);
hold on
plot([0;dist],[0,0],'r');
hold on
plot([dist;p(1)],[0,p(2)],'k');
xlabel('X-axis');
ylabel('Y-axis');
title('Routing problem')
legend('Center and Target','Route on X-axis','Route to Target');
end