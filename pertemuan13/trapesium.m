function [result] = trapesium(f, atas, bawah, segmen)
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
           hasilSegmen = hasilSegmen + (2*fx(i,:));
       else
           hasilSegmen = hasilSegmen + fx(i,:);
       end
    end
    
    inTrapesium = (atas-bawah)*(hasilSegmen/(2*segmen));
    result = inTrapesium;
end