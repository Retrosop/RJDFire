from dataclasses import field
import datetime 
import pandas as pd

class Fire:
    longitude = None
    latitude = None
    acq_daten = None
    idote = None
    rautomap = None
    rrailmap = None
    
    def __init__(self, longitude, latitude, acq_daten,idote,rautomap,rrailmap):
        self.longitude = longitude
        self.latitude = latitude
        self.acq_daten = acq_daten
        self.idote = idote
        self.rautomap = rautomap
        self.rrailmap = rrailmap
        
class FireMap:
        
    df = None
    def loadFire(self, countFire = None):
        if countFire != None:
            dataFile = pd.read_csv("firemapeao.csv")[:countFire]
        else:
            dataFile = pd.read_csv("firemapeao.csv")
            
        dfFire = dataFile[['Latitude', 'Longitude','Acq_date','Acq_time']]
        dfFire['Acq_daten'] = pd.to_datetime(dfFire['Acq_time'])
        dfFire['Year'] = 2000
        for index,row in dfFire.iterrows():
              date_string = str(row['Acq_date'])
              dfFire.at[index,'Acq_daten'] = datetime.datetime.strptime (date_string, '%Y%m%d')
              dfFire.at[index, 'Year'] = datetime.datetime.strptime (date_string, '%Y%m%d').year
        print(dfFire)
        self.df = dfFire
    def statFire(self):
        print('Статистика за день')
        print(self.df.groupby(pd.PeriodIndex(self.df['Acq_daten'], freq="D"))['Year'].count())
        print(self.df.groupby(pd.PeriodIndex(self.df['Acq_daten'], freq="M"))['Year'].count())
        print('Статистика за месяц')
        print(self.df.groupby(pd.PeriodIndex(self.df['Acq_daten'], freq="Y"))['Year'].count())
        print('Статистика за год')
    def saveStatFire(self):
        (self.df.groupby(pd.PeriodIndex(self.df['Acq_daten'], freq="D"))['Year'].count()).to_csv(f'fireday.csv', sep=";")
        (self.df.groupby(pd.PeriodIndex(self.df['Acq_daten'], freq="M"))['Year'].count()).to_csv(f'firemonth.csv', sep=";")
        (self.df.groupby(pd.PeriodIndex(self.df['Acq_daten'], freq="Y"))['Year'].count()).to_csv(f'fireyear.csv', sep=";")
        


def main():
    fireDB = FireMap()
    fireDB.loadFire()
    fireDB.statFire()
    fireDB.saveStatFire()

if __name__ == '__main__':
    main()