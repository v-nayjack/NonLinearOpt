function [G] = hessian(F,x0)
if size(x0,2) ~= 1
    x0 = x0';
end
N  = length(x0);
G = zeros(N);
h1 = 1e-8;
h2 = 1;
hh1 = h1.*eye(N);
hh2 = h2.*eye(N);
for i = 1:N
    for j = 1:N
        G(i,j) = round((F(x0+hh1(:,i)+hh2(:,j))-F(x0 + hh1(:,i))-F(x0 + hh2(:,j))+F(x0))./h1*h2);
    end
end
end

