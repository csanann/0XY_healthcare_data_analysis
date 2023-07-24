<!-- file: 0XY_healthcare_data_analysis/eda_report.md -->

## Exploratory Data Analysis Report

1. Binary to Numerical Conversion

The conversion as successfully done by using 'convert_binary_to_numerical' function, to convert binary categorical variables into numerical ones. It was done for 'SEX' and 'SOURCE' columns with 'F' and 'out' mapped to '0', and 'M' and 'in' being mapped to '1'.

2. Outlier Detection

We looked for outliers by using the 'identify_outliers' function, boxplot and violin plot, which are numbers that are much higher and lower than the rest. The finding shows no outliers.

3. Visulisations

The histogram of 'HAEMATOCRIT' shows that the data is skewed to the right, indicating that most patients have a lower haematocrit value, with a few patients having significantly higher values.

The scatter plot of 'HAEMATOCRIT' against 'SEX' shows on clear relationship between the two variables, suggesting that sex may not be a significant factor in determining a patient's heamatocrit level.

The boxplot and violin plot of 'HAEMATOCRIT' also confirmed there are no outliers with several points falling outside the interquartile range.
