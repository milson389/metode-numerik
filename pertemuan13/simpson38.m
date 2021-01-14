function [result] = simpson38(f, atas, bawah, h)
     x1 = bawah + h;
     x2 = x1 + h;
    total = f(x1) + f(x2);
    
    result = (atas-bawah)*((f(bawah) + (3*total) + f(atas))/8);
end