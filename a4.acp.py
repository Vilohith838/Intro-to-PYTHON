import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

sns.set_theme(style="whitegrid")

# 1. Distribution Plot (Histogram + KDE)
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="sepal_length", kde=True, color="skyblue")
plt.title("Univariate Distribution of Sepal Length")
plt.show()

# 2. Scatter Plot (Relationship between two variables)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", style="species")
plt.title("Bivariate Relationship: Sepal Length vs Width")
plt.show()

# 3. Box Plot (Visualizing Statistical Outliers and Quartiles)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="species", y="petal_length", palette="Set2")
plt.title("Petal Length Distribution by Species")
plt.show()

# 4. Pair Plot (Matrix of all numerical relationships)
sns.pairplot(df, hue="species", corner=True)
plt.show()

# 5. Heatmap (Correlation Matrix)
plt.figure(figsize=(8, 6))
correlation_matrix = df.drop(columns='species').corr()
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu")
plt.title("Feature Correlation Heatmap")
plt.show()