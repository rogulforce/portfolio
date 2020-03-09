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
% matlab sam omija komórki, w których jest tekst
X = X(1:end-3,:);
%wyrzucenie reszty offsetu (dó³)
time = X(end,1);
disp("czas trwania badania: "+time)
%liczymy rns dla ka¿dego miêœnia
M = mean(X);
disp("wartoœæ RMS dla bicepsa [uV]: "+M(2))
disp("wartoœæ RMS dla g³owy przyœrodkowej tricepsa [uV]: "+M(3))
disp("wartoœæ RMS dla g³owy d³ugiej tricepsa [uV]: "+M(4))
disp("wartoœæ RMS dla g³owy bocznej tricepsa [uV]: "+M(5))
subplot(2,2,1)
plot(X(:,1),X(:,2));
title('Biceps')
subplot(2,2,2)
plot(X(:,1),X(:,3))
title('G³owa Przyœrodkowa Tricepsa')
subplot(2,2,3)
plot(X(:,1),X(:,4))
title('G³owa D³uga Tricepsa')
subplot(2,2,4)
plot(X(:,1),X(:,5))
title('G³owa Boczna Tricepsa')