uk_countries=[57.11,3.13,1.91,5.45]
around_Zhejiang=[65.77,41.88,45.28,61.27,85.15]
#store the population sizes in two lists 
sorted_uk=sorted(uk_countries)
sorted_Zhejiang=sorted(around_Zhejiang)
#use sorted()to sort the data
print("After sorted, the population is",sorted_uk,"in uk, and",sorted_Zhejiang,"around Zhejiang")
#print the result

import matplotlib.pyplot as plt
labels_uk=['England','Wales','Northern Ireland','Scotland']
labels_Zhejiang=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']
plt.figure(figsize=(6,6))
plt.pie(uk_countries,labels=labels_uk,autopct='%1.11f%%',startangle=0)
#
plt.axis('equal')
#
plt.title(' the distribution of population sizes separately in UK countries')
#add the title
plt.show()
plt.figure(figsize=(6,6))
plt.pie(around_Zhejiang,labels=labels_Zhejiang,autopct='%1.11f%%',startangle=0)
plt.axis('equal')
plt.title(' the distribution of population sizes separately in Zhejiang-neighbouring provinces')
plt.show()