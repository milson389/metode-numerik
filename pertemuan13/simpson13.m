function [result] = simpson033(f, atas, bawah, segmen, h)
    
    totalGenap = 0;
    totalGanjil = 0;
    
    for i = 1:segmen-1
       xi = bawah + i*h;
       if(mod(i,2) == 0)
          totalGenap = totalGenap + f(xi);
       else
          totalGanjil = totalGanjil + f(xi);
       end
    end
    
    result = (atas-bawah)*(f(bawah) + (4*totalGanjil) + (2*totalGenap) + f(atas))/(3*segmen);
end