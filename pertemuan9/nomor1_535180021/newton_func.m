function [list] = newton_func(tebakan1)
    ea = 100;
    es = 0.01;
    iterasi = 0;
    list_ea = [];
    list_xi = [];
    list_iter = [];
    
    while(ea > es)
       iterasi = iterasi + 1;
       disp(['Iterasi : ', num2str(iterasi)])
       list_iter(iterasi,:) = iterasi;
       xi = tebakan1;
       nextX =  xi - (func(xi)/turunan_func(xi));
       disp(['Nilai Xi : ' num2str(nextX)]);
       list_xi(iterasi,:) = nextX;
       if(iterasi<1)
           ea = 100;
           disp('');
       else
           ea = abs((nextX-xi)/nextX)*100;
           disp(['Nilai EA : ' num2str(ea)]);
           disp('');
       end
       list_ea(iterasi,:) = ea;
       tebakan1 = nextX;
    end
list(:,1) = list_iter(:,1);
list(:,2) = list_xi(:,1);
list(:,3) = list_ea(:,1);
end