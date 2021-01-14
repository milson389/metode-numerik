%PCA IMAGE

clear; clc;

%READR UMPUT
%val(:,:,1) = red - val(:,:,2) = green - val(:,:,3) = blue
%imread digunakan untuk membaca gambar
rumput1 = imread('rumput5x5(1).jpg'); 
%bertipe uint8, tidak dapat ditranspose
rumput1 = double(rumput1);
%harus diganti ke double supaya bisa diolah

rumput2 = imread('rumput5x5(2).jpg'); 
rumput2 = double(rumput2);

rumput3 = imread('rumput5x5(3).jpg'); 
rumput3 = double(rumput3);

rumput4 = imread('rumput5x5(4).jpg'); 
rumput4 = double(rumput4);

%READ ASPAL
aspal1 = imread('ASPAL5x5(1).jpg'); 
aspal1 = double(aspal1);

aspal2 = imread('ASPAL5x5(2).jpg'); 
aspal2 = double(aspal2);


%RGB Filter Rumput Matriks Red Green Blue
redR1 = rumput1(:,:,1); %Matriks Red Rumput 1
greenR1 = rumput1(:,:,2); %Matriks Greeen Rumput 1
blueR1 = rumput1(:,:,3); %Matriks Blue Rumput 1

redR2 = rumput2(:,:,1);
greenR2 = rumput2(:,:,2);
blueR2 = rumput2(:,:,3);

redR3 = rumput3(:,:,1);
greenR3 = rumput3(:,:,2);
blueR3 = rumput3(:,:,3);

redR4 = rumput4(:,:,1);
greenR4 = rumput4(:,:,2);
blueR4 = rumput4(:,:,3);

%RGB Filter Aspal Matriks Red Green Blue
redA1 = aspal1(:,:,1);
greenA1 = aspal1(:,:,2);
blueA1 = aspal1(:,:,3);

redA2 = aspal2(:,:,1);
greenA2 = aspal2(:,:,2);
blueA2 = aspal2(:,:,3);


%UBAH KE VEKTOR
[n,p] = size(redR1);
k = 0;
for j = 1:p
    for i = 1:p
        k = k + 1;
        %RUMPUT
        V_RRumput1(k,1) = redR1(j,i); %Mengubah Matriks Red menjadi Vektor Red
        V_GRumput1(k,1) = greenR1(j,i); %Mengubah Matriks Green menjadi Vektor Green
        V_BRumput1(k,1) = blueR1(j,i); %Mengubah Matriks Blue menjadi Vektor Blue
        Mat_Rumput1 = [V_RRumput1, V_GRumput1, V_BRumput1] 
        %satukan 3 vektor menjadi satu matriks besar
        
        V_RRumput2(k,1) = redR2(j,i); %Mengubah Matriks Red menjadi Vektor Red
        V_GRumput2(k,1) = greenR2(j,i); %Mengubah Matriks Green menjadi Vektor Green
        V_BRumput2(k,1) = blueR2(j,i); %Mengubah Matriks Blue menjadi Vektor Blue
        Mat_Rumput2 = [V_RRumput2, V_GRumput2, V_BRumput2] 
        %satukan 3 vektor menjadi satu matriks besar
        
        V_RRumput3(k,1) = redR3(j,i); %Mengubah Matriks Red menjadi Vektor Red
        V_GRumput3(k,1) = greenR3(j,i); %Mengubah Matriks Green menjadi Vektor Green
        V_BRumput3(k,1) = blueR3(j,i); %Mengubah Matriks Blue menjadi Vektor Blue
        Mat_Rumput3 = [V_RRumput3, V_GRumput3, V_BRumput3] 
        %satukan 3 vektor menjadi satu matriks besar
        
        V_RRumput4(k,1) = redR4(j,i); %Mengubah Matriks Red menjadi Vektor Red
        V_GRumput4(k,1) = greenR4(j,i); %Mengubah Matriks Green menjadi Vektor Green
        V_BRumput4(k,1) = blueR4(j,i); %Mengubah Matriks Blue menjadi Vektor Blue
        Mat_Rumput4 = [V_RRumput4, V_GRumput4, V_BRumput4] 
        %satukan 3 vektor menjadi satu matriks besar
        
        %ASPAL
        V_RAspal1(k,1) = redA1(j,i); %Mengubah Matriks Red menjadi Vektor Red
        V_GAspal1(k,1) = greenA1(j,i); %Mengubah Matriks Green menjadi Vektor Green
        V_BAspal1(k,1) = blueA1(j,i); %Mengubah Matriks Blue menjadi Vektor Blue
        Mat_Aspal1 = [V_RAspal1, V_GAspal1, V_BAspal1] 
        %satukan 3 vektor menjadi satu matriks besar
        
        V_RAspal2(k,1) = redA2(j,i); %Mengubah Matriks Red menjadi Vektor Red
        V_GAspal2(k,1) = greenA2(j,i); %Mengubah Matriks Green menjadi Vektor Green
        V_BAspal2(k,1) = blueA2(j,i); %Mengubah Matriks Blue menjadi Vektor Blue
        Mat_Aspal2 = [V_RAspal2, V_GAspal2, V_BAspal2] 
        %satukan 3 vektor menjadi satu matriks besar
        
    end
