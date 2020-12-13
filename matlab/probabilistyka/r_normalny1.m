function y = r_normalny1(mu,sigma,N)
% ceil i floor dla przypadku gdy mod(N,2) = 1
%  X= mu*ones(1,ceil(N/2))+sigma*sqrt(-2*log(rand(1,ceil(N/2)))).*cos(2*pi*rand(1,ceil(N/2)));
%  Y= mu*ones(1,floor(N/2))+sigma*sqrt(-2*log(rand(1,floor(N/2)))).*sin(2*pi*rand(1,floor(N/2)));
%  y=[X,Y];
y = [mu*ones(1,ceil(N/2))+sigma*sqrt(-2*log(rand(1,ceil(N/2)))).*cos(2*pi*rand(1,ceil(N/2))),mu*ones(1,floor(N/2))+sigma*sqrt(-2*log(rand(1,floor(N/2)))).*sin(2*pi*rand(1,floor(N/2)))];
end
