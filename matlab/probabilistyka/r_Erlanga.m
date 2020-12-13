function y = r_Erlanga(n,lambda,N)
% tworzymy n x N realizacji rozkladu wykladniczego i sumujemy
y = sum(-log(rand(n, N))/lambda);
end