function y = kosc(n)
% symulacja wielokrotnego rzutu kością
x = rand(1,n);
A_1 = x<(1/6);
A2 = (x>(1/6)) & (x<(2/6));
A3 = (x>(2/6)) & (x<(3/6));
A4 = (x>(3/6)) & (x<(4/6));
A5 = (x>(4/6)) & (x<(5/6));
A6 = (x>(5/6));
y = A_1 + 2* A2 + 3*A3 + 4*A4 + 5*A5 + 6*A6;
mean(y)
var(y)
%histogram(y, 'Normalization','probability')
ecdf(y)
end
