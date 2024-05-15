import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\cars.csv')
plt.scatter(cars["manufacturer"], cars["displ"], color="black", label="All")
plt.show()