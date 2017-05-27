# From this website http://machinelearningmastery.com/quick-and-dirty-data-analysis-with-pandas/
# Load data
import pandas as pd
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('pima-indians-diabetes.data', names=names)
# Describe data
print(data)
print("Data describe:\n",data.describe())

# Feature distribution
import matplotlib.pyplot as plt
data.boxplot()
#plt.show()
data.hist()
#plt.show()

# Feature-Class relationships
data.groupby('class').hist()
#plt.show()
data.groupby('class').plas.hist(alpha=0.4)
#plt.show()

# Feature-Feature relationships
from pandas import DataFrame
from pandas.plotting import scatter_matrix
df = DataFrame(data, columns=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
plt.show()
