function I = metoda_trapezow(f,a,b,n)
% zlozona metoda trapezow
% f - funkcja
% a - pocz�tek przedzia�u ca�kowania
% b - koniec -||-
% n - ilo�� podzia��w

x=linspace(a,b,n);
x_1 = x(1:end-1);
x_2= x(2:end);
I=1/2*sum((f(x_1)+f(x_2)).*(x_2-x_1));