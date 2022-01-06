import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import pandas._testing as tm
import scipy as sy
from scipy import stats
from scipy.stats import shapiro
from matplotlib import pyplot
from scipy.stats import spearmanr, pearsonr


dbdf = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv")

list(dbdf)

timeinhospital = dbdf['time_in_hospital']

male = dbdf[dbdf['gender'] == 'Male']

w=0.4
x = ["timeinhospital"]
bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]

plt.bar(bar1,male,w,label="male")
plt.bar(bar2,female,w,label="female")

ttest_ind(female['time_in_hospital'], male['time_in_hospital'])

#Q1 Since P-value < 0.05 there is a significant difference between days in hospital for each group of men and women.
#Ttest_indResult(statistic=9.542637042242887, pvalue=1.4217299655114968e-21)


caucasian = dbdf[dbdf['race'] == 'Caucasian'] 
african_American = dbdf[dbdf['race'] == 'AfricanAmerican']

ttest_ind(caucasian['time_in_hospital'], african_American ['time_in_hospital'])

#Q2 There is a significant difference between two leveles(Africanamerican & Caucasian) and the days in hospital.
#Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)


asian = dbdf[dbdf['race'] == 'Asian']
african_American = dbdf[dbdf['race'] == 'AfricanAmerican']

ttest_ind(asian['time_in_hospital'], african_American ['time_in_hospital'])

#Q3 P-value < 0.05 reveals the significant difference between Asian and African American number of days in hospital
#Ttest_indResult(statistic=-4.193460125064539, pvalue=2.7592265975996794e-05)








