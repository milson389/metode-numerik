function [result] = simspon0375(f, atas, bawah, segmen)
    h = (atas-bawah)/segmen;
    x = [];

    nilaiX = bawah;
    for i = 1:segmen+1
       x(i,:) = nilaiX;
       nilaiX = nilaiX + h;
    end
    x
    fx = [];
    for i = x
       fx(:,1) = f(i);
    end
    fx
    [baris, kolom] = size(fx);
    hasilSegmen = 0;
    for i = 1:baris
       if(i>1 && i<baris)
           hasilSegmen = hasilSegmen + (3*fx(i,:));
       else
           hasilSegmen = hasilSegmen + fx(i,:);
       end
    end
    
    inSim375 = (atas-bawah)*(hasilSegmen/(8));
    result = inSim375;
end