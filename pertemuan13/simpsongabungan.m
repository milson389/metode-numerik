function [result] = simpsongabungan(f, atas, bawah, segmen)
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
    for i = 1:baris
        if(mod(segmen,2)==1)
            result = simpson38(f, bawah+3*h, bawah, h);
            if(segmen-3 > 1)
                hasil = simpson38(f, bawah+3*h, bawah, h);
                result = hasil + simpson13(f, atas, bawah+3*h, segmen-3, h);
            end
        else
            result = simpson13(f, atas, bawah, segmen, h);
        end
    end
end