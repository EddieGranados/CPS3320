import numpy as np  # numerical computation package
import pandas as pd  # dataframe
import matplotlib.pyplot as plt  # basic plotting package
import seaborn as sns  # more advanced graphing


#iris is a dataframe that we load the csv data read in from the URL into
iris = pd.read_csv("https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/iris.csv", index_col=0)
print(iris.head())
iris_rows100 = iris.loc[0:99]
print(iris_rows100.tail())
# plt.figure(figsize=(10, 5))


# Let us first grab the column names
column_names = [column for column in iris]  # list comprehension example


#Here is a way to find the maximum and minimum values the numerical data in a dataframe
#why, for example, the min() called twice?
mini = iris[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']].min().min()
maxi = iris[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']].max().max()

#line graph
# for i in range(0,4):
#         plt.plot(iris[column_names[i]])
# plt.ylim(mini,maxi)  #the plot limited to the range of the data - now you know why min and max were calculated
# plt.legend(['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'])  #makes it easier to read


##Another common but powerful display of data using box-and-whisker plots
# this does the job the box plots of all columns
# iris.boxplot(['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'])

#histogram
iris1 = iris.loc[:, :'Petal.Width']
# iris1.plot(kind='hist', bins=25, figsize=(10, 5))

#scatterplots
# iris1.plot.scatter('Sepal.Length', 'Petal.Length', figsize=(10, 6))

#regression line
sns.lmplot(data=iris, x='Sepal.Length', y='Petal.Length')
plt.show()

