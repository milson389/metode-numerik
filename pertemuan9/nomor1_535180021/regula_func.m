function [list] = regula_func(tebakan1, tebakan2)
    ea = 100;
    es = 0.01;
    iterasi = 0;
    list_ea = [];
    list_xr = [];
    list_iter = [];
while(ea > es)
  iterasi = iterasi + 1;
  list_iter(iterasi,:) = iterasi;
  disp(['Iterasi : ', num2str(iterasi)])
  xr = (tebakan2 - (func(tebakan2)*(tebakan1-tebakan2))/(func(tebakan1)-func(tebakan2)));
  disp(['Nilai Xr : ' num2str(xr)]);
  list_xr(iterasi,:) = xr;
  if(iterasi > 1)
     ea = abs((xr-prevXr)/xr)*100;
     disp(['Nilai EA : ' num2str(ea)]);
     disp('');
  else
      ea = 100;
      disp('');
  end
  list_ea(iterasi,:) = ea;
        
  if(func(tebakan1)*func(xr) < 0)
     tebakan2 = xr;
  elseif(func(tebakan1)*func(xr)>0)
     tebakan1 = xr;
  else 
     break;
  end
    prevXr = xr;
end
list(:,1) = list_iter(:,1);
list(:,2) = list_xr(:,1);
list(:,3) = list_ea(:,1);

end