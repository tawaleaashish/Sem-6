import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\cars.csv')
mtcars = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\mtcars.csv')
plt.hist(mtcars["hp"],bins=5,color='skyblue', edgecolor='black')
plt.title("Horse-Power of Cars")
plt.show()
plt.bar(cars["manufacturer"],cars["cyl"],color='skyblue', edgecolor='black')
plt.ylabel("No. of cylinders")
plt.xlabel("Manufacturer")
plt.show()
plt.pie(cars["class"].value_counts(),labels=["suv","compact","midsize","subcompact","pickup","minivan","2seater"])
plt.show()