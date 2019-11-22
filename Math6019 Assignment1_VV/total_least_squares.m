function [a] = total_least_squares(m,b,ei,N)
% Nonlinear Optimization Assignment #1 - Vysakh Venugopal(M10665532)
% total_least_squares finds the best fit line passing through the origin
% for a set of noisy data
% m: slope
% b: intercept
% ei: magnitude of noise
% N: Number of data points

% Creating data
y = zeros(1,N);
for i = 1:N
    y(i) = (m.*i) + b + (ei*((2*rand)-1));
end
data = [1:N;y];

% Objective function
Func = @(a)sum((data(1,:)'- ((data(1,:)' + (a.*data(2,:)'))./((a.^2) +1))).^2 + (data(2,:)'-(a.*((data(1,:)' + (a.*data(2,:)'))./((a.^2) +1)))).^2);

% Newton_Raphson Method
[a] = newton_raphson(Func,0.5);

fprintf('The optimal value of the slope is a = %1.4d\n',a);
fprintf('The value of the objective function at minima is f(a) = %1.4d\n',Func(a));

%Plots
figure(4);
scatter(data(1,:),data(2,:),'b')
hold on
plot([0,length(data)],[0,length(data)*a],'r')
title(['The slope a is ',num2str(a),' and F(a) is ',num2str(Func(a))])
xlabel('X-axis')
ylabel('Y-axis')
legend('Data Points','Best Fit Line');
end