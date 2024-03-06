a=0.05 #initial density
day=0
while a<=0.9 :  #samller than 90%
    day+=1     #calculate the number of days
    a=2*a    #cell line doubles in density every 24 hours
    if a>0.9 :
        break
print(day)