mu=2;
sigma=3;
N = 10000;

x_rnd = r_normalny2(mu,sigma, N);
x = linspace(min(x_rnd), max(x_rnd),1000);

subplot(2, 1, 1);
cdfplot(x_rnd);
hold on;
plot(x, normcdf(x,mu,sigma),'r--');
legend('Dystr. Empiryczna', 'Dystr. Teoretyczna');

subplot(2, 1, 2);
histogram(x_rnd, 'normalization', 'pdf');
hold on;
plot(x, normpdf(x,mu,sigma));
legend('Histogram', 'Gêstoœæ teoretyczna');

fprintf('Œrednia:\n teoretyczna: %f, próbkowa: %f\n', mu, mean(x_rnd));
fprintf('Wariancja:\n teoretyczna: %f, próbkowa: %f\n', sigma^2, var(x_rnd));

fprintf('Wynik funkcji kstest: %4.0f\n' ,kstest(x_rnd))
