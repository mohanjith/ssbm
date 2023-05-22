import pandas as pd
import matplotlib.pyplot as plt

# read data from xlsx file
df = pd.read_excel(
    'data/data.xlsx', sheet_name='COVID-19-geographic-disbtributi')

# plot cases and deaths per day globally and save to png file
df.groupby('dateRep').sum().plot(y=['cases', 'deaths'])

plt.title('COVID-19 cases and deaths per day globally')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('images/cases-deaths-trend.png', bbox_inches='tight')
