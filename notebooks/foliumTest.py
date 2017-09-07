import folium
import vincent
import random
import json
from pprint import pprint

import pandas as pd


her_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
her_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
her_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
her_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

her_data = [her_1, her_2, her_3, her_4]
her_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_her = pd.DataFrame(her_data, index=her_index)


agNik_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
agNik_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
agNik_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
agNik_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

agNik_data = [agNik_1, agNik_2, agNik_3, agNik_4]
agNik_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_agNik = pd.DataFrame(agNik_data, index=agNik_index)

sitia_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
sitia_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
sitia_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
sitia_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

sitia_data = [sitia_1, sitia_2, sitia_3, sitia_4]
sitia_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_sitia = pd.DataFrame(sitia_data, index=sitia_index)

kalyves_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
kalyves_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
kalyves_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
kalyves_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

kalyves_data = [kalyves_1, kalyves_2, kalyves_3, kalyves_4]
kalyves_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_kalyves = pd.DataFrame(kalyves_data, index=kalyves_index)

rethymno_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
rethymno_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
rethymno_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
rethymno_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

rethymno_data = [rethymno_1, rethymno_2, rethymno_3, rethymno_4]
rethymno_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_rethymno = pd.DataFrame(rethymno_data, index=rethymno_index)

chania_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
chania_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
chania_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
chania_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

chania_data = [chania_1, chania_2, chania_3, chania_4]
chania_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_chania = pd.DataFrame(chania_data, index=chania_index)

platanias_1 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
platanias_2 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
platanias_3 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }
platanias_4 = {'Kastration': random.randint(90,290), 'Weitere Operationen': random.randint(10,70) }

platanias_data = [platanias_1, platanias_2, platanias_3, platanias_4]
platanias_index = ['Katze (weiblich)', 'Katze (männlich)', 'Hund (weiblich)', 'Hund (männlich)']
df_platanias = pd.DataFrame(platanias_data, index=platanias_index)

"""
Getting to where I want

"""

heraklion = vincent.StackedBar(df_her)
heraklion.axis_titles(x='Tierarten', y='Anzahl Operationen')
heraklion.legend(title='Heraklion')
heraklion.scales['x'].padding = 0.2
heraklion.colors(brew='Pastel1')
heraklion.width = 350
heraklion.height = 200


agiosNikolaos = vincent.StackedBar(df_her)
agiosNikolaos.axis_titles(x='Tierarten', y='Anzahl Operationen')
agiosNikolaos.legend(title='Agios Nikolaos')
agiosNikolaos.scales['x'].padding = 0.2
agiosNikolaos.colors(brew='Pastel1')
agiosNikolaos.width = 350
agiosNikolaos.height = 200


sitia = vincent.StackedBar(df_sitia)
sitia.axis_titles(x='Tierarten', y='Anzahl Operationen')
sitia.legend(title='Sitia')
sitia.scales['x'].padding = 0.2
sitia.colors(brew='Pastel1')
sitia.width = 350
sitia.height = 200

kalyves = vincent.StackedBar(df_kalyves)
kalyves.axis_titles(x='Tierarten', y='Anzahl Operationen')
kalyves.legend(title='kalyves')
kalyves.scales['x'].padding = 0.2
kalyves.colors(brew='Pastel1')
kalyves.width = 350
kalyves.height = 200

rethymno = vincent.StackedBar(df_rethymno)
rethymno.axis_titles(x='Tierarten', y='Anzahl Operationen')
rethymno.legend(title='rethymno')
rethymno.scales['x'].padding = 0.2
rethymno.colors(brew='Pastel1')
rethymno.width = 350
rethymno.height = 200

chania = vincent.StackedBar(df_chania)
chania.axis_titles(x='Tierarten', y='Anzahl Operationen')
chania.legend(title='chania')
chania.scales['x'].padding = 0.2
chania.colors(brew='Pastel1')
chania.width = 350
chania.height = 200

platanias = vincent.StackedBar(df_platanias)
platanias.axis_titles(x='Tierarten', y='Anzahl Operationen')
platanias.legend(title='platanias')
platanias.scales['x'].padding = 0.2
platanias.colors(brew='Pastel1')
platanias.width = 350
platanias.height = 200

kreta = folium.Map(location=[35.3220, 25.1001],
                   tiles="Stamen Terrain",
                   zoom_start=8)

popup1 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(heraklion, width=500, height=250))

popup2 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(agiosNikolaos, width=500, height=250))

popup3 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(sitia, width=500, height=250))

popup4 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(kalyves, width=500, height=250))

popup5 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(rethymno, width=500, height=250))

popup6 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(chania, width=500, height=250))

popup7 = folium.Popup(max_width=800,
                     ).add_child(folium.Vega(platanias, width=500, height=250))

# folium.Marker([35.517583, 23.905217], popup='Platanias').add_to(kreta)
# folium.Marker([35.512933, 24.027401], popup='Chania').add_to(kreta)
# folium.Marker([35.452198, 24.171107], popup='Kalyves').add_to(kreta)
# folium.Marker([35.363304, 24.481352], popup='Rethymno').add_to(kreta)
# folium.Marker([35.3220, 25.1001], popup="Heraklion").add_to(kreta)
# folium.Marker([35.1813, 25.6986], popup='Agios Nikolaos').add_to(kreta)
# folium.Marker([35.198516, 26.077081], popup='Sitia').add_to(kreta)

# Platanias Marker
folium.RegularPolygonMarker(location=[35.517583, 23.905217],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup7).add_to(kreta)

# Chania Marker
folium.RegularPolygonMarker(location=[35.512933, 24.027401],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup6).add_to(kreta)

# Kalyves Marker
folium.RegularPolygonMarker(location=[35.452198, 24.171107],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup5).add_to(kreta)

# Rethymno Marker
folium.RegularPolygonMarker(location=[35.363304, 24.481352],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup4).add_to(kreta)


# Heraklion Marker
folium.RegularPolygonMarker(location=[35.325723, 25.134040],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup1).add_to(kreta)

#Agios Nikolaos Marker
folium.RegularPolygonMarker(location=[35.192464, 25.706721],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup2).add_to(kreta)

#Sitia Marker
folium.RegularPolygonMarker(location=[35.198516, 26.077081],
                    fill_color = '#43d9de',
                    radius = 10,
                    number_of_sides = 3,
                    rotation = -90,
                    weight = 1,
                    popup=popup3).add_to(kreta)

#
#Click Marker
folium.ClickForMarker()

kreta.save("../figures/kreta.html")
