%PCA Image

clear; clc;

%Rumput
%imread digunakan untuk membaca Gambar
rumput1 = imread('rumput5x5(1).jpg'); %bertipe uint8 tidak dapat ditranspose
rumput1 = double(rumput1); % harus diganti ke double supaya bisa diolah

rumput2 = imread('rumput5x5(2).jpg');
rumput2 = double(rumput2); 

rumput3 = imread('rumput5x5(3).jpg'); 
rumput3 = double(rumput3);

rumput4 = imread('rumput5x5(4).jpg'); 
rumput4 = double(rumput4); 

%Aspal
aspal1 = imread('ASPAL5x5(1).jpg');
aspal1 = double(aspal1);

aspal2 = imread('ASPAL5x5(2).jpg');
aspal2 = double(aspal2);


% RGB
%Matrix RGB Rumput1
redR1 = rumput1(:,:,1); 
greenR1 = rumput1(:,:,2); 
blueR1 = rumput1(:,:,3); 

%Matrix RGB Rumput2
redR2 = rumput2(:,:,1); 
greenR2 = rumput2(:,:,2); 
blueR2 = rumput2(:,:,3); 

%Matrix RGB Rumput3
redR3 = rumput3(:,:,1); 
greenR3 = rumput3(:,:,2); 
blueR3 = rumput3(:,:,3); 

%Matrix RGB Rumput4
redR4 = rumput4(:,:,1); 
greenR4 = rumput4(:,:,2); 
blueR4 = rumput4(:,:,3); 

%Matrix RGB Aspal1
redA1 = aspal1(:,:,1);
greenA1 = aspal1(:,:,2);
blueA1 = aspal1(:,:,3);

redA2 = aspal2(:,:,1);
greenA2 = aspal2(:,:,2);
blueA2 = aspal2(:,:,3);


%UBAH KE VEKTOR
[n,p] = size(redR1);
k = 0;
for j=1:p
    for i=1:p
        k = k+1;
        
        %Rumput
        VK_RRumput1(k,1) = redR1(j,i); %mengubah matrix red menjadi vektor red
        VK_GRumput1(k,1) = greenR1(j,i); %mengubah matrix green menjadi vektor green
        VK_BRumput1(k,1) = blueR1(j,i); %mengubah matrix blue menjadi vektor blue
        Mat_Rumput1 = [VK_RRumput1 VK_GRumput1 VK_BRumput1]%satukan 3 vektor tadi menjadi satu matrix besar
        
        VK_RRumput2(k,1) = redR2(j,i); 
        VK_GRumput2(k,1) = greenR2(j,i);
        VK_BRumput2(k,1) = blueR2(j,i); 
        Mat_Rumput2 = [VK_RRumput2 VK_GRumput2 VK_BRumput2]
        
        VK_RRumput3(k,1) = redR3(j,i); 
        VK_GRumput3(k,1) = greenR3(j,i); 
        VK_BRumput3(k,1) = blueR3(j,i); 
        Mat_Rumput3 = [VK_RRumput3 VK_GRumput3 VK_BRumput3]
        
        VK_RRumput4(k,1) = redR4(j,i); 
        VK_GRumput4(k,1) = greenR4(j,i); 
        VK_BRumput4(k,1) = blueR4(j,i); 
        Mat_Rumput4 = [VK_RRumput4 VK_GRumput4 VK_BRumput4]
        
        %ASPAL
        %Rumput
        VK_RAspal1(k,1) = redA1(j,i); %mengubah matrix red menjadi vektor red
        VK_GAspal1(k,1) = greenA1(j,i); %mengubah matrix green menjadi vektor green
        VK_BAspal1(k,1) = blueA1(j,i); %mengubah matrix blue menjadi vektor blue
        Mat_Aspal1 = [VK_RAspal1 VK_GAspal1 VK_BAspal1]%satukan 3 vektor tadi menjadi satu matrix besar
        
        VK_RAspal2(k,1) = redA2(j,i); 
        VK_GAspal2(k,1) = greenA2(j,i);
        VK_BAspal2(k,1) = blueA2(j,i); 
        Mat_Aspal2 = [VK_RAspal2 VK_GAspal2 VK_BAspal2]
        
    end
end

[nv, pv]= size(Mat_Aspal2);

Acuan = zeros(nv, pv);
DistRumput1 = 0;
DistRumput2 = 0;
DistRumput3 = 0;
DistRumput4 = 0;
DistAspal1 = 0;
DistAspal2 = 0;

for i = 1:nv
    for j = 1:pv
        %Rumput
        DistRumput1 = DistRumput1 + (Mat_Rumput1(i,j)-Acuan(i,j))^2;
        DistRumput1 = sqrt(DistRumput1);
        
        DistRumput2 = DistRumput2 + (Mat_Rumput2(i,j)-Acuan(i,j))^2;
        DistRumput2 = sqrt(DistRumput2);
        
        DistRumput3 = DistRumput3 + (Mat_Rumput3(i,j)-Acuan(i,j))^2;
        DistRumput3 = sqrt(DistRumput3);
        
        DistRumput4 = DistRumput4 + (Mat_Rumput4(i,j)-Acuan(i,j))^2;
        DistRumput4 = sqrt(DistRumput4);
        
        %Aspal
        DistAspal1 = DistAspal1 + (Mat_Aspal1(i,j)-Acuan(i,j))^2;
        DistAspal1 = sqrt(DistAspal1);
        
        DistAspal2 = DistAspal2 + (Mat_Aspal2(i,j)-Acuan(i,j))^2;
        DistAspal2 = sqrt(DistAspal2);
        
    end
end

Distan = [DistRumput1, DistRumput2, DistRumput3, DistRumput3, DistAspal1, DistAspal2];
plot(Distan, 'ro');
pause()