# SSBM
eMBA data projects

## Prequisite

* Python
* pip

## Preparation

1. Remember to place the Excel file with the data in data directory named data.xlsx.
2. Intall required Python libraries

```
pip install -r requirements.txt
```


## Usage
### Total cases and deaths by country
```
LC_TIME=en_GB.UTF-8 python3 country-cumulative-cases.py
LC_TIME=en_GB.UTF-8 python3 country-cumulative-deaths.py
```
### 1. Do the curves of cases and deaths have an upward trend globally?

```
LC_TIME=en_GB.UTF-8 python3 cases-deaths-trend.py
```
### 2. Does any continent have a distinct ascending curve of cases?
```
LC_TIME=en_GB.UTF-8 python3 continent-cases.py
```
### 3. What date was noted with the highest daily number of new cases? In which country?
```
LC_TIME=en_GB.UTF-8 python3 country-cases.py
```
### 4. Does the epidemiological situation in France differ in comparison to Cuba?
```
LC_TIME=en_GB.UTF-8 python3 cases-deaths-trend-per-country.py France Cub
```
