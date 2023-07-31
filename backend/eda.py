#file: 0XY_healthcare_data_analysis/backend/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
  df = pd.read_csv(file_path)
  return df

def convert_binary_to_numerical(df):
  # convert datatype from binary to numerical
  # each unique value is assigned as integer value using map function.
  df['SEX'] = df['SEX'].map({'F': 0, 'M': 1})
  df['SOURCE'] = df['SOURCE'].map({'out': 0, 'in': 1})
  return df

# examining the basic statistic of the dataset is done. 
#EDA, visualise the data to understand the distributions of individual variables 
# and relationships between different part of variables.abs

def plot_age_histogram(df):
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
def plot_haematocrit_boxplot(df):
  plt.figure(figsize = (8, 6))
  sns.boxplot(df['HAEMATOCRIT'])
  plt.xlabel('HAEMATOCRIT')
  plt.ylabel('Value')
  plt.title('HAEMATOCRIT Box Plot')
  plt.grid(True)
  plt.savefig('heametocrit_boxplot.png')
  plt.show()
  
def identify_outliers(df, column):
  #check outliers
  Q1 = df[column].quantile(0.25)
  Q3 = df[column].quantile(0.75)
  IQR = Q3 - Q1
  #any data point falls below or above is a potential outliers
  outliers = df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]
  
  if outliers.empty:
    print("No outliers found.")
    return pd.DataFrame(columns = [column])
  else:
    print("Potential outliers:")
    print(outliers)
    return(outliers)
  
#scatter plots HAEMATOCRIT and HAEMOGLOBINS
def plot_haematocrit_vs_haemoglobins_scatter(df):
  plt.figure(figsize = (8, 6))
  plt.scatter(df['HAEMATOCRIT'], df['HAEMOGLOBINS'])
  plt.xlabel('HAEMATOCRIT')
  plt.ylabel('HAEMOGLOBINS')
  plt.title('HAEMATOCRIT_VS_HAEMOGLOBINS Scatter Plot')
  plt.grid(True)
  plt.savefig('haematocrit_vs_haemoglobins_scatter.png')
  plt.show()

#correlation matrix
def plot_correlation_matrix(df):
  corr_matrix = df.corr()
  print(corr_matrix)
  
  plt.figure(figsize = (10, 8))
  sns.heatmap(df.corr(), annot = True, fmt = ".2f")
  plt.title('Correlation Matrix')
  plt.savefig('correlation_matrix.png')
  plt.show()
  
def analyse(df, column):
  if column in df.columns:
    min_val = df[column].min()
    max_val = df[column].max()
    mean_val = df[column].mean()
    return pd.DatFrame({
      f'min_{column}': [min_val],
      f'max_{column}': [max_val],
      f'mean_{column}': [mean_val]
    })
  else:
    print(f"Column '{column}' not found inthe dataframe.")
    return pd.DataFrame()
      
if __name__ == '__main__':
  data_file_path = 'data-ori.csv'
  df = load_data(data_file_path)
  df = convert_binary_to_numerical(df)

  print(df.head())
  print(df.tail())
  print(df.columns)
  print(df.isnull().sum())
  #check which columns in df are binary
  binary_cols = [col for col in df.columns if df[col].nunique() == 2]
  print(binary_cols)
  # see basic stat
  print(df.describe())
  
  plot_age_histogram(df)
  plot_haematocrit_boxplot(df)
  outliers = identify_outliers(df, 'HAEMATOCRIT')
  print("Potential outliers:")
  print(outliers)
  plot_haematocrit_vs_haemoglobins_scatter(df)
  plot_correlation_matrix(df)
  
  #violin plot
  column_to_analyse = 'HAEMATOCRIT'
  outliers = identify_outliers(df, column_to_analyse)
  plt.figure(figsize = (10, 6))
  sns.violinplot(x = df[column_to_analyse])
  plt.title(f'Violoin plot of of {column_to_analyse}')
  plt.show()