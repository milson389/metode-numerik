%Audie Milson 535180021

clear; clc;

data = [6.5079,16.41;8.0814,16.6266;3.9090, 15.9;6.1082,16.3467;9.9294,16.8325;
    9.9629,16.8359;2.2558,15.3505;3.0724,15.6594;1.5146,14.9522;5.4081,16.2245];

sortedData = sort(data,1)

xTanya = 7.3;
xTanya1 = 5;

disp('Nilai f(x = 7.3) : ');
orde = input('Orde ke : ');
hasil = lagrange_func(sortedData, xTanya, orde)

disp('Nilai f(x = 5.0) : ');
orde1 = input('Orde ke : ');
hasil1 = lagrange_func(sortedData, xTanya1, orde1)