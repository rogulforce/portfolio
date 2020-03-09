function y=ruletka(n,m,x) 
%funkcja ruletka(n, m, x) zwraca œredni wynik gracza s
%po n grach przy za³o¿eniu, ¿e przychodzi³ do kasyna m razy 
%(za ka¿dym razem u¿ywaj¹c tej samej strategii)
%jest to ruletka europejska - 37 pól: 18 czarnych, 18 czerwonych i jedno
%neutralne. Gracz podwaja obstawion¹ sumê x jeœli kula zatrzyma siê na jego
%kolorze, w przeciwnym wypadku traci tê sumê
%
%funkcja rysuje te¿ wykres bilansu po ka¿dej z n gier dla ka¿dego z m dni
%
%przyk³adowo: ruletka(5,10,15) zwraca œredni wynik gracza, który przyszed³
%do kasyna 10 razy i 5 razy obstawi³ 15pln na czerwone pola oraz rysuje 10
%wykresów bilansu od ka¿dej z 5 gier rozegranych danego dnia
%
%autor: Piotr Rogula
if n <= 0 || m <= 0 || n~=round(n) || m ~=round(m)
   y=[];
   disp('B³¹d! n i m powinny byæ liczbami naturalnymi.')
   %imo lepsze jest 'disp' zamiast 'error' ale jeœli to problem, to mo¿na
   %zamieniæ 'disp' na 'error'
else
    r=randi([1,37],m,n);
    W=(r<19);               %wygrane
    P=(r>18);               %przegrane
    A=(W-P).*x;             %macierz zysków i strat 
    D=[zeros(1,m);cumsum(A')];   %zeros ¿eby wykres siê zaczyna³ od zera
    %cumsum zeby sie po kolei sumowaly zyski i straty 
    plot((0:n),D,'o-')
    
    y=sum(sum(A));  %suma wierszy a potem kolumn z macierzy zyskow i strat
    xlabel('kolejne gry (n)')
    ylabel('bilans')
    title('wykres bilansu od gier, ka¿dy wykres to inny dzieñ')
end
end
%zrobic legende!!!
