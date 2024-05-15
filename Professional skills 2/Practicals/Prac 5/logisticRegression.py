import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
data = pd.read_csv("D:\Professional skills 2\Practicals\Prac 5\StudentData.csv")  
X = data[["gre", "gpa", "rank"]] 
y = data["admitted"]  

model = LinearRegression()

model.fit(X, y)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

X = sm.add_constant(X) 
m = sm.Logit(y, X).fit()
print("\n\n",m.summary(),"\n\n")

new_data = pd.DataFrame([[640, 4.25, 3]], columns=["gre", "gpa", "rank"])  
prediction = model.predict(new_data)
print("Predicted acceptance probability:", prediction[0])