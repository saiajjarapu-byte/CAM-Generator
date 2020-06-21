%%
%Author: Sai Ajjarapu
%Spring 2019

%Functions that are used:
%Rise_code_SCCA.m
%Fall_code_SCCA.m
%Rise_code_Poly.m
%Fall_code_Poly.m
%Dwell.m
%Dwell_Fall.m
%% Input Data
clear;clc;
disp('I HATE MY LIFE');
disp('The Trapezoidal curve derivation is beyond me');
disp('Rise Data Input');
h = 2; %input('Max Throw = ');
beta = 45; %input('Beta = ');
beta = deg2rad(beta);
%Dwell at rise
disp('Dwell Rise Data Input');
startbeta = 45; %input('Start beta = ');
startbeta = deg2rad(startbeta);
endbeta = 122; %input('End beta = ');
endbeta = deg2rad(endbeta);
x = 2; %input('Dwell distance = ');
%Fall
disp('Fall Data Input');
beta1 = 122; %input('Start beta = ');
beta1 = deg2rad(beta1);
beta2 = 270; %input('End beta = ');
beta2 = deg2rad(beta2);
y = 2; %input('Fall Distance = ');
%Dwell at Fall
disp('Dwell at Fall');
start_beta = 270; %input('Start Beta = ');
start_beta = deg2rad(start_beta);
end_beta = 360; %input('End Beta = ');
end_beta = deg2rad(end_beta);
base = 3; %input('Base circle = ');
%% Function Calls
[Displacement_Rise_SCCA] = Rise_code_SCCA(beta,h); %Rise SCCA
[Displacement_Rise_Poly] = Rise_code_Poly(beta,h); %Rise Poly
[d3,v3,a3,j3,t33] = Dwell(x,startbeta,endbeta); %Dwell after Rise
[Displacement_Fall_SCCA] = Fall_code_SCCA(beta1,beta2,y); %Fall SCCA
[Displacement_Fall_Poly] = Fall_code_Poly(beta1,beta2,y); %Fall Poly
[d4,v4,a4,j4,t43] = Dwell_Fall(start_beta,end_beta); %Fall Dwell
%Constant Acceleration
S1_Rise = Displacement_Rise_SCCA(1).S;
V1_Rise = Displacement_Rise_SCCA(1).V;
A1_Rise = Displacement_Rise_SCCA(1).A;
J1_Rise = Displacement_Rise_SCCA(1).J;
T1_Rise = Displacement_Rise_SCCA(1).theta;
%Mod Trapezoidal
S2_Rise = Displacement_Rise_SCCA(2).S;
V2_Rise = Displacement_Rise_SCCA(2).V;
A2_Rise = Displacement_Rise_SCCA(2).A;
J2_Rise = Displacement_Rise_SCCA(2).J;
T2_Rise = Displacement_Rise_SCCA(2).theta;
%Mod Sine
S3_Rise = Displacement_Rise_SCCA(3).S;
V3_Rise = Displacement_Rise_SCCA(3).V;
A3_Rise = Displacement_Rise_SCCA(3).A;
J3_Rise = Displacement_Rise_SCCA(3).J;
T3_Rise = Displacement_Rise_SCCA(3).theta;
%Harmonic Displacement
S4_Rise = Displacement_Rise_SCCA(4).S;
V4_Rise = Displacement_Rise_SCCA(4).V;
A4_Rise = Displacement_Rise_SCCA(4).A;
J4_Rise = Displacement_Rise_SCCA(4).J;
T4_Rise = Displacement_Rise_SCCA(4).theta;
%Cyclodial Displacement
S5_Rise = Displacement_Rise_SCCA(5).S;
V5_Rise = Displacement_Rise_SCCA(5).V;
A5_Rise = Displacement_Rise_SCCA(5).A;
J5_Rise = Displacement_Rise_SCCA(5).J;
T5_Rise = Displacement_Rise_SCCA(5).theta;
%3,4,5 Poly
S6_Rise = Displacement_Rise_Poly(1).S;
V6_Rise = Displacement_Rise_Poly(1).V;
A6_Rise = Displacement_Rise_Poly(1).A;
J6_Rise = Displacement_Rise_Poly(1).J;
T6_Rise = Displacement_Rise_Poly(1).theta;
%4,5,6,7 Poly
S7_Rise = Displacement_Rise_Poly(2).S;
V7_Rise = Displacement_Rise_Poly(2).V;
A7_Rise = Displacement_Rise_Poly(2).A;
J7_Rise = Displacement_Rise_Poly(2).J;
T7_Rise = Displacement_Rise_Poly(2).theta;
%% Fall Function calls
%Constant Acceleration
S1_Fall = Displacement_Fall_SCCA(1).S;
S1_Fall = flip(S1_Fall);
V1_Fall = Displacement_Fall_SCCA(1).V;
V1_Fall = -(V1_Fall);
A1_Fall = Displacement_Fall_SCCA(1).A;
A1_Fall = -(A1_Fall);
J1_Fall = Displacement_Fall_SCCA(1).J;
J1_Fall = -(J1_Fall);
T1_Fall = Displacement_Fall_SCCA(1).theta;
T1_Fall = T1_Fall + beta1;
%Mod Trapezoidal
S2_Fall = Displacement_Fall_SCCA(2).S;
S2_Fall = flip(S2_Fall);
V2_Fall = Displacement_Fall_SCCA(2).V;
V2_Fall = -(V2_Fall);
A2_Fall = Displacement_Fall_SCCA(2).A;
A2_Fall = -(A2_Fall);
J2_Fall = Displacement_Fall_SCCA(2).J;
J2_Fall = -(J2_Fall);
T2_Fall = Displacement_Fall_SCCA(2).theta;
T2_Fall = T2_Fall + beta1;
%Mod Sine
S3_Fall = Displacement_Fall_SCCA(3).S;
S3_Fall = flip(S3_Fall);
V3_Fall = Displacement_Fall_SCCA(3).V;
V3_Fall = -(V3_Fall);
A3_Fall = Displacement_Fall_SCCA(3).A;
A3_Fall = -(A3_Fall);
J3_Fall = Displacement_Fall_SCCA(3).J;
J3_Fall = -(J3_Fall);
T3_Fall = Displacement_Fall_SCCA(3).theta;
T3_Fall = T3_Fall + beta1;
%Harmonic Displacement
S4_Fall = Displacement_Fall_SCCA(4).S;
S4_Fall = flip(S4_Fall);
V4_Fall = Displacement_Fall_SCCA(4).V;
V4_Fall = -(V4_Fall);
A4_Fall = Displacement_Fall_SCCA(4).A;
A4_Fall = -(A4_Fall);
J4_Fall = Displacement_Fall_SCCA(4).J;
J4_Fall = -(J4_Fall);
T4_Fall = Displacement_Fall_SCCA(4).theta;
T4_Fall = T4_Fall + beta1;
%Cyclodial Displacement
S5_Fall = Displacement_Fall_SCCA(5).S;
S5_Fall = flip(S5_Fall);
V5_Fall = Displacement_Fall_SCCA(5).V;
V5_Fall = -(V5_Fall);
A5_Fall = Displacement_Fall_SCCA(5).A;
A5_Fall = -(A5_Fall);
J5_Fall = Displacement_Fall_SCCA(5).J;
J5_Fall = -(J5_Fall);
T5_Fall = Displacement_Fall_SCCA(5).theta;
T5_Fall = T5_Fall + beta1;
% %3,4,5 Poly
S6_Fall = Displacement_Fall_Poly(1).S;
S6_Fall = flip(S6_Fall);
V6_Fall = Displacement_Fall_Poly(1).V;
V6_Fall = -(V6_Fall);
A6_Fall = Displacement_Fall_Poly(1).A;
A6_Fall = -(A6_Fall);
J6_Fall = Displacement_Fall_Poly(1).J;
J6_Fall = -(J6_Fall);
T6_Fall = Displacement_Fall_Poly(1).theta;
T6_Fall = T6_Fall + beta1;
% %4,5,6,7 Poly
S7_Fall = Displacement_Fall_Poly(2).S;
S7_Fall = flip(S7_Fall);
V7_Fall = Displacement_Fall_Poly(2).V;
V7_Fall = -(V7_Fall);
A7_Fall = Displacement_Fall_Poly(2).A;
A7_Fall = -(A7_Fall);
J7_Fall = Displacement_Fall_Poly(2).J;
J7_Fall = -(J7_Fall);
T7_Fall = Displacement_Fall_Poly(2).theta;
T7_Fall = T7_Fall + beta1;
%% CAM Profile computation
constant_accel = [S1_Rise d3 S1_Fall d4];
theta1 = [T1_Rise t33 T1_Fall t43];
mod_trap = [S2_Rise d3 S2_Fall d4];
theta2 = [T2_Rise t33 T2_Fall t43];
mod_sine = [S3_Rise d3 S3_Fall d4];
theta3 = [T3_Rise t33 T3_Fall t43];
harm_disp = [S4_Rise d3 S4_Fall d4];
theta4 = [T4_Rise t33 T4_Fall t43];
cyc_disp = [S5_Rise d3 S5_Fall d4];
theta5 = [T5_Rise t33 T5_Fall t43];
poly_345 = [S6_Rise d3 S6_Fall d4];
theta6 = [T6_Rise t33 T6_Fall t43];
poly_4567 = [S7_Rise d3 S7_Fall d4];
theta7 = [T7_Rise t33 T7_Fall t43];
%% Plot the SVAJ graphs
figure(1)
plot(rad2deg(T1_Rise),S1_Rise,rad2deg(T2_Rise),S2_Rise,rad2deg(T3_Rise),S3_Rise,rad2deg(T4_Rise),S4_Rise,...
    rad2deg(T5_Rise),S5_Rise,rad2deg(T6_Rise),S6_Rise,rad2deg(T7_Rise),S7_Rise);%rise plot
