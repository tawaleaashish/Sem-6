import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('D:\Professional skills 2\Practicals\Prac 1\mtcars.csv')

X = df[['mpg', 'hp']]
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
df['Cluster'] = kmeans.labels_

plt.figure(figsize=(8, 6))
plt.scatter(X['mpg'], X['hp'], c=df['Cluster'], cmap='viridis')
plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('Clustering of mtcars dataset based on mpg and hp by K-means')
plt.colorbar(label='Cluster')
plt.show()