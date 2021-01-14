% Audie Milson ( 535180021 )
clear; clc;

bAtas = 2;
bBawah = 0.5;
segment = 2;
seg_t = 2;

fun = @(x) (0.5*(exp(1.5*x+1)))-(3*sqrt(x));
nilaiIntegral = integral(fun, bBawah, bAtas);

error_s = 100;
error_t = 100;
iterasi = 0;
iter = 0;

array_simpson = [];
array_trapesium = [];

while(error_t > 0.0001)
    iter = iter + 1;
    hasil_trapesium = trapesium(fun, bAtas, bBawah, seg_t);
    error_t = (abs(hasil_trapesium-nilaiIntegral)/hasil_trapesium)*100;
    array_trapesium(iter,:) = [seg_t hasil_trapesium error_t];
    if(error_t < 0.0001)
         continue;
     else
         seg_t = seg_t + 1;
    end
end

% Simpson gabungan
 while(error_s > 0.0001)
     iterasi = iterasi + 1;
     hasil_gabungan = simpsongabungan(fun, bAtas, bBawah, segment);
     error_s = abs((hasil_gabungan-nilaiIntegral)/hasil_gabungan)*100;
     array_simpson(iterasi,:) = [segment hasil_gabungan error_s];
     if(error_s < 0.0001)
         continue;
     else
         segment = segment + 1;
     end
 end
 
array_trapesium
array_simpson
jumlah_segment_trapesium = seg_t
jumlah_segment_simpson = segment
 
 figure1 = figure('Position',[100,100,800,600]);
 subplot(2,1,1);
 plot(array_simpson(:,1), array_simpson(:,3),'bo', array_trapesium(:,1), array_trapesium(:,3), 'r*')
 title('Perbandingan Integral Trapesium dan Integral Simpson')
 xlabel('Segmen');
 ylabel('error(%)');
 legend('Integral Simpson','Integral Trapesium'); 
 subplot(2,1,2);
 plot(array_simpson(:,1), array_simpson(:,2),'bo', array_trapesium(:,1), array_trapesium(:,2), 'r*')
 xlabel('Segmen');
 ylabel('Nilai Integral');
 legend('Integral Simpson','Integral Trapesium');
 
 