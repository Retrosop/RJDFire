import datetime
import pandas as pd

dataFile = pd.read_csv("firemap1.csv")[:100]
dfFire = dataFile[['Latitude', 'Longitude','Acq_date','Acq_time']]
dfFire['Acq_daten'] = 20000101
dfFire['Year'] = 2000
for index,row in dfFire.iterrows():
    date_string = str(row['Acq_date'])
    dfFire[index,'Acq_daten'] = datetime.datetime.strptime (date_string.removesuffix('.0'), '%Y%m%d')
    dfFire[index, 'Year'] = datetime.datetime.strptime (date_string.removesuffix('.0'), '%Y%m%d').year
print(dfFire)

# #https://python-lab.ru/metod-pandas-dataframe-count-v-python
# print(dfFire.count(axis='columns'))

# dfFire['Count_y'] = dfFire.groupby(y)['Date'].transform('size')
# print(dfFire)

print(dfFire.groupby(pd.PeriodIndex(dfFire['Acq_daten'], freq="M"))['Year'].count())
