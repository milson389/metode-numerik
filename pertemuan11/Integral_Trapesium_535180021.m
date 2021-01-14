% Audie Milson ( 535180021 )
clear; clc;

bAtas = 2;
bBawah = 0.5;
segment = 2;

fun = @(x) (0.5*(exp(1.5*x+1)))-(3*sqrt(x));
error_eksak = 100;
while(error_eksak > 0.001)
    hasil_trapesium = trapesium(fun, bAtas, bBawah, segment)
    nilaiIntegral = integral(fun, bBawah, bAtas);
    error_eksak = (abs(nilaiIntegral-hasil_trapesium)/nilaiIntegral)*100
    segment = segment + 1;
end
