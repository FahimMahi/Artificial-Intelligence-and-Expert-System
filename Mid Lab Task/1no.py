def population(year):     
    if(2000<=year):
        l = year%100        
        s = l - 10    
        m = s*3      
        p = m + 310       
        return p  
    
    else:
        print("-1")
    
print(population(2001)) 
print(population(2010)) 
print(population(2016))