import numpy as np
import matplotlib.pyplot as plt
N=10000 #define the total number
beta=0.3 #define beta
gamma=0.05 #define gamma
S=[N-1] #the initial number of susceptible people
I=[1] #the initial number of infected people
R=[0] #the initial number of people who have recovered
for t in range(1000):
    infection_prob=beta*I[-1]/N #calculate the current infection probability
    new_infections=np.random.choice(range(2),S,p=[1-infection_prob,infection_prob])
    #randomly choose susceptible people for infection
    new_recoveries=np.random.choice(range(2),I,p=[1-gamma,gamma]) 
    #randomly choose infected people for recovery 
    s=S[-1]-new_infections
    i=I[-1]+new_infections-new_recoveries
    r=R[-1]+new_recoveries
    #update the number of people in each group
    s=max(s.all(),0)
    i=max(i.all(),0)
    r=max(r.all(),0)
    #ensure that the number is not negative
    S.append(s)
    I.append(i)
    R.append(r)
    #add to the array
plt.figure(figsize=(10,6))
plt.plot(S,label="Susceptiblle")
plt.plot(I,label="Infected")
plt.plot(R,label="Recovered")
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend()
plt.grid(True)
plt.show()
#draw the result

