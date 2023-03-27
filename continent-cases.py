import pandas as pd
import matplotlib.pyplot as plt

# read data from xlsx file
df = pd.read_excel(
    'data/data.xlsx', sheet_name='COVID-19-geographic-disbtributi')

# Plot cases per day for each continent and save to png file
df.groupby(['dateRep', 'continentExp']).sum().unstack().plot(
    y='cases')

plt.title('COVID-19 cases per day for each continent')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend(title='Continent')
plt.tight_layout()
plt.savefig('images/continent-case-trend.png', bbox_inches='tight')
