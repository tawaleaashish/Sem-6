import pandas as pd

print("Section A: \n-----------\n")
mtcars = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\mtcars.csv')
print(f"Summary Statistics of mtcars dataset:\n{mtcars.describe()}")
print(f"\nStructure of mtcars dataset:")
mtcars.info()
print(f"\nHorse Power Quantile:\n{mtcars['hp'].quantile([0.25, 0.5, 0.75])}")

print("\n\nSection B: \n-----------")
cars = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\cars.csv')
print(f"Summary Statistics of cars dataset:\n{cars.describe()}")
print(f"\nStructure of cars dataset:")
cars.info()
print(f"\nQuantile of cars dataset:\n{cars['cyl'].quantile([0.25, 0.5, 0.75])}")