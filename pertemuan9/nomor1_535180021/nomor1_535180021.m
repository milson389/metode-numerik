% Audie Milson 535180021
clear; clc;

% Bisection Method
xi = 0;
xu = 1.5;

disp('Bisection Method');
hasil_bisec = bisection_func(xi,xu);
list_iter = hasil_bisec(:,1);
list_xr = hasil_bisec(:,2);
list_ea = hasil_bisec(:,3);

% Regulafalsi
xi_r = 0;
xu_r = 1.5;

disp('Regulafalsi');
hasil_regula = regula_func(xi_r,xu_r);
listr_iter = hasil_regula(:,1);
listr_xr = hasil_regula(:,2);
listr_ea = hasil_regula(:,3);

% Newton Raphson
xtebakan = 0;

disp('Newton Raphson');
hasil_newton = newton_func(xtebakan);
listn_iter = hasil_newton(:,1);
listn_xi = hasil_newton(:,2);
listn_ea = hasil_newton(:,3);

% Secant
xprev = 0;
xcurr = 0.2;

disp('Secant');
hasil_secant = secant_func(xprev, xcurr);
lists_iter = hasil_secant(:,1);
lists_xi = hasil_secant(:,2);
lists_ea = hasil_secant(:,3);


figure1 = figure('Position',[100,100,800,600]);
subplot(2,1,1)
plot(list_iter, list_xr, 'b-o', listr_iter, listr_xr, 'y-o', listn_iter, listn_xi, 'g-o', lists_iter, lists_xi, 'r-o')
title('Akar persamaan f(x) = 3x + sin(x) - exp(x)')
ylabel('Akar')
legend('Biseksi', 'Regulafalsi', 'Newton Raphson', 'Secant')
grid on

subplot(2,1,2)
plot(list_iter, list_ea, 'b-o', listr_iter, listr_ea, 'y-o', listn_iter, listn_ea, 'g-o', lists_iter, lists_ea, 'r-o')
ylabel('Error (%)')
xlabel('Iterasi')
legend('Biseksi', 'Regulafalsi', 'Newton Raphson', 'Secant')
grid on

pause()
% enter untuk mengakhiri

