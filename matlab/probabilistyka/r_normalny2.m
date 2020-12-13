function y = r_normalny2(mu,sigma,N)
y=ones(1,N);
for i=1:floor(N/2)
V_1 = -1+rand*2;
V_2 = -1+rand*2;
R_kw = V_1^2+V_2^2;
while R_kw>1
    V_1 = -1+rand*2;
    V_2 = -1+rand*2;
    R_kw = V_1^2+V_2^2;
end
y(i)=mu+sigma*sqrt(-2*log(R_kw)/R_kw)*V_1;
y(N+1-i)=mu+sigma*sqrt(-2*log(R_kw)/R_kw)*V_2;
% w przypadku nieparzystym przy ostatniej pêtli y(N+1-i) nadpisze y(i)
end
end