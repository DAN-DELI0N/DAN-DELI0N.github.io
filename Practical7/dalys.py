import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv") #input the csv file
data_1=dalys_data.iloc[0:101:10,3]   # the fourth column from every 10th row, starting from the first row, for the first 100 rows

entity=dalys_data["Entity"]
afghanistan=dalys_data["Entity"]=="Afghanistan"  #boolean to show cl=olumns related to afghanistan
afghanistan_data=dalys_data[afghanistan]

china_data = dalys_data[dalys_data['Entity']=="China"]
china_mean=np.mean(china_data["DALYs"]) #calculate the mean DALYs in China

            

plt.figure()
plt.plot(china_data.Year, china_data.DALYs, "ro")
plt.xlabel("years")
plt.ylabel("DALYs")
plt.title("DALYs of china")
plt.xticks(china_data.Year, rotation=-90)
plt.show()
plt.clf()#show a plot

print(afghanistan_data)
print(data_1)
print(china_mean)
if china_mean>22270.51 :
    print("DALYs in 2019 for China were below the mean.")
elif china_mean<22270.51 :
    print("DALYs in 2019 for China were above the mean.")
else :
    print("DALYs in 2019 for China were equal to the mean.") #state if the 2019 DALYs is greater than the mean
            


#question
countries=""
data_2019=dalys_data[dalys_data["Year"]==2019]
for index,row in data_2019.iterrows():
    if row["DALYs"]<=18000 :
        countries+=row["Entity"]+","
print(countries)

