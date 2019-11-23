% Vysakh Venugopal (M10665532) Assignment #2 - Problem 5
%%%%%%%%%%%%%%%%% TOTAL LEAST SQUARES %%%%%%%%%%%%%%%%%%%%%

flagClear = input('Do you want to clear the workspace? (1-Yes & 0-NO)\n');
if flagClear == 1
    clear;
end
flagClc = input('Do you want to clear the command window? (1-Yes & 0-NO)\n');
if flagClc == 1
    clc;
end

% LineFitplots finds and plots the best fit line passing through the origin
% for a set of noisy data

% m: slope
% b: intercept
% ei: magnitude of noise
% N: Number of data points

m = input('Enter value of slope for data\n');
b = input('Enter value of intercept for data\n');
ei = input('Enter value of error term ei \n');
N = input('Enter value of data points\n');
iniX = input('Enter initial guess as [slope intercept] format\n');

rng(0);

% Generating data points
y = zeros(1,N);
for i = 1:N
    y(i) = (m.*i) + b + (ei*((2*rand)-1));
end
data = horzcat((1:N)',y');

% Minimization
[a] = powellMethod(@(a)linefit(a,data),iniX,[0 1],[2,8]);

% Plotting
y = zeros(1,N);
for i = 1:N
    y(i) = (m.*i) + b + (ei*((2*rand)-1));
end
data = horzcat((1:N)',y');
bestFitline = @(x) a(1).*x + a(2);

fprintf('The optimal value of the slope is a = %1.4d\n',a(1));
fprintf('The optimal value of the intecept is b = %1.4d\n',a(2));

% Plot of best fit line
figure(1);
scatter(data(:,1),data(:,2),'b')
hold on
x = 1:N;
y = bestFitline(data(:,1));
plot(x,y);
xlabel('X-axis')
ylabel('Y-axis')
legend('Data Points','Best Fit Line');
title('Problem 5');


% Plot of the objective function

% Reformulating the function in terms of two separate variables
z = @(p,n)(data(:,1) + p.*data(:,2) - p.*n)./(p.^2 + 1);
Func = @(p,n) sum((data(:,1)- z(p,n)).^2 + (data(:,2)-(p.*z(p,n) + n)).^2); % Objective Function

x = 0:0.1:10;
y = 0:0.1:10;
[X,Y] = meshgrid(x);
temp = length(X);
X_temp = reshape(X,numel(X),1);
Y_temp = reshape(Y,numel(Y),1);
F = zeros(numel(X),1);
for i = 1:numel(X)
    F(i) = Func(X_temp(i),Y_temp(i));
end
F = reshape(F,temp,temp);

figure(2);
surf(X,Y,F);
xlabel('Slope');
ylabel('Intercept');
zlabel('Function');
title('Total Least Squares Objective Function');
