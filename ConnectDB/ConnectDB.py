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
listStation.append(Station("Архара", "Амурская обл.", 49.420501, 130.075086));
listStation.append(Station("о.п. Карьерный", "Амурская обл.", 49.386809, 130.104437));
listStation.append(Station("о.п. 8088 км", "Амурская обл.", 49.370273, 130.139846));
listStation.append(Station("Татакан", "Амурская обл.", 49.348907, 130.160364));
listStation.append(Station("о.п. Каменный карьер", "Амурская обл.", 49.318027, 130.188621));
listStation.append(Station("Богучан", "Амурская обл.", 49.284290, 130.260611));
listStation.append(Station("Рачи", "Амурская обл.", 49.265495, 130.361914));
listStation.append(Station("Урил", "Амурская обл.", 49.229035, 130.478107));
listStation.append(Station("Тарманчукан", "Амурская обл.", 49.194913, 130.658895));
listStation.append(Station("о.п. Тоннельный", "Амурская обл.", 49.164833, 130.713425));
listStation.append(Station("о.п. Касаткин", "Амурская обл.", 49.157417, 130.735151));
listStation.append(Station("Кундур", "Амурская обл.", 49.107741, 130.755188));
listStation.append(Station("Казачий", "Амурская обл.", 49.054096, 130.825799));
listStation.append(Station("о.п. 8166 км", "Амурская обл.", 49.047496, 130.851235));
listStation.append(Station("о.п. Есауловка", "Амурская обл.", 49.047496, 130.851235));
listStation.append(Station("Ядрин", "Амурская обл.", 48.977517, 131.021402));
listStation.append(Station("Облучье", "ЕАО", 49.011088, 131.059552));
listStation.append(Station("Ударный", "ЕАО", 49.011088, 131.059552));
listStation.append(Station("Лагар-Аул", "ЕАО", 49.006014, 131.232914));
listStation.append(Station("Кимкан", "ЕАО", 48.989314, 131.419661));
listStation.append(Station("о.п. Снарский", "ЕАО", 48.990038, 131.514409));
listStation.append(Station("Известковая", "ЕАО", 48.983540, 131.556847));
listStation.append(Station("о.п. Двуречье", "ЕАО", 48.983540, 131.556847));
listStation.append(Station("Биракан", "ЕАО", 48.983540, 131.556847));
listStation.append(Station("Тёплое Озеро", "ЕАО", 49.001678, 131.880888));
listStation.append(Station("Известковый Завод", "ЕАО", 49.001678, 131.880888));
listStation.append(Station("Лондоко", "ЕАО", 49.001678, 131.880888));
listStation.append(Station("о.п. Кандалик", "ЕАО", 49.001678, 131.880888));
listStation.append(Station("Будукан", "ЕАО", 49.001678, 131.880888));
listStation.append(Station("о.п. Бобровский", "ЕАО", 49.021524, 132.347431));
listStation.append(Station("Бира", "ЕАО", 49.000080, 132.463185));
listStation.append(Station("Семисточный", "ЕАО", 48.960709, 132.567188));
listStation.append(Station("о.п. Трек", "ЕАО", 48.960709, 132.567188));
listStation.append(Station("Кирга", "ЕАО", 48.960709, 132.567188));
listStation.append(Station("Биробиджан-1", "ЕАО", 48.792982, 132.934532));
listStation.append(Station("Икура", "ЕАО", 48.792982, 132.934532));
listStation.append(Station("о.п. Усов Балаган", "ЕАО", 48.792982, 132.934532));
listStation.append(Station("Аур", "ЕАО", 48.792982, 132.934532));
listStation.append(Station("о.п. Оль", "ЕАО", 48.792982, 132.934532));
listStation.append(Station("о.п. Белгородское", "ЕАО", 48.792982, 132.934532));
listStation.append(Station("Ин", "ЕАО", 48.594397, 133.814051));
listStation.append(Station("о.п. Урми", "ЕАО", 48.594746, 133.979384));
listStation.append(Station("Ольгохта", "ЕАО", 48.594746, 133.979384));
listStation.append(Station("о.п. Лумку-Корани", "ЕАО", 48.603188, 134.313587));
listStation.append(Station("о.п. Поперечка", "ЕАО", 48.603188, 134.313587));
listStation.append(Station("Волочаевка-1", "ЕАО", 48.603188, 134.313587));
listStation.append(Station("Тунгусский", "ЕАО", 48.603188, 134.313587));
listStation.append(Station("Дежневка", "ЕАО", 48.535558, 134.627437));
listStation.append(Station("о.п. Совхозное", "ЕАО", 48.535558, 134.627437));
listStation.append(Station("о.п. Ключевое", "ЕАО", 48.535558, 134.627437));
listStation.append(Station("Николаевка", "ЕАО", 48.531121, 134.772767));
listStation.append(Station("о.п. Энтузиастов", "ЕАО", 48.531121, 134.772767));
listStation.append(Station("Приамурская", "ЕАО", 48.531121, 134.772767));
listStation.append(Station("Покровский", "ЕАО", 48.527224, 134.944256));
listStation.append(Station("о.п. Тельман", "ЕАО", 48.527224, 134.944256));
listStation.append(Station("Хабаровск-1", "Хабаровский край", 48.496899, 135.072946));
listStation.append(Station("о.п. Хехцир", "Хабаровский край", 48.294248, 135.097197));
listStation.append(Station("о.п. 8557 км", "Хабаровский край", 48.253603, 135.072433));
listStation.append(Station("Корфовская", "Хабаровский край", 48.253603, 135.072433));
listStation.append(Station("о.п. Чирки", "Хабаровский край", 48.166062, 135.118578));
listStation.append(Station("о.п. 8571 км", "Хабаровский край", 48.166062, 135.118578));
listStation.append(Station("Кругликово", "Хабаровский край", 48.166062, 135.118578));
listStation.append(Station("о.п. Зоевка", "Хабаровский край", 48.055402, 135.098783));
listStation.append(Station("Верино", "Хабаровский край", 48.166062, 135.118578));
listStation.append(Station("Хор", "Хабаровский край", 48.055402, 135.098783));
listStation.append(Station("Хака", "Хабаровский край", 47.842123, 134.944162));
listStation.append(Station("Дормидонтовка", "Хабаровский край", 47.842123, 134.944162));
listStation.append(Station("о.п. Дубки", "Хабаровский край", 47.718930, 134.906241));
listStation.append(Station("Красицкий", "Хабаровский край", 47.718930, 134.906241));
listStation.append(Station("о.п. Садовый", "Хабаровский край", 47.553010, 134.806123));
listStation.append(Station("Вяземская", "Хабаровский край", 47.553010, 134.806123));
listStation.append(Station("Биробиджан-2", "ЕАО", 48.758353, 132.895281));
listStation.append(Station("Бирофельд", "ЕАО", 48.437892, 132.707133));
listStation.append(Station("Опытное поле", "ЕАО", 48.403143, 132.686943));
listStation.append(Station("Красивое", "ЕАО", 48.286517, 132.530145));
listStation.append(Station("Лазарево", "ЕАО", 48.239542, 132.448930));
listStation.append(Station("Унгун", "ЕАО", 48.214700, 132.407300));
listStation.append(Station("Бабстово", "ЕАО", 48.124253, 132.430337));
listStation.append(Station("Ленинск", "ЕАО", 47.987088, 132.616802));


for s in listStation:
   print(s.name)