end

[nv, pv] = size(Mat_Aspal2);

% PROSES GREYSCALE
for i = 1:nv
   %Rumput
   greyscale1(i,1) = (0.299*V_RRumput1(i,1))+(0.587*V_GRumput1(i,1))+(0.114*V_BRumput1(i,1)); 
   greyscale2(i,1) = (0.299*V_RRumput2(i,1))+(0.587*V_GRumput2(i,1))+(0.114*V_BRumput2(i,1)); 
   greyscale3(i,1) = (0.299*V_RRumput3(i,1))+(0.587*V_GRumput3(i,1))+(0.114*V_BRumput3(i,1)); 
   greyscale4(i,1) = (0.299*V_RRumput4(i,1))+(0.587*V_GRumput4(i,1))+(0.114*V_BRumput4(i,1)); 
    
   % Aspal
   greyscale5(i,1) = (0.299*V_RAspal1(i,1))+(0.587*V_GAspal1(i,1))+(0.114*V_BAspal1(i,1)); 
   greyscale6(i,1) = (0.299*V_RAspal2(i,1))+(0.587*V_GAspal2(i,1))+(0.114*V_BAspal2(i,1)); 
end

%GABUNG SEMUA VEKTOR MENJADI 1 MATRIKS BESAR
Mat_GrayScale = [greyscale1 greyscale2 greyscale3 greyscale4 greyscale5 greyscale6]
Mat_GS = Mat_GrayScale' %TRANSPOSE MATRIKS


%PROSES PCA
[na,pa] = size(Mat_GS);

%Proses Normalisasi Data
Xrata = mean((Mat_GS)');

%1. Kurangi Data X dengan Vektor rata-rata
for i = 1:pa
    Zr(:,i) = Mat_GS(:,i) - Xrata'
end

%2. Covariance Matriks
S = cov(Mat_GS)

%3. Bagi dengan Akar Covariance Matriks pada Elemen Diagonal Utama
for i = 1:na
    for j = 1:pa
        Z(i, j) = Zr(i, j) / sqrt(S(j,j));
    end
end

%TAHAP REDUKSI DIMENSI
Zcov = cov(Z)

%1. Mencari Nilai Eigen Value dan Eigen Vektor
[VA, DA] = eig(Zcov);

%2. Urutkan Eigen Value dan Eigen Vektor dari Terbesar ke Terkecil
m = 1;
for k = pa:-1:1
    DA_Urut(m,m) = DA(k,k);
    VA_Urut(:,m) = VA(:,k);
    m = m + 1; 
end

%3. Membuat Vektor Urut
for j = 1:pa
    Vektor_DA_Urut(j,1) = DA_Urut(j,j);
end

%Hitung Jumlah Vektor
Total = sum(Vektor_DA_Urut)

%Perhitungan Komponennya
proporsiKum = 0;
komponen = 0;
for j = 1:na
    proporsiValue(j,:) = Vektor_DA_Urut(j,1) / Total;
    if(proporsiKum<0.95)
        proporsiKum = proporsiKum + proporsiValue(j,:);
        komponen = komponen + 1;
    end
end

%VA_Komponen = akan digunakan untuk membentuk Variabel Baru yang disebut
%Variabel Komponen Utama
VA_Komponen = VA_Urut(:,1:komponen)

W = Z * VA_Komponen %W = Variabel Komponen Utama

%plot(W(:,1),'*') %Plot 1 Dimensi
%plot(W(:,1), W(:,2),'*') %Plot 2 Dimensi
plot3(W(:,1), W(:,2), W(:,3), '*') %Plot 3 Dimensi
grid on
pause()