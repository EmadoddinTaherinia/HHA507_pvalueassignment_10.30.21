import pandas as pd
import pandas._testing as tm
import scipy as sy
from scipy import stats
from scipy.stats import shapiro
from matplotlib import pyplot
from scipy.stats import spearmanr, pearsonr


dbdf = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv")

list(dbdf)

timeinhospital = dbdf['time_in_hospital']
sex = dbdf['gender']


### Q1: Sex or Gender is a nominal category and should be tested with Non-Parametic methods
sex_stat, sex_p = shapiro(sex)
print('statistics=%.3f, p=%.3f' % (stat, p))


### Q1: P-value for time in hospital is equall to 0.000 which means the null hypothesis is rejected and our distribution 
### is not normal, and we need to use Non-parametric tests.

timeinhospital_stat, timeinhospital_p = shapiro(timeinhospital)
print('statistics=%.3f, p=%.3f' % (timeinhospital_stat, timeinhospital_p))
 
pyplot.hist(timeinhospital).show

pearsonr(timeinhospital, sex)
spearmanr(timeinhospital, sex)


### Q2

CauAAdf = dbdf['race'] 
option=['AfricanAmerican', 'Caucasian']
CauAAdf1 = CauAAdf[CauAAdf['race'].isin(option)]







