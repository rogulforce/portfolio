
N = 20000;

x_rnd = r_beta(N);
x = linspace(min(x_rnd), max(x_rnd),1000);

subplot(2, 1, 1);
cdfplot(x_rnd);
hold on;
plot(x,betacdf(x, 2, 4),'r--','LineWidth', 3);
legend('Dystr. Empiryczna', 'Dystr. Teoretyczna');

subplot(2, 1, 2);
histogram(x_rnd, 'normalization', 'pdf');
hold on;
plot(x, betapdf(x,2,4),'r-','LineWidth', 3);
legend('Histogram', 'G�sto�� teoretyczna');

fprintf('�rednia:\n teoretyczna: %f, pr�bkowa: %f\n', 1/3, mean(x_rnd));
fprintf('Wariancja:\n georetyczna: %f, pr�bkowa: %f\n', 8/252, var(x_rnd));
