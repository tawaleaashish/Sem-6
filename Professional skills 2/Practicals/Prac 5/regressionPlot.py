import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the data is stored in a file named "student_data.csv"
data = pd.read_csv("D:\Professional skills 2\Practicals\Prac 5\StudentData.csv")

# Plot scatter plot with linear regression line
sns.lmplot(x='gre', y='gpa',z='rank', hue='admitted', data=data, logistic=False, scatter_kws={"s": 50})
plt.title('Linear Regression: GRE Score and GPA vs. Admitted')
plt.xlabel('GRE Score')
plt.ylabel('GPA')
plt.show()
