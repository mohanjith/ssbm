import pandas as pd
import matplotlib.pyplot as plt

# read data from xlsx file
df = pd.read_excel(
    'data/data.xlsx', sheet_name='COVID-19-geographic-disbtributi')

# replace _ with space
df['countriesAndTerritoriesHuman'] = df['countriesAndTerritories'].str.replace(
    '_', ' ')

# Find the highest daily number of new cases and the associated country and date
max_daily_cases = df.loc[df['cases'].idxmax()]

# Group the data by country and date to plot the time series for each country
df.groupby(['dateRep', 'countriesAndTerritoriesHuman']).sum().unstack().plot(
    y='cases')

# Highlight the date with the highest daily number of new cases
plt.axvline(max_daily_cases['dateRep'], color='red',
            linestyle='--', label='Highest daily cases')

# Set chart title and labels
plt.title('COVID-19 cases per day for each country')
plt.xlabel('Date')
plt.ylabel('Cases')

plt.annotate(f"{max_daily_cases['cases']} cases in {max_daily_cases['countriesAndTerritoriesHuman']} on {max_daily_cases['dateRep'].strftime('%Y-%m-%d')}", xy=(
    max_daily_cases['dateRep'], max_daily_cases['cases']))

# Display the legend
plt.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), ncol=3).set_in_layout(True)

plt.tight_layout()

plt.savefig('images/country-case-trend.png', bbox_inches='tight')

# Print the date with the highest daily number of new cases and the associated country
print(
    f"The highest daily number of new cases was on {max_daily_cases['dateRep'].strftime('%Y-%m-%d')} in {max_daily_cases['countriesAndTerritoriesHuman']} with {max_daily_cases['cases']} cases.")
