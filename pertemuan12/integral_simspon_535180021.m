% Audie Milson ( 535180021 )
clear; clc;

bAtas = 2;
bBawah = 0.5;
segment = 2;
segment_0375 = 3;

fun = @(x) (0.5*(exp(1.5*x+1)))-(3*sqrt(x));
nilaiIntegral = integral(fun, bBawah, bAtas);

hasil_simpson033 = simpson033(fun, bAtas, bBawah, segment)
error_eksak = (abs(nilaiIntegral-hasil_simpson033)/nilaiIntegral)*100

hasil_simpson0375 = simpson0375(fun, bAtas, bBawah, segment_0375)
error_eksak1 = (abs(nilaiIntegral-hasil_simpson0375)/nilaiIntegral)*100