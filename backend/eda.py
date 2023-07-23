#file: 0XY_healthcare_data_analysis/backend/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data-ori.csv')

print(df.head())
print(df.tail())
print(df.columns)
print(df.isnull().sum())

#check which columns in df are binary
binary_cols = [col for col in df.columns if df[col].nunique() == 2]
print(binary_cols)

# we have to convert datatype from binary to numerical
# each unique value is assigned as integer value using map function.
df['SEX'] = df['SEX'].map({'F': 0, 'M': 1})
df['SOURCE'] = df['SOURCE'].map({'out': 0, 'in': 1})

# see basic stat
print(df.describe())

# examining the basic statistic of the dataset is done. 
#EDA, visualise the data to understand the distributions of individual variables 
# and relationships between different part of variables.abs

#histograms AGE
plt.figure(figsize = (8, 6))
plt.hist(df['AGE'], bins = 20, color = 'skyblue', edgecolor = 'black' )
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.grid(True)
plt.savefig('age_histograme.png')
plt.show()

#Box plots HAEMATOCRIT

#scatter plots HAEMATOCRIT and HAEMOGLOBINS

#correlation matrix