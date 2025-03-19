Language=['JavaScript','HTML','Python','SQL','TypeScript']
Users=['62.3%','52.9%','51%','51%','38.5%']
data_dict=dict(zip(Language,Users))   
print(data_dict) 

import pandas as pd
import matplotlib.pyplot as plt
data={'Language':['JavaScript','HTML','Python','SQL','TypeScript'],'Users':[62.3,52.9,51,51,38.5]}
#the data of the flame
df=pd.DataFrame(data)
df.plot(kind='bar',x='Language',y='Users',color='red',legend=False)
#use pandas to draw the plot
plt.title('Language popularity')
#add the title
plt.xlabel('Language')
plt.ylabel('Users/%')
#add the axis title
plt.show()
#show the plot

df.set_index('Language',inplace=True)
#set the 'Language' as index
key=input("please input the language you want to inquire")
if key in df.index:
    print(f"this language's users are {df.loc[key,'Users']} of the word's population")
else:
    print("inexistence")