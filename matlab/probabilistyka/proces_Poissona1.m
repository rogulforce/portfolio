function y=proces_Poissona1(lambda,T,n)
t=-log(rand)/lambda;
t_i=0:T/n:T;
y=zeros(1,n+1);
while t<T
    y=y+(t_i>t);
    t=t-log(rand)/lambda;
end
end