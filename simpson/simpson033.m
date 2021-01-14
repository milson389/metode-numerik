function [result] = simspon033(f, atas, bawah, h, segmen)
    h = (atas-bawah)/segmen;
    x = [];

    nilaiX = bawah;
    for i = 1:segmen+1
       x(i,:) = nilaiX;
       nilaiX = nilaiX + h;
    end
    fx = [];
    for i = x
       fx(:,1) = f(i);
    end
    [baris, kolom] = size(fx);
    hasilSegmen = 0;
    for i = 1:baris
       if(i>1 && i<baris)
           if(mod(i,2)==0)
                hasilSegmen = hasilSegmen + (4*fx(i,:));
           else
                hasilSegmen = hasilSegmen + (2*fx(i,:));
           end  
       else
           hasilSegmen = hasilSegmen + fx(i,:);
       end
    end
    
    inSim33 = (atas-bawah)*(hasilSegmen/(3*segmen));
    result = inSim33;
end