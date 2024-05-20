import numpy as np
import matplotlib.pyplot as plt #import libraries

total=10000
susceptible=9999
infected=1
recovered=0
beta=0.3
gamma=0.05 #define variables 

all_susceptible=[susceptible]
all_infected=[infected]
all_recovered=[recovered] #create directtory

for time in range(1,1000) :
    probability_infected=beta*all_infected[-1]/(total-1)
    probability_recovered=gamma
    new_infected=np.random.choice(range(2), all_susceptible[-1], p=[1-probability_infected,probability_infected]).sum()
    new_recovered=np.random.choice(range(2), all_infected[-1], p=[1-probability_recovered,probability_recovered]).sum() #get the random number from the np.random.choice function

    all_susceptible.append(all_susceptible[-1]-new_infected)
    all_infected.append(all_infected[-1]+new_infected-new_recovered)
    all_recovered.append(all_recovered[-1]+new_recovered)  #write down numbers

plt.figure(figsize=(6,4), dpi=150)
plt.plot(range(1,1001), all_susceptible, label="susceptible")
plt.plot(range(1,1001), all_infected, label="infected")
plt.plot(range(1,1001), all_recovered, label="recovered")
plt.xlabel("Time")
plt.ylabel("Number")
plt.title("SIR Moedel")
plt.legend(["Susceptible", "Infected", "Recovered"])
plt.savefig("SIR Model.png", format="png")
plt.show()
plt.clf() #show the figure





