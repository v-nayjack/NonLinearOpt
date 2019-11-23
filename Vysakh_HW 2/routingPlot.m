% Vysakh Venugopal (M10665532) Assignment #2 - Problem 6
%%%%%%%%%%%%%%%%% ROUTING PROBLEM %%%%%%%%%%%%%%%%%%%%%

flagClear = input('Do you want to clear the workspace? (1-Yes & 0-NO)\n');
if flagClear == 1
    clear;
end
flagClc = input('Do you want to clear the command window? (1-Yes & 0-NO)\n');
if flagClc == 1
    clc;
end
n = input('Do you want to use Powell''s method (1) or quasi_newton (2)?\n');

% Three test cases given in assignment

m = input('Enter the test case number from (1-4)\n');

switch m
    case 1
        p = [5 3]; c = [2 2]; r = 1; rho = 3 ;s1 = [1 2.5]; s2 = [1 1.5];
    case 2
        p = [2,4]; c = [2 2]; r = 1; rho = 10 ;s1 = [1 2.5];  s2 = [1 2.5];
    case 3
        p = [3 3]; c = [2 2]; r = 1; rho = 2 ;s1 = [2.5,1]; s2 = [2.5 1];
    case 4
        p = [1 1]; c = [2 2]; r = 1; rho = 2 ;s1 = [2.5,1]; s2 = [0.9 0.5];
end

[F] = @(x) route(x,p,c,r,rho);

switch n
    case 1
        [xmin] = powellMethod(@(x)F(x),s1,[0 0],[5 5]);
    case 2
        [xmin,Fmin] = quasi_newton(@(x)F(x),s2);
end

% Plotting the route
figure(1);
rectangle('Position',[1 1 2 2],'Curvature',[1,1],'EdgeColor','b');
axis equal;
hold on
scatter(c(1),c(2),'sk');
hold on
scatter(p(1),p(2),'g');
hold on
scatter(xmin(1),xmin(2),'*r');
hold on
plot([0;xmin(1)],[0;xmin(2)],'--r');
hold on
plot([xmin(1);p(1)],[xmin(2);p(2)],'--k');
xlabel('X-axis');
ylabel('Y-axis');
title('Routing');
legend('Center','Target','Intermediate Point','Path 1','Path 2');

% Plotting the objective function
x = 0:0.1:10;
y = 0:0.1:10;
[X,Y] = meshgrid(x);
temp = length(X);
X_temp = reshape(X,numel(X),1);
Y_temp = reshape(Y,numel(Y),1);
F_val = zeros(numel(X),1);
for i = 1:numel(X)
    temp1 = [X_temp(i),Y_temp(i)];
    F_val(i) = F(temp1);
end
F_val = reshape(F_val,temp,temp);
figure(2);
surf(X,Y,F_val);
xlabel('x');
ylabel('y');
zlabel('Function');
title('Routing Objective Function');