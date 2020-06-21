%%
%Author: Sai Ajjarapu
%Spring 2019

function [s33,v33,a33,j33,theta33] = Dwell(x,startbeta,endbeta)

theta33 = linspace(startbeta,endbeta);
s33 = x * ones(1,100);
v33 = zeros(1,100);
a33 = zeros(1,100);
j33 = zeros(1,100);

end