title('Displacement');
hold on;
plot(rad2deg(t33),d3);%dwell at rise
plot(rad2deg(T1_Fall),S1_Fall,rad2deg(T2_Fall),S2_Fall,rad2deg(T3_Fall),S3_Fall,rad2deg(T4_Fall),S4_Fall,...
    rad2deg(T5_Fall),S5_Fall,rad2deg(T6_Fall),S6_Fall,rad2deg(T7_Fall),S7_Fall);%fall
plot(rad2deg(t43),d4);%dwell at fall
legend('Constant Acceleration','Modified Trapezoid','Modified Sine',...
    'Harmonic displacement','Cyclodial displacement','3,4,5 Poly','4,5,6,7 Poly');

figure(2)
plot(rad2deg(T1_Rise),V1_Rise,rad2deg(T2_Rise),V2_Rise,rad2deg(T3_Rise),V3_Rise,rad2deg(T4_Rise),V4_Rise,...
    rad2deg(T5_Rise),V5_Rise,rad2deg(T6_Rise),V6_Rise,rad2deg(T7_Rise),V7_Rise);%rise plot
title('Velocity');
hold on;
plot(rad2deg(t33),v3);%dwell at rise
plot(rad2deg(T1_Fall),V1_Fall,rad2deg(T2_Fall),V2_Fall,rad2deg(T3_Fall),V3_Fall,rad2deg(T4_Fall),V4_Fall,...
    rad2deg(T5_Fall),V5_Fall,rad2deg(T6_Fall),V6_Fall,rad2deg(T6_Fall),V7_Fall);%fall
