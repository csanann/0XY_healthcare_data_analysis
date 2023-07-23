<!-- file: 0XY_healthcare_data_analysis/eda_report.md -->
## Age Distribution Analysis

The histogram below shows the age distribution of patients in the dataset. The age ranges have been grouped as follows:

- 0-20 age range: Approximately 115 patients in the dataset are between the ages of 0 and 20. This represents a relatively smaller number of patients in this age group compared to other age ranges.

- 20-40 age range: Over 300 patients in the dataset fall within the ages of 20 and 40. This indicates a higher number of patients in this age group compared to the younger age range (0-20).

- 40-60 age range: There are less than 300 patients in the dataset who are between the ages of 40 and 60. The number of patients starts to decrease in this age range compared to the 20-40 age group.

- 60-80 age range: There is a gradual decrease in frequency from around 350 patients between the ages of 60 and 70 to around 200 patients between 70 and 80. The frequency decreases as the age increases, indicating fewer patients in the older age range.

- 80-100 age range: The frequency sharply declines from 150 to 0, indicating that there are very few patients in the dataset who are between the ages of 80 and 100.

Overall, the histogram reveals a higher concentration of patients in the middle age groups (20-60) and a decline in the number of patients as the age increases beyond 60. The dataset appears to have fewer patients in the very young and very old age groups.

Further analysis will be conducted to explore relationships between age and other variables in the dataset.

# Since, blood test could help us to understand the distribution of the results in the dataset such as (HAEMATOCRIT, HAEMOGLOBINS, ERYTHROCYTE, LEUCOCYTE, THROMBOCYTE, MCH, MCHC, MCV)

we use seaborn to create visualisation histograms.