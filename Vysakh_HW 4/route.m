% Vysakh Venugopal (M10665532) Assignment #4 - Problem 6

%%%%%%%%%%%%%%%%% ROUTING PROBLEM %%%%%%%%%%%%%%%%%%%%%
function F = route(intPoint,target,center,radius,penalty)

% route calculates the objective function of the routing problem
% intPoint : intermediate point
% target : target point p
% center : center of circle c
% radius : radius of circle r
% penalty

% Line Origin - To - Intermediate Point
A1 = intPoint(1).^2 + intPoint(2).^2;
B1 = 2*((-center(1)*intPoint(1)) + (-center(2)*intPoint(2)));
C = center(1).^2 + center(2).^2 - radius.^2;
D1 = B1^2 - 4*A1*C; % Discriminant
v1 = 0;
if D1 > 0
   s1 = (-B1 + D1.^0.5) / (2*A1);
   s2 = (-B1 - D1.^0.5) / (2*A1);
   if s1 >= s2
       temp = s2;
       s2 = s1;
       s1 = temp;
   end
   if (s1 < 1 && s2 < 1) || (s1 < 0 && s2 < 0)
       v1 = (min(s2,1) - max(s1,0)).*(A1.^0.5);
   else
       v1 = 0;
   end
end
F1 = (A1.^0.5) + (penalty*v1.^3);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Line Intermediate point - To - Target
A2 = (target(1)-intPoint(1)).^2 + (target(2)-intPoint(2)).^2;
B2 = 2*((intPoint(1)-center(1))*(target(1)-intPoint(1)) + (intPoint(2)-...
    center(2))*(target(2)-intPoint(2)));
C2 = (intPoint(1)-center(1)).^2 + (intPoint(2)-center(2)).^2 - radius.^2;
D2 = B2^2 - 4*A2*C2; % Discriminant
v2 = 0;
if D2 > 0
   s11 = (-B2 + D2.^0.5) / (2*A2);
   s22 = (-B2 - D2.^0.5) / (2*A2);
   if s11 >= s22
       temp = s22;
       s22 = s11;
       s11 = temp;
   end
   if (s11 < 1 && s22 < 1) || (s11 < 0 && s22 < 0)
       v2 = (min(s22,1) - max(s11,0)).*(A2.^0.5);
   else
       v2 = 0;
   end
end
F2 = (A2.^0.5) + (penalty*v2.^3);

% Final objective function
F = F1 + F2;

end