%autor: Piotr Rogula
%nazwa: puchar do picia wina
%przeznaczenie:  picie wina czerwonego wytrawnego
%zalety:
%. szeroka podstawa pozwala zachowaæ odpowiedni¹ stabilnoœæ
%. d³ugi,gruby trzon pozwala na zrêczne trzymanie pucharu, bez obaw o jego
%zniszczenie przy konserwacji
%. elipsoidalny kwiat pucharu daje du¿¹ objêtoœæ
%. zwê¿ona koñcowa czêœæ kwiata pozwala na natê¿enie zapachu wina,
%pozwalaj¹c knsumentowi na dog³êbniejsze odczuwanie smaku trunku
%zapach jest integraln¹ czêœci¹ picia wina, dlatego te¿ tak wa¿ne jest
%delikatne zwê¿enie kwiata pucharu (intensywne zwiêkszenie przeszkadza w praktycznej czêœci próbowania trunku)


zasieg3 = linspace(pi/6,3*pi/4,30);
x=linspace(0,2,10);
K1 = 1.1-(x.^2)/4;              %y=1.1-(x.^2)/4
K2 = sin(zasieg3);              %y=sin(x) D:[pi/6,3*pi/4]
K3 = ones(1,25)./10;            %y=0.1
K4 = [0.1:0.1:0.5];             %y=0.1x-3.3
razem=[K1,K3,K4,K2];
[x,y,z]=cylinder(razem);

%liczê objêtoœæ naczynia tylko dla K4 i K2 bo tylko one maj¹ za zadanie
%przechowywaæ ciecz
W4=@(k) 0.1*k-3.3;
syms k
f4= diff(0.1*k-3.3);   %pochodna
W4_2=@(k)(0.1*k-3.3)*sqrt(1+1/10.^2);

V4=abs(2*pi*integral(W4,34,38));        %objetosc
P4 = abs(2*pi*integral(W4_2,34,38));    %pole powierzchni

W2=@(k) sin(k);
f2=diff(sin(k));
W2_2=@(k)(sin(k)).*sqrt(1+(cos(k)).^2);
V2=abs(2*pi*integral(W2,pi/6,3*pi/4));
P2 = abs(2*pi*integral(W2_2,pi/6,3*pi/4));
Vc=V4+V2;

P3 = (0.1).^2*pi*25;
Pc=P4+P2+P3;
W1=@(k)1.1-(k.^2)/4;
W1_2=@(k)(1.1-(k.^2)/4).*sqrt(1+(k/4).^2);
P1=abs(2*pi*integral(W1_2,0,2));
opis=sprintf('V= %f[j^3],Pp= %f[j^2]',Vc,Pc);


%naczynie
subplot(1,2,1)     
surf(x,y,z);
axis square
xlabel('x')
ylabel('y')

title(opis)
%wykres
subplot(1,2,2)
plot(1:10,K1)
hold on
plot(10:34,K3)
hold on
plot(34:38,K4)
hold on
plot(38:67,K2)
hold on
axis square
xlabel('x')
ylabel('y')
title('wykres')
hold off
legend('1.1-(x^2)/4','0.1','0.1x-3.3','sin(x)')

