function y = convertToR(x,Ry,punkty,odleglosc)
    %tu sie kryje wielka tajemnica jak to dzia³a (wiele zastanowienia i trudno
    %opisaæ).
    %Przyk³ad jak powsta³ ten wzór.
    %Korzystamy z metody walcowej:
    %zrobiliœmy 4 walce na przedziale (0,4) a wiêc walce, których œrodki wysokoœci
    %znajduj¹ siê w [0.5 1.5 2.5 3.5] i to s¹ te nasze "punkty".
    %Mamy równie¿ d³ugoœci promieni tych walców - w kolejnoœci niech bêdzie, ¿e
    %równaj¹ siê [1 2 3 4].
    %Otrzymaliœmy wiele punktów na odcinku (0,4) i chcemy im jakoœ przyporz¹dkowaæ
    %odpowienie wartoœci promieni, wokó³ 0.5 ma byæ przyporz¹dkowany promieñ 1
    %wokó³ to znaczy w odleg³oœci co najwy¿ej 0.5 (odleg³oœci pomiêdzy wêz³ami)
    %jako, ¿e je¿eli coœ znajduje siê w tej maksymalnej odleg³oœci to wpada w 2
    %otoczenia to uznajemy, ¿e wpada do tego nastêpnego.
    %za³ó¿my, ¿e otrzymaliœmy tak jak w zadaniu listê x, które s¹ rownorozmieszczone
    %na przedziale [0,4]. Dla u³atwienia przyk³adu za³ó¿my, ¿e otrzymaliœmy listê
    %x = [0 0.25 0.5 0.75 ... 4] ( w rzeczywistoœci bêdzie to lista d³u¿sza ale ta i tak
    %jest d³u¿sza ni¿ liczba wêz³ów co stwarza problem)
    %teraz (x' > punkty - odleglosc).*(x' <= punkty + odleglosc) (czyli tak naprawdê
    %dla macierzy logicznych mno¿enie jest koniunkcj¹) zwróci nam macierz logiczn¹ 
    %wygl¹daj¹ca nastêpuj¹co:
    %gdybyœmy nie dali x' a x nie wysz³o by tak ³adnie a zwróci³o by b³¹d.
    %[0 0 0 0
    % 1 0 0 0
    % 1 0 0 0
    % 0 1 0 0
    % 0 1 0 0
    % 0 0 1 0
    % 0 0 1 0
    % 0 0 0 1
    % 0 0 0 1]
    %Jak nale¿y j¹ interpretowaæ?
    %Je¿eli bêdziemy mieli drugi z wektorów z x to wtedy patrzymy na drugi wiersz
    %tam gdzie jest jedynka tam jest miejsce na którym znajduje siê w liœcie promieni
    %promieñ, który ma odpowiadaæ temu punktowi. Analogicznie dla drugiego, trzeciego
    %itd.
    %Teraz pomno¿ymy tê macierz przez macierz maj¹c¹ promienie w sposób pokazany we wzorze.
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
    %teraz po zsumowaniu wzglêdem wzd³u¿ wierszy otrzymamy listê promieni jak¹ powinny
    %mieæ poszczególne x-sy (pierwszy zawsze bêdzie mia³ promieñ 0 ale to wrêcz dodaje
    %efektu poniewa¿, bêdziemy mieli z przodu ³adne "zamkniêcie" walca.
    %a wiêc na koñcu otrzymaliœmy listê:
    %[0  1    1   2   ... 4],
    %która odpowiada punktom
    %[0 0.25 0.5 0.75 ... 4],
    %co by³o naszym celem.
    y = sum(((x' > punkty - odleglosc).*(x' <= punkty + odleglosc)).*Ry,2); 
end
