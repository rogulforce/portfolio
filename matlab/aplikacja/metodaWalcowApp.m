function V = metodaWalcowApp(fun,przedzial,n,screen)
    %funkcja ta oblicza metod� walc�w obj�to�� bry�y obrotowej powsta�ej przez obr�t
    %funkcji fun wok� osi oX na podanym przedziale. Rysuje na podanym wykresie(screen)
    %n-walc�w powsta�ych przez metod� walc�w na podanym przedziale.
    %ca�kuj�c bry�e obrotow� funkcji(fun).
    punkty = [];
    lPrzedzial = przedzial(2)-przedzial(1);     %d�ugo�� podanego przedzia�u
    odlegloscWezly = lPrzedzial/(n);            %odleg�o�� w jakiej musz� by� pomi�dzy sob� w�z�y
    for i = [1:n]
        punkty = [punkty przedzial(1)+odlegloscWezly/2+odlegloscWezly*(i-1)];    %dodaje na ko�cu kolejny w�ze�
        %odlegloscWezly/2+odlegloscWezly*(i-1) stworzy pierwszy w�z� w odleg�o�ci po�owy w�z�a
        %a nast�pne w odleg�o�ci pomiedzy w�z�ami nast�pne wzgl�dem poprzedniego
    end
    Ry = [];
    for i = punkty
        R = abs(fun(i));
        Ry = [Ry R];%dopisuje warto�ci podanej funkcji w wyznaczonych w�z��ch
    end
    
    t = linspace(przedzial(1),przedzial(2),1000);%do cylindra
    %wiele punkt�w na tej linii jest potrzebnych aby nie by�o wida� pochy�ych,
    %kt�re mog� si� pojawi� pomi�dzy kolejnymi punktami na linii, nale��cymi do 
    %2 r�nych w�z��w (aby odleg�o�� ta by�a ma�a i niezauwa�alna)
    
    R = convertToR(t,Ry,punkty,odlegloscWezly/2);%funkcja ta zwraca list� warto�ci jakiej
    %powinny mie� kolejne punkty tak aby by�y walcami
    
    [x, y, z] = cylinder(R);%obr�t powsta�ych R-�w wok� osi
    
    surf(screen,z,x,y);%narysowanie powsta�ej bry�y na wykresie
    
    V = VWalca(Ry,odlegloscWezly);%obliczenie obj�to�ci poszczeg�lnych walc�w
    V = sum(V);%zsumowanie obj�to�ci wszystkich walc�w
    
end