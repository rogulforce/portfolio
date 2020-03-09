function y=ruletka(n,m,x) 
%funkcja ruletka(n, m, x) zwraca �redni wynik gracza s
%po n grach przy za�o�eniu, �e przychodzi� do kasyna m razy 
%(za ka�dym razem u�ywaj�c tej samej strategii)
%jest to ruletka europejska - 37 p�l: 18 czarnych, 18 czerwonych i jedno
%neutralne. Gracz podwaja obstawion� sum� x je�li kula zatrzyma si� na jego
%kolorze, w przeciwnym wypadku traci t� sum�
%
%funkcja rysuje te� wykres bilansu po ka�dej z n gier dla ka�dego z m dni
%
%przyk�adowo: ruletka(5,10,15) zwraca �redni wynik gracza, kt�ry przyszed�
%do kasyna 10 razy i 5 razy obstawi� 15pln na czerwone pola oraz rysuje 10
%wykres�w bilansu od ka�dej z 5 gier rozegranych danego dnia
%
%autor: Piotr Rogula
if n <= 0 || m <= 0 || n~=round(n) || m ~=round(m)
   y=[];
   disp('B��d! n i m powinny by� liczbami naturalnymi.')
   %imo lepsze jest 'disp' zamiast 'error' ale je�li to problem, to mo�na
   %zamieni� 'disp' na 'error'
else
    r=randi([1,37],m,n);
    W=(r<19);               %wygrane
    P=(r>18);               %przegrane
    A=(W-P).*x;             %macierz zysk�w i strat 
    D=[zeros(1,m);cumsum(A')];   %zeros �eby wykres si� zaczyna� od zera
    %cumsum zeby sie po kolei sumowaly zyski i straty 
    plot((0:n),D,'o-')
    
    y=sum(sum(A));  %suma wierszy a potem kolumn z macierzy zyskow i strat
    xlabel('kolejne gry (n)')
    ylabel('bilans')
    title('wykres bilansu od gier, ka�dy wykres to inny dzie�')
end
end
%zrobic legende!!!
