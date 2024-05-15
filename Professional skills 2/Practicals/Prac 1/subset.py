import pandas as pd

iris_df = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\IRIS.csv')

subset_condition = iris_df['sepal_length'] > 7
subset_df = iris_df[subset_condition]
print("Subset of the Iris dataset with sepal length greater than 7:")
print(subset_df)

aggregated_result = iris_df.groupby('species').agg({
    'sepal_length': 'mean',
    'sepal_width': 'mean',
    'petal_length': 'mean',
    'petal_width': 'mean'
})

print("\nAggregated result by species:")
print(aggregated_result)