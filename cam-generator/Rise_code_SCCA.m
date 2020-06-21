%%
%Author: Sai Ajjarapu
%Spring 2019

function [Displacement_Rise_SCCA] = Rise_code_SCCA(beta,h)
Displacement_Rise_SCCA = struct();
for curve = 1:5
    %% Selecting the curve and calculating the equations
    switch(curve)
        case 1 %Constant Acceleration
            b = 0; c = 1; d = 0; Ca = 4; disp('Constant Acceleration');
        case 2 % Modified Trapezoidal
            b = 0.25; c = 0.50; d = 0.25; Ca = 4.8881; disp('Modified Trapezoidal');
        case 3 %Modified Sine
            b = 0.25; c = 0; d = 0.75; Ca = 5.5280; disp('Modified Sine');
        case 4 %Harmonic Displacement
            b = 0; c = 0; d = 1; Ca = 4.9348; disp('Harmonic Displacement');
        case 5 %Cyclodial displacement
            b = 0.50; c = 0; d = 0.50; Ca = 6.2832; disp('Cyclodial displacement');
    end
    
    x1 = linspace(0,(b/2));
    x2 = linspace((b/2),((1-d)/2));
    x3 = linspace(((1-d)/2),((1+d)/2));
    x4 = linspace(((1+d)/2),(1-(b/2)));
    x5 = linspace((1-(b/2)),1);
    
    s1 = (((b/pi)*x1)-...
        ((b/pi).^2)*sin((pi/b)*x1));
    s2 = ((x2.^2/2)+...
        (b*((1/pi)-0.5)*x2)+...
        (b.^2*(0.125-(1/(pi.^2)))));
    s3 = ((((b/pi)+(c/2))*x3)+...
        ((d/pi).^2)+...
        (b.^2*(0.125-(1/pi.^2)))-...
        (((1-d).^2)/8)-...
        (((d/pi).^2)*(cos((pi/d)*(x3-((1-d)/2))))));
    s4 = ((-x4.^2/2)+...
        (((b/pi)+1-(b/2))*x4)+...
        ((2*d.^2-b.^2)*(((1/pi.^2)-0.125))-0.25));
    s5 = (((b/pi)*x5)+...
        ((2*(d.^2-b.^2))/(pi.^2))+...
        (((1-b).^2-d.^2)/4)-...
        ((b/pi).^2)*sin((pi/b)*(x5-1)));
    
    v1 = (b/pi) - ((b/pi) * cos((pi/b)*x1));
    v2 = x2 + (b*((1/pi)-0.5));
    v3 = (b/pi) + (c/2) + ((d/pi)*sin((pi/d) * (x3 - ((1-d)/2))));
    v4 = -x4 + (b/pi) + 1 - (b/2);
    v5 = (b/pi) - ((b/pi) * cos((pi/b)*(x5-1)));
    
    a1 = sin((pi/b)*x1);
    a2 = 1;
    a3 = cos((pi/d) * (x3 - ((1-d)/2)));
    a4 = -1;
    a5 = sin((pi/b) * (x5-1));
    
    j1 = (pi/b) * cos( (pi/b) * x1);
    j2 = 0;
    j3 = -((pi/d) * sin((pi/d) * (x3 - ((1-d)/2))));
    j4 = 0;
    j5 = (pi/b) * cos((pi/b) * (x5-1));
    
    %Error cases
    if (curve == 1) %constant accel
        Displacement_Rise_SCCA(curve).theta = beta * [ x2 x4 ];
        Displacement_Rise_SCCA(curve).S = Ca * h * [ s2 s4 ];
        Displacement_Rise_SCCA(curve).V = Ca * h * [ v2 v4 ];
        Displacement_Rise_SCCA(curve).A = Ca * h * [(ones(1,100)*a2) (ones(1,100)*a4)];
        Displacement_Rise_SCCA(curve).J = Ca * h * [(zeros(1,100)*j2) (zeros(1,100)*j4) ];
    elseif (curve == 3) %Simple Harmonic
        Displacement_Rise_SCCA(curve).theta = beta * [ x2 x3 x4 ];
        Displacement_Rise_SCCA(curve).S = Ca * h * [ s2 s3 s4 ];
        Displacement_Rise_SCCA(curve).V = Ca * h * [ v2 v3 v4 ];
        Displacement_Rise_SCCA(curve).A = Ca * h * [(ones(1,100)*a2) a3 (ones(1,100)*a4)];
        Displacement_Rise_SCCA(curve).J = Ca * h * [(zeros(1,100)*j2) j3 (zeros(1,100)*j4)];
    elseif (curve == 2 || curve == 4 || curve == 5) %Modified Trapezoidal or Modified Sine or Cyclodial Displacement
        Displacement_Rise_SCCA(curve).theta = beta * [x1 x2 x3 x4 x5];
        Displacement_Rise_SCCA(curve).S = Ca * h * [s1 s2 s3 s4 s5];
        Displacement_Rise_SCCA(curve).V = Ca * h * [v1 v2 v3 v4 v5];
        Displacement_Rise_SCCA(curve).A = Ca * h * [a1 (ones(1,100)*a2) a3 (ones(1,100)*a4) a5];
        Displacement_Rise_SCCA(curve).J = Ca * h * [j1 (zeros(1,100)*j2) j3 (zeros(1,100)*j4) j5];       
    end
end