#4.1
a=5.08  #Population in 2004 (in millions)
b=5.33  #Population in 2014 (in millions)
c=5.55  #Population in 2024 (in millions)
d=b-a   
e=c-b
print(d)
print(e)

if d > e:
    print("Population growth is decelerating.")
else:
    print("The population growth is accelerating.")
# The population growth in Scotland is slowing down.
#4.2
X=True
Y=False
W=X and Y
#X=True and Y=False W=True
#X=True and Y=True W=False
#X=False and Y=True W=False
#X=False and Y=False W=False