% Audie Milson ( 535180021 )
clear; clc;

bAtas = 2;
bBawah = 0.5;
segment = 2;

fun = @(x) (0.5*(exp(1.5*x+1)))-(3*sqrt(x));
nilaiIntegral = integral(fun, bBawah, bAtas);

error = 100;

while(error > 0.001)
    segment = segment + 1;
    if(mod(segment,2)==1)
        if(segment-3 > 1)
            hasil_simpson = simpson0375(fun, bBawah+3*h, bBawah, segment)
        end
    else
        hasil_simpson1 = simpson033(fun, bAtas, bBawah+3*h, segment)
    end
end