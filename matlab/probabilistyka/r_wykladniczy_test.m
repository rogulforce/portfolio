lambda = 3;
N = 10000;

x_rnd = r_wykladniczy(lambda, N);
x = linspace(min(x_rnd), max(x_rnd),1000);

subplot(2, 1, 1);
cdfplot(x_rnd);
hold on;
plot(x, 1-exp(-lambda*x));
legend('Dystr. Empiryczna', 'Dystr. Teoretyczna');

subplot(2, 1, 2);
histogram(x_rnd, 'normalization', 'pdf');
hold on;
plot(x, lambda*exp(-lambda*x));
legend('Histogram', 'Gêstoœæ teoretyczna');

fprintf('Œrednia:\n teoretyczna: %f, próbkowa: %f\n', 1/lambda, mean(x_rnd));
fprintf('Wariancja:\n teoretyczna: %f, próbkowa: %f\n', 1/lambda^2, var(x_rnd));