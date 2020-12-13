n = 9;
lambda = 1/2;
N = 1000;

x_rnd = r_Erlanga(n,lambda, N);
x = linspace(min(x_rnd), max(x_rnd),1000);

subplot(2, 1, 1);
cdfplot(x_rnd);
hold on;
plot(x, gamcdf(x,n,1/lambda),'r--');
legend('Dystr. Empiryczna', 'Dystr. Teoretyczna');

subplot(2, 1, 2);
histogram(x_rnd, 'normalization', 'pdf');
hold on;
plot(x, gampdf(x,n,1/lambda));
legend('Histogram', 'Gêstoœæ teoretyczna');

fprintf('Œrednia:\n teoretyczna: %f, próbkowa: %f\n', n/lambda, mean(x_rnd));
fprintf('Wariancja:\n teoretyczna: %f, próbkowa: %f\n', n/lambda^2, var(x_rnd));
