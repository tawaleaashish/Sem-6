import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\IRIS.csv')

X = df[['sepal_length', 'sepal_width']]
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
df['Cluster'] = kmeans.labels_

plt.figure(figsize=(8, 6))
plt.scatter(X['sepal_length'], X['sepal_width'], c=df['Cluster'], cmap='viridis')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title('Clustering of mtcars dataset based on sepal leangth and width by K-means')
plt.colorbar(label='Cluster')
plt.show()