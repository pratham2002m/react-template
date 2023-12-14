import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import probplot

# Load the Iris dataset
iris = sns.load_dataset("iris")

# a. Quantile plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 5))

# for column in iris.columns[:-1]:
#     sns.kdeplot(iris[column], cumulative=True, label=column)

sns.kdeplot(iris['sepal_length'], cumulative=True, label='sepal_length')

plt.title('Quantile Plot')
plt.xlabel('Values')
plt.ylabel('Cumulative Percentage')
plt.legend()
plt.show()

# b. Quantile-quantile (q-q) plot
plt.figure(figsize=(8, 8))
sns.set(style="whitegrid")

for column in iris.columns[:-1]:
    probplot(iris[column], plot=plt)

plt.title('Quantile-Quantile (Q-Q) Plot')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.show()

# c. Histogram
plt.figure(figsize=(12, 5))
sns.histplot(data=iris, x="sepal_length", bins=20, kde=True)
plt.title('Histogram for Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# d. Scatter plot
sns.set(style="whitegrid")
sns.FacetGrid(iris, hue="species", height=6) \
    .map(plt.scatter, "sepal_length", "sepal_width") \
    .add_legend()
plt.title('Scatter Plot for Sepal Length and Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# e. Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.title('Boxplot for Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.show()
