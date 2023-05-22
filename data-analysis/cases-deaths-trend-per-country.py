import sys
import pandas as pd
import matplotlib.pyplot as plt

# read data from xlsx file
df = pd.read_excel(
    'data/data.xlsx', sheet_name='COVID-19-geographic-disbtributi')

# function to plot cases and deaths per day for given country


def plot_cases(country1, country2):
    data1 = df[df['countriesAndTerritories'] ==
               country1][df['cases'] >= 0][df['deaths'] >= 0]
    data1['casesPerCapita'] = data1['cases'] / data1['popData2019']
    data1['deathsPerCapita'] = data1['deaths'] / data1['popData2019']

    data2 = df[df['countriesAndTerritories'] ==
               country2][df['cases'] >= 0][df['deaths'] >= 0]
    data2['casesPerCapita'] = data2['cases'] / data2['popData2019']
    data2['deathsPerCapita'] = data2['deaths'] / data2['popData2019']

    plt.plot(data1['dateRep'], data1['casesPerCapita'],
             label=f'Cases {country1}')
    plt.plot(data1['dateRep'], data1['deathsPerCapita'],
             label=f'Deaths {country1}')
    plt.plot(data2['dateRep'], data2['casesPerCapita'],
             label=f'Cases {country2}')
    plt.plot(data2['dateRep'], data2['deathsPerCapita'],
             label=f'Deaths {country2}')

    plt.legend()

    plt.title(
        f'COVID-19 cases and deaths per capita per day in {country1} and {country2}')
    plt.xlabel('Date')
    plt.tight_layout()
    plt.savefig(
        f'images/{country1}-{country2}-cases-trend.png', bbox_inches='tight')


plot_cases(sys.argv[1], sys.argv[2])
