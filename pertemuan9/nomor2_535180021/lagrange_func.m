function [hasil] = lagrange_func(list, xTanya, bData)
result = 0;
orde = bData;
for i = 1:orde
   term = list(i,2);
   for j = 1:orde
    if(j ~= i)
        term = term * (xTanya - list(j,1))/(list(i,1)-list(j,1));
    end
   end
   result = result + term;
end
hasil = result;
end