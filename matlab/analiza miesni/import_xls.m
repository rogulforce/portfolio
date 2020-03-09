%wczytany plik w formacie xls

%input nazwy pliku 
% dozwolone nazwy:
% 'dane1.xls'
% 'dane2.xls'
% 'dane3.xls'
% 'dane4.xls'
% 'dane5.xls'
% 'dane6.xls'
plik_xls='dane3.xls';

X = xlsread(plik_xls);
% matlab sam omija kom�rki, w kt�rych jest tekst
X = X(1:end-3,:);
%wyrzucenie reszty offsetu (d�)
time = X(end,1);
disp("czas trwania badania: "+time)
%liczymy rns dla ka�dego mi�nia
M = mean(X);
disp("warto�� RMS dla bicepsa [uV]: "+M(2))
disp("warto�� RMS dla g�owy przy�rodkowej tricepsa [uV]: "+M(3))
disp("warto�� RMS dla g�owy d�ugiej tricepsa [uV]: "+M(4))
disp("warto�� RMS dla g�owy bocznej tricepsa [uV]: "+M(5))
subplot(2,2,1)
plot(X(:,1),X(:,2));
title('Biceps')
subplot(2,2,2)
plot(X(:,1),X(:,3))
title('G�owa Przy�rodkowa Tricepsa')
subplot(2,2,3)
plot(X(:,1),X(:,4))
title('G�owa D�uga Tricepsa')
subplot(2,2,4)
plot(X(:,1),X(:,5))
title('G�owa Boczna Tricepsa')