%%
%Author: Sai Ajjarapu
%Spring 2019

function [Displacement_Fall_Poly] = Fall_code_Poly(beta1,beta2,y)
beta = beta2 - beta1;
Displacement_Fall_Poly = struct();
for curve = 1:2
    %% Selecting the curve and calculating the equations
    switch(curve)
        case 1 %3,4,5 Poly
            theta = linspace(0,beta);
            Displacement_Fall_Poly(curve).theta = theta;
            Displacement_Fall_Poly(curve).S = y * ((10*theta.^3)/beta.^3 - (15*theta.^4)/beta.^4 + (6*theta.^5)/beta.^5);
            Displacement_Fall_Poly(curve).V = y * ((30*theta.^2)/beta.^3 - (60*theta.^3)/beta.^4 + (30*theta.^4)/beta.^5);
            Displacement_Fall_Poly(curve).A = y * ((60*theta)/beta.^3 - (180*theta.^2)/beta.^4 + (120*theta.^3)/beta.^5);
            Displacement_Fall_Poly(curve).J = y * (60/beta.^3 - (360*theta)/beta.^4 + (360*theta.^2)/beta.^5);
            disp('3,4,5 Poly');
        case 2  %4,5,6,7 Poly
            theta = linspace(0,beta);
            Displacement_Fall_Poly(curve).theta = theta;
            Displacement_Fall_Poly(curve).S = y * ((35*theta.^4)/beta.^4 - (84*theta.^5)/beta.^5 + (70*theta.^6)/beta.^6 - (20*theta.^7)/beta.^7);
            Displacement_Fall_Poly(curve).V = y*((140*theta.^3)/beta.^4 - (420*theta.^4)/beta.^5 + (420*theta.^5)/beta.^6 - (140*theta.^6)/beta.^7);
            Displacement_Fall_Poly(curve).A = y*((420*theta.^2)/beta.^4 - (1680*theta.^3)/beta.^5 + (2100*theta.^4)/beta.^6 - (840*theta.^5)/beta.^7);
            Displacement_Fall_Poly(curve).J = y*((840*theta)/beta.^4 - (5040*theta.^2)/beta.^5 + (8400*theta.^3)/beta.^6 - (4200*theta.^4)/beta.^7);
            disp('4,5,6,7 Poly');
    end
end
end