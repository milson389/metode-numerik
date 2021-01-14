clear; clc;

% SPL
% 3x1 - 4x2 + 2x3 = 7
% 2x1 + x2 + 3x3 = 9
% x1 + 2x2 + 2x3 = 10


% Augmented Matrix, gabungan dari matrix A dan C
aug = xlsread('data_spl');
[n, m] = size(aug);

% Forward Elimination, membuat matrix segitiga atas
for i = 1:n
    % buat diagonal utama jadi 1, caranya bagi dengan pivot
    pivot = aug(i,i);
    for j = 1:m
        aug(i, j) = aug(i, j) / pivot;
    end
    % meng-nol-kan kolom di bawah diagonal utama
    for j = i+1 : n
        factor = aug(j, i);
        for k = 1:m
            aug(j, k) = aug(j, k)-factor*aug(i, k);
        end
    end
end

aug
% Backward substitution, mendapatkan nilai x
x(n) = aug(n, m);
for i = n-1:-1:1
    sum = 0;
    for j = i+1 : n
        sum = sum + aug(i, j)*x(j);
    end
    x(i) = aug(i, m) - sum;
end
x
