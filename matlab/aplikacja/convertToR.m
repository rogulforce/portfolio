function y = convertToR(x,Ry,punkty,odleglosc)
    %tu sie kryje wielka tajemnica jak to dzia�a (wiele zastanowienia i trudno
    %opisa�).
    %Przyk�ad jak powsta� ten wz�r.
    %Korzystamy z metody walcowej:
    %zrobili�my 4 walce na przedziale (0,4) a wi�c walce, kt�rych �rodki wysoko�ci
    %znajduj� si� w [0.5 1.5 2.5 3.5] i to s� te nasze "punkty".
    %Mamy r�wnie� d�ugo�ci promieni tych walc�w - w kolejno�ci niech b�dzie, �e
    %r�wnaj� si� [1 2 3 4].
    %Otrzymali�my wiele punkt�w na odcinku (0,4) i chcemy im jako� przyporz�dkowa�
    %odpowienie warto�ci promieni, wok� 0.5 ma by� przyporz�dkowany promie� 1
    %wok� to znaczy w odleg�o�ci co najwy�ej 0.5 (odleg�o�ci pomi�dzy w�z�ami)
    %jako, �e je�eli co� znajduje si� w tej maksymalnej odleg�o�ci to wpada w 2
    %otoczenia to uznajemy, �e wpada do tego nast�pnego.
    %za��my, �e otrzymali�my tak jak w zadaniu list� x, kt�re s� rownorozmieszczone
    %na przedziale [0,4]. Dla u�atwienia przyk�adu za��my, �e otrzymali�my list�
    %x = [0 0.25 0.5 0.75 ... 4] ( w rzeczywisto�ci b�dzie to lista d�u�sza ale ta i tak
    %jest d�u�sza ni� liczba w�z��w co stwarza problem)
    %teraz (x' > punkty - odleglosc).*(x' <= punkty + odleglosc) (czyli tak naprawd�
    %dla macierzy logicznych mno�enie jest koniunkcj�) zwr�ci nam macierz logiczn� 
    %wygl�daj�ca nast�puj�co:
    %gdyby�my nie dali x' a x nie wysz�o by tak �adnie a zwr�ci�o by b��d.
    %[0 0 0 0
    % 1 0 0 0
    % 1 0 0 0
    % 0 1 0 0
    % 0 1 0 0
    % 0 0 1 0
    % 0 0 1 0
    % 0 0 0 1
    % 0 0 0 1]
    %Jak nale�y j� interpretowa�?
    %Je�eli b�dziemy mieli drugi z wektor�w z x to wtedy patrzymy na drugi wiersz
    %tam gdzie jest jedynka tam jest miejsce na kt�rym znajduje si� w li�cie promieni
    %promie�, kt�ry ma odpowiada� temu punktowi. Analogicznie dla drugiego, trzeciego
    %itd.
    %Teraz pomno�ymy t� macierz przez macierz maj�c� promienie w spos�b pokazany we wzorze.
    %Otrzymamy macierz:
    %[0 0 0 0
    % 1 0 0 0
    % 1 0 0 0
    % 0 2 0 0
    % 0 2 0 0
    % 0 0 3 0
    % 0 0 3 0
    % 0 0 0 4
    % 0 0 0 4]
    %teraz po zsumowaniu wzgl�dem wzd�u� wierszy otrzymamy list� promieni jak� powinny
    %mie� poszczeg�lne x-sy (pierwszy zawsze b�dzie mia� promie� 0 ale to wr�cz dodaje
    %efektu poniewa�, b�dziemy mieli z przodu �adne "zamkni�cie" walca.
    %a wi�c na ko�cu otrzymali�my list�:
    %[0  1    1   2   ... 4],
    %kt�ra odpowiada punktom
    %[0 0.25 0.5 0.75 ... 4],
    %co by�o naszym celem.
    y = sum(((x' > punkty - odleglosc).*(x' <= punkty + odleglosc)).*Ry,2); 
end
