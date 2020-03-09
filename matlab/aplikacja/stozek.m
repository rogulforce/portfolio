function V = stozek(fun,przedzial,dokladnosc,screen)
%stozek(@(x) x^2,[1,2],5)
a=przedzial(1);
b=przedzial(2);

iksy=[];
igreki=[];
V=0;        %objetosc
poczatek=feval(fun,a);
koniec=feval(fun,b);

    dx=(b-a)/dokladnosc;    %dzielimy przedzial na dokladnosc (odleglosc pomiedzy kolejnymi iksami)
    for c=0:dokladnosc
        iksy=[iksy, a+c*dx]; %tworzymy podzial przedzialu
        
    end
    
    for n=1:length(iksy)
        p=iksy(n);
        igreki=[igreki, feval(fun,p)]; %wartosci dla przedzialu
    end
    
        %if sum(igreki<0) ~= 0
        %    disp('wartosci w danym przedziale nie moga byc ujemne')
        %end
    abs_igreki=abs(igreki);
    
    %plot(iksy,igreki);

    [iks,igrek,zet]=cylinder(igreki);
    surf(screen,zet,iks,igrek);

    
    for n=1:length(iksy)-1
        R=abs_igreki(n);
        r=abs_igreki(n+1);
        V=V+(pi./3)*dx*(R.^2+r*R+r.^2);     %objetosc
    end

end
