p = [0.1, 0.05, 0.1, 0.05, 0.5,0.2];
lambda = [2, 3, 4, 5, 6,7];
N = 3000;


F = @(x) 0.1*(1-exp(-2*x))+ 0.05*(1-exp(-3*x))+0.1*(1-exp(-4*x))+0.05*(1-exp(-5*x))+0.5*(1-exp(-6*x))+0.2*(1-exp(-7*x));
f =  @(x) 0.2*exp(-2*x)+0.15*exp(-3*x)+0.4*exp(-4*x)+0.25*exp(-5*x)+3*exp(-6*x)+1.4*exp(-7*x);

x_rnd = r_hiperexp(p, lambda, N);
x = linspace(min(x_rnd), max(x_rnd),1000);

subplot(2, 1, 1);
cdfplot(x_rnd);
hold on;
plot(x, F(x),'r--');
legend('Dystr. Empiryczna', 'Dystr. Teoretyczna');

subplot(2, 1, 2);
histogram(x_rnd, 'normalization', 'pdf');
hold on;
plot(x, f(x));
legend('Histogram', 'Gêstoœæ teoretyczna');

fprintf('Œrednia:\n teoretyczna: %f, próbkowa: %f\n', sum(p./lambda), mean(x_rnd));
fprintf('Wariancja:\n teoretyczna: %f, próbkowa: %f\n', sum(2*p./(lambda.^2))- (sum(p./lambda))^2, var(x_rnd));