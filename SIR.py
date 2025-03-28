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
    if S[-1]>0:
        infection_results=np.random.choice(range(2),size=S[-1],p=[1-infection_prob,infection_prob])
        new_infections=np.sum(infection_results)
    else:
        new_infections=0
    #randomly choose susceptible people for infection
    if I[-1]>0:
        recovery_results=np.random.choice(range(2),size=I[-1],p=[1-gamma,gamma]) 
        new_recoveries=np.sum(recovery_results)
    else:
        new_recoveries=0   
    #randomly choose infected people for recovery 
    s=S[-1]-new_infections
    i=I[-1]+new_infections-new_recoveries
    r=R[-1]+new_recoveries
    #update the number of people in each group
    s=max(s,0)
    i=max(i,0)
    r=max(r,0)
    #ensure that the number is not negative
    S.append(s)
    I.append(i)
    R.append(r)
    #add to the array
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S,label="Susceptible")
plt.plot(I,label="Infected")
plt.plot(R,label="Recovered")
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend()
plt.grid(True)
plt.savefig("SIR Model.png",format="png")
plt.show()
#draw the result


