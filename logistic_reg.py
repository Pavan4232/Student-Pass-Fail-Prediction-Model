import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data=pd.read_excel(r"C:\Users\pavan\Downloads\student_pass_fail_dataset.xlsx")
x=data[["StudyHours","Attendance","PreviousScore"]]
y=data["Pass"]
model=LogisticRegression()
# print(data)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
model.fit(x_train,y_train)
abc=model.predict(x_test)
ac=accuracy_score(y_test,abc)
newdata=[[2.6,55,70]]
predictedvalue=model.predict(newdata)
prob=model.predict_proba(newdata)[0]
fail_per=prob[0] * 100
pass_per=prob[1] * 100
print(prob,"prob")
print(predictedvalue,"predictvalue")
print(round(fail_per,2),"failper")
print(round(pass_per,2),"passper")
# print(ac)