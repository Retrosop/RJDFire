class Station:
  name = None
  region = None
  lon = 0.0
  lat = 0.0
  def __init__(self, n, s,lo,la):
        self.name = n
        self.region = s
        self.lon = lo
        self.lat = la

class Fire:
  lon  = None
  lat = None
  ploshad_les = None
  ploshad_neles = None

class Ote:
  id = None
  nomerkavartala = None
  namelesnichestva = None
  nameleshoza= None
  lon_center= None
  lat_center= None
  lesnoyfond = None
  nelesnoyfon= None   
  
listStation = []
listStation.append(Station("Урми", "ЕАо", 56.0, 45.8));
listStation.append(Station("Урми1", "ЕАо", 56.0, 45.8));
listStation.append(Station("Урми2", "ЕАо", 56.0, 45.8));
listStation.append(Station("Урми3", "ЕАо", 56.0, 45.8));
listStation.append(Station("Урми4", "ЕАо", 56.0, 45.8));
listStation.append(Station("Урми5", "ЕАо", 56.0, 45.8));

for s in listStation:
   print(s.name)