plot(rad2deg(t43),d4);%dwell at fall
legend('Constant Acceleration','Modified Trapezoid','Modified Sine',...
    'Harmonic displacement','Cyclodial displacement','3,4,5 Poly','4,5,6,7 Poly');

figure(3)
plot(rad2deg(T1_Rise),A1_Rise,rad2deg(T2_Rise),A2_Rise,rad2deg(T3_Rise),A3_Rise,rad2deg(T4_Rise),A4_Rise,...
    rad2deg(T5_Rise),A5_Rise,rad2deg(T6_Rise),A6_Rise,rad2deg(T7_Rise),A7_Rise);%rise plot
title('Acceleration');
hold on;
plot(rad2deg(t33),v3);%dwell at rise
plot(rad2deg(T1_Fall),A1_Fall,rad2deg(T2_Fall),A2_Fall,rad2deg(T3_Fall),A3_Fall,rad2deg(T4_Fall),A4_Fall,...
    rad2deg(T5_Fall),A5_Fall,rad2deg(T6_Fall),A6_Fall,rad2deg(T7_Fall),A7_Fall);%fall
plot(rad2deg(t43),d4);%dwell at fall
legend('Constant Acceleration','Modified Trapezoid','Modified Sine',...
    'Harmonic displacement','Cyclodial displacement','3,4,5 Poly','4,5,6,7 Poly');

figure(4)
plot(rad2deg(T1_Rise),J1_Rise,rad2deg(T2_Rise),J2_Rise,rad2deg(T3_Rise),J3_Rise,rad2deg(T4_Rise),J4_Rise,...
    rad2deg(T5_Rise),J5_Rise,rad2deg(T6_Rise),J6_Rise,rad2deg(T7_Rise),J7_Rise);%rise plot
title('Jerk');
hold on;
plot(rad2deg(t33),v3);%dwell at rise
plot(rad2deg(T1_Fall),J1_Fall,rad2deg(T2_Fall),J2_Fall,rad2deg(T3_Fall),J3_Fall,rad2deg(T4_Fall),J4_Fall,...
    rad2deg(T5_Fall),J5_Fall,rad2deg(T6_Fall),J6_Fall,rad2deg(T7_Fall),J7_Fall);%fall
plot(rad2deg(t43),d4);%dwell at fall
legend('Constant Acceleration','Modified Trapezoid','Modified Sine',...
    'Harmonic displacement','Cyclodial displacement','3,4,5 Poly','4,5,6,7 Poly');

figure(5)
polarplot(theta1,constant_accel + base);
title('Constant Acceleration');
figure(6)
polarplot(theta2,mod_trap + base);
title('Modified Trapezoidal');
figure(7)
polarplot(theta3,mod_sine + base);
title('Modified Sine');
figure(8)
polarplot(theta4,harm_disp + base);
title('Harmonic Displacement');
figure(9)
polarplot(theta5,cyc_disp + base);
title('Cycloidal Displacement');
figure(10)
polarplot(theta6,poly_345 + base);
title('3,4,5 Polynomial');
figure(11)
polarplot(theta7,poly_4567 + base);
title('4,5,6,7 Polynomial');

