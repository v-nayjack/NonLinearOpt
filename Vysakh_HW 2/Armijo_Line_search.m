function [s] = Armijo_Line_search(F,x0,pk)

C = 1.1;
c = 0.9;
maxloop = 200;
loop = 0;
eta1 = 0.4;
eta2 = 0.4;
g = gradient(F,x0);
s = 1;
while loop < maxloop
    D = @(s) (F(x0 + s.*pk) - F(x0))./(s.*pk'*g);
    if abs(1-D(s)) <= eta2
        smin = s;
        s = C*s;
    else
        return;
    end
    s = smin + c*(s-smin);
    loop = loop +1;
    if D(s) <= eta1
        break;
    end
end

end

