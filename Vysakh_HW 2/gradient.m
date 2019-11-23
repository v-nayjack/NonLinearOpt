function [g] = gradient(F,x0)
if size(x0,2) ~= 1
    x0 = x0';
end
N  = length(x0);
g = zeros(N,1);
h = 1e-8;
hh = h.*eye(N);
for i = 1:N
    g(i) = (F(x0+hh(:,i))-F(x0))/h;
end
end