W=input("请输入你的体重")
H=input("请输入你的身高")
W=float(W)
H=float(H)
BMI=W/H**2
print("my BMI is ",BMI)
if BMI>30:
    print("肥胖")
if 18.5<=BMI<=30:
    print("体重正常")
if BMI<18.5:
    print("体重不足")