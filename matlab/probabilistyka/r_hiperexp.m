function y = r_hiperexp(p,lambda,N)
y = -log(rand(1,N))./lambda((length(p)+1)*ones(1,N)-sum(cumsum(repmat(p',1,N))>repmat(rand(1,N),length(p),1)));

% a tutaj bardziej czytelnie ale w wiekszej ilosci linijek

%generowanie indeksu Lambda_i
%  P_i = cumsum(repmat(p',1,N));
%  U = repmat(rand(1,N),length(p),1);
%  i = (length(p)+1)*ones(1,N)-sum(P_i>U);
%generowanie rozkladu dla podanego lambda
%  y = -log(rand(1,N))./lambda(i);
end