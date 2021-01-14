a = 5;
b = 7;
c = 8;

result = a + b + c;
disp(['Hasil penjumlahan = ' num2str(result)]);

s = input('Masukkan nilai sisi persegi : ');
luas = s*s;
disp(['Luas = ' num2str(luas)]);

N = input('Masukkan bilangan bulat : ');

if(N>0)
    disp('Positif');
elseif(N<0)
    disp('Negatif');
else
    disp('Nol');
end

%loop startnya dari mana berhentinya samapi berapa
for i = 1:1000
    disp(i);
end

%looping jaraknya berapa di taruh di parameter tengahnya
for i = 1:100:1000
    disp(i);
end

%While loop
j = 10;
while(j<100)
   disp(j);
   j = j + 10;
end

%Array
v = [10,20,30];%Vektor baris
w = [40 50 60];%Vektor baris
z = [56; 78;90];%Vektor kolom
p = [1,2,3;4,5,6;7,8,9;];%Matrix / Array 2D
acak = rand(3,3);
acak1 = randi(100,[4,3]);%maksimum 100 angka randomnya dengan matrix ukuran 4x3
A = eye(5,5);

% perkalian tiap element .*
% perkalian matrix biasa *
a = randi(30,3);
b = randi(10,3);
hasil1 = a .* b
hasil2 = a/b
hasil3 = a./b
hasil4 = a .^b


