cities1=["Edinburgh","Glasgow","Stirling","London"]
cities2=["Haining","Hangzhou","Shanghai","Beijing"]

UK_cities=[0.56,0.62,0.04,9.7]
China_cities=[0.58,8.4,29.9,22.2]
sorted_UK_cities=sorted(UK_cities)
sorted_China_cities=sorted(China_cities)
print(sorted_UK_cities)
print(sorted_China_cities)     #The code above is to sort the values of populations.


import numpy as np
import matplotlib.pyplot as plt
plt.figure() 
plt.bar(cities1,UK_cities)
plt.ylabel("UK_cities")
plt.xlabel("cities1")
plt.title("UK")
plt.show()
plt.clf()   # It aims to show the bar plots of UK cities sizes.


plt.figure() 
plt.bar(cities1,UK_cities)
plt.ylabel("China_cities")
plt.xlabel("cities2")
plt.title("China")
plt.show()
plt.clf()   #It aims to show the bar plots of China cities sizes.
