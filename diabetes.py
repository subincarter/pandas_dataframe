import pandas as pd

read=pd.read_csv("diabetes.csv")
df=pd.DataFrame(read)
bmi=df[["BMI","Glucose","Age","BloodPressure"]]
empty=[]
print(bmi)
# pri=bmi.iloc[0,0]+bmi.iloc[1,1]

for index,col in bmi.iterrows():
    new=col["BMI"]+col["Glucose"]+col["Age"]+col["BloodPressure"]
    empty.append(new)
print(empty)


#     result=bmi.bmi.iloc[0,0]+bmi.iloc[1,1]
#     empty.append(result)
# print(empty)

# lucose=df[["Glucose"]]
# age=df[["Age"]]
# blood_pressure=df[["BloodPressure"]]







