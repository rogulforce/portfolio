function V = metodaWalcowApp(fun,przedzial,n,screen)
    %funkcja ta oblicza metod¹ walców objêtoœæ bry³y obrotowej powsta³ej przez obrót
    %funkcji fun wokó³ osi oX na podanym przedziale. Rysuje na podanym wykresie(screen)
    %n-walców powsta³ych przez metodê walców na podanym przedziale.
    %ca³kuj¹c bry³e obrotow¹ funkcji(fun).
    punkty = [];
    lPrzedzial = przedzial(2)-przedzial(1);     %d³ugoœæ podanego przedzia³u
    odlegloscWezly = lPrzedzial/(n);            %odleg³oœæ w jakiej musz¹ byæ pomiêdzy sob¹ wêz³y
    for i = [1:n]
        punkty = [punkty przedzial(1)+odlegloscWezly/2+odlegloscWezly*(i-1)];    %dodaje na koñcu kolejny wêze³
        %odlegloscWezly/2+odlegloscWezly*(i-1) stworzy pierwszy wêz³ w odleg³oœci po³owy wêz³a
        %a nastêpne w odleg³oœci pomiedzy wêz³ami nastêpne wzglêdem poprzedniego
    end
    Ry = [];
    for i = punkty
        R = abs(fun(i));
        Ry = [Ry R];%dopisuje wartoœci podanej funkcji w wyznaczonych wêz³¹ch
    end
    
    t = linspace(przedzial(1),przedzial(2),1000);%do cylindra
    %wiele punktów na tej linii jest potrzebnych aby nie by³o widaæ pochy³ych,
    %które mog¹ siê pojawiæ pomiêdzy kolejnymi punktami na linii, nale¿¹cymi do 
    %2 ró¿nych wêz³ów (aby odleg³oœæ ta by³a ma³a i niezauwa¿alna)
    
    R = convertToR(t,Ry,punkty,odlegloscWezly/2);%funkcja ta zwraca listê wartoœci jakiej
    %powinny mieæ kolejne punkty tak aby by³y walcami
    
    [x, y, z] = cylinder(R);%obrót powsta³ych R-ów wokó³ osi
    
    surf(screen,z,x,y);%narysowanie powsta³ej bry³y na wykresie
    
    V = VWalca(Ry,odlegloscWezly);%obliczenie objêtoœci poszczególnych walców
    V = sum(V);%zsumowanie objêtoœci wszystkich walców
    
end