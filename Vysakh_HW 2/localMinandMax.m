% Vysakh Venugopal (M10665532) Assignment #2 - Problem 4

flagClear = input('Do you want to clear the workspace? (1-Yes & 0-NO)\n');
if flagClear == 1
    clear;
end
flagClc = input('Do you want to clear the command window? (1-Yes & 0-NO)\n');
if flagClc == 1
    clc;
end


%%%%%%%%%%%%%%%%%%%%%%%% POWELL'S METHOD %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Given Function for minimization
F = @(x)((x(1)^2 + x(2) - 11)^2 + (x(1) + x(2).^2 - 7)^2);

% Function for minimization
Fm = @(x) -1.*((x(1)^2 + x(2) - 11)^2 + (x(1) + x(2).^2 - 7)^2);

% Initial Guess
x0 = [-5 -5; 5 -5; -3 3; 5 5; 3.001 1.998];

% Left Bound
L = [-5 -5];

% Right Bound
U = [5 5];

% Initialize
min = zeros(length(x0),2);
max = zeros(length(x0),2);
F_min = zeros(length(x0),1);
F_max= zeros(length(x0),1);

for i = 1: length(x0)
    min(i,:) = powellMethod(F,x0(i,:),L,U);         % Minimization
    F_min(i) = F(min(i,:));
    max(i,:) = powellMethod(Fm,x0(i,:),L,U);        % Maximization
    F_max(i) = F(max(i,:));
end

[c] = unique(round(min),'rows');
numLocalMinima = length(c);                         % #minima
numLocalMaxima = numel(~isnan(F_max),2);            % #maxima

fprintf('The number of local minima is %i\n',numLocalMinima);
fprintf('The number of local maxima is %i\n',numLocalMaxima);
