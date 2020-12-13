function y = r_wykladniczy(lambda, N)
    u = rand(1, N);
    y = -log(u)/lambda;
end