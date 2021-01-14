clear; clc;

p = input('Panjang: ');
l = input('Lebar: ');

luas = hitung_luas(p,l);
disp(['Luas = ' num2str(luas)]);

% contoh lambda function
f = @(x,y) 3*x+y;
f(6, 7);

x = -3:0.1:3;
y = x .^ 3;
plot(x,y);
pause()
% octave --persist contoh_fx.m
% untuk mendisplay plot