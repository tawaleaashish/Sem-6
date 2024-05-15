import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\cars.csv')
cars.boxplot(by='manufacturer',column =['cyl'], grid = False) 
plt.show()
cars.plot(kind='scatter',x='manufacturer',y='cty')
plt.show()