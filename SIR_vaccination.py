import numpy as np
import matplotlib.pyplot as plt

def run_sir_simulation(vaccination_percent):
    N=10000 #define the total number
    beta=0.3 #define beta
    gamma=0.05 #define gamma
    vaccinated_count=int(N*vaccination_percent/100)
    S=[N-vaccinated_count-1] #the initial number of susceptible people
    V=[vaccinated_count] #the vaccinated people
    I=[1] #the initial number of infected people
    R=[0] #the initial number of people who have recovered
    vaccine_efficacy=0.9
    for t in range(1000):
        infection_prob_susceptible=beta*I[-1]/N #calculate the current infection probability
        infection_prob_vaccinated=infection_prob_susceptible*(1-vaccine_efficacy) #infection probability for vaccinated
        if S[-1]>0:
            infection_results_S=np.random.choice(range(2),size=S[-1],p=[1-infection_prob_susceptible,infection_prob_susceptible])
            infections_S=np.sum(infection_results_S)
        else:
            infections_S=0
    #randomly choose susceptible people for infection
        if V[-1]>0:
            infection_results_V=np.random.choice(range(2),size=I[-1],p=[1-infection_prob_vaccinated,infection_prob_vaccinated]) 
            infections_V=np.sum(infection_results_V)
        else:
            infections_V=0 
    #randomly choose vaccinated people for infection  
        if I[-1]>0:
            recovery_results=np.random.choice(range(2),size=I[-1],p=[1-gamma,gamma]) 
            new_recoveries=np.sum(recovery_results)
        else:
            new_recoveries=0   
    #randomly choose infected people for recovery 
        s=S[-1]-infections_S
        v=V[-1]-infections_V
        i=I[-1]+infections_S+infections_V-new_recoveries
        r=R[-1]+new_recoveries
    #update the number of people in each group
        s=max(s,0)
        v=max(v,0)
        i=max(i,0)
        r=max(r,0)
    #ensure that the number is not negative
        S.append(s)
        V.append(v)
        I.append(i)
        R.append(r)
    #add to the array
    return S,V,I,R
vaccination_percentages=[0,10,20,30,50,70]
results={}
#Run simulations for different vaccination percentages
for vp in vaccination_percentages:
    results[vp]=run_sir_simulation(vp)
#plot comparison of infected curves
plt.figure(figsize=(6,4),dpi=150)
for vp in vaccination_percentages:
    plt.plot(results[vp][2], label=f'{vp}% vaccinated')
plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('Infected People Over Time for Different Vaccination Percentages')
plt.legend()
plt.grid(True)
plt.savefig("Vaccination_Comparison.png", format="png")
plt.show()
# Plot comparison of infected curves
plt.figure(figsize=(6,4),dpi=150)
S, V, I, R = results[10]
plt.plot(S,label="Susceptible")
plt.plot(V, label="Vaccinated")
plt.plot(I,label="Infected")
plt.plot(R,label="Recovered")
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIRV Model with 10% Vaccination')
plt.legend()
plt.grid(True)
plt.savefig("SIRv_Model_10%.png",format="png")
plt.show()
# Plot one scenario with all compartments (10% vaccinated)

print("Peak infections for each vaccination percentage:")
for vp in vaccination_percentages:
    peak_infections = max(results[vp][2])
    print(f"{vp}% vaccinated: {peak_infections} peak infections")
# Print peak infections for each scenario


