function m = macierz_01(n)
 % funkcja macierze_01(n) zawraca macierz
 %  _            _
 % |     /\       |
 % |    /__\      | 
 % |_  /    \I,J _|
 %
 % rozmiaru n x n tak�, �e 
 %
 % >je�li 4 dzieli (i+j), to :
 %
 %  _            _          __
 % |     /\       |        |  |
 % |    /__\      |   =    |  |
 % |_  /    \I,J _|        |__|
 %
 % >je�li 4 nie dzieli (i+j), to :
 %
 %  _            _          /|
 % |     /\       |        / |
 % |    /__\      |   =      |
 % |_  /    \I,J _|        __|__
 %
 % np: macierz_01(10) zwr�ci macierz postaci:
 %
 %   0     0     1     0     0     0     1     0     0     0
 %   0     1     0     0     0     1     0     0     0     1
 %   1     0     0     0     1     0     0     0     1     0
 %   0     0     0     1     0     0     0     1     0     0
 %   0     0     1     0     0     0     1     0     0     0
 %   0     1     0     0     0     1     0     0     0     1
 %   1     0     0     0     1     0     0     0     1     0
 %   0     0     0     1     0     0     0     1     0     0
 %   0     0     1     0     0     0     1     0     0     0
 %   0     1     0     0     0     1     0     0     0     1
 %
 % autor: Piotr Rogula
 if n <= 0 || n~=round(n)
   m=[];
   disp('B��d! n i m powinny by� liczbami naturalnymi.')
   %imo lepsze jest 'disp' zamiast 'error' ale je�li to problem, to mo�na
   %zamieni� 'disp' na 'error'
 else

 m=zeros(n,n);              
 m(3:4:end,1:4:end)=1;  %zmienia co 4 element pocz�wszy od trzeciego w co czwartej kolumnie pocz�wszy od peirwszej
 m(2:4:end,2:4:end)=1;  %analogicznie
 m(1:4:end,3:4:end)=1;  %analogicznie
 m(4:4:end,4:4:end)=1;  %analogicznie
 end
 
end