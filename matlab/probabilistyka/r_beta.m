function y=r_beta(N)
m = 135/64; % m = 135/64 dla x=1/4
y = zeros(1,N);
f = @(x) 20*x*(1-x)^3;
for i=1:N
    U = rand;
    while f(U) < rand*m
        U = rand;
    end
    y(i) = U;
end
end
