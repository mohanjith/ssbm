import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# read data from xlsx file
df = pd.read_excel(
    'data/data.xlsx', sheet_name='COVID-19-geographic-disbtributi')


# create a world map of countries with sum of deaths, preserve popData2019
country_deaths = df.groupby('countryterritoryCode').sum().reset_index()[[
    'countryterritoryCode', 'deaths', 'popData2019']]

world_map = gpd.read_file("data/geo.json")
world_map = world_map.merge(
    country_deaths, left_on='adm0_iso', right_on='countryterritoryCode', how='left')
world_map['deaths'] = world_map['deaths'].fillna(0)
world_map['deathsPerCapita'] = world_map['deaths'] / world_map['popData2019']

# create two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10))

world_map.plot(column='deaths', cmap='Reds', linewidth=0.8,
               edgecolor='0.8', ax=ax1, legend=True)

ax1.set_title('COVID-19 total number of deaths by country')
ax1.set_axis_off()

world_map.plot(column='deathsPerCapita', cmap='Reds', linewidth=0.8,
               edgecolor='0.8', ax=ax2, legend=True)

ax2.set_title('COVID-19 total number of deaths per capita by country')
ax2.set_axis_off()

plt.tight_layout()
plt.savefig('images/country-cumulative-deaths.png', bbox_inches='tight')

# print max number of deaths per capita country
print(world_map[world_map['deathsPerCapita']
      == world_map['deathsPerCapita'].max()])

# print max number of deaths country
print(world_map[world_map['deaths'] == world_map['deaths'].max()])
