function [list] = secant_func(tebakan_prev, tebakan_curr)
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
       prevX = tebakan_prev;
       currX = tebakan_curr;
       nextX = currX - (func(currX)*(currX-prevX))/(func(currX)-func(prevX));
       disp(['Nilai Xi+1 : ' num2str(nextX)]);
       list_xi(iterasi,:) = nextX;
       if(iterasi>1)
           ea = abs((nextX-currX)/nextX)*100;
           disp(['Nilai EA : ' num2str(ea)]);
           disp('');
       else
           ea = 100;
           disp('');
       end
       list_ea(iterasi,:) = ea;
       tebakan_prev = tebakan_curr;
       tebakan_curr = nextX;
    end
list(:,1) = list_iter(:,1);
list(:,2) = list_xi(:,1);
list(:,3) = list_ea(:,1);
end