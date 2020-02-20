```python
%load_ext autoreload
from src.data import stocks
```


```python
API_KEY = "9868196c4e3cef02ebb3ec9af04db1038f741599"
```


```python
from datetime import datetime
datetime(1990,1,1).strftime("%Y-%m-%d")
```




    '1990-01-01'




```python
%autoreload 2
from src.data import tiingo_api, stocks

#data = tiingo_api.get_historical_data("SPY", API_KEY)
data = stocks.get_historical_data("SPY", API_KEY)
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
      <th>adjusted close</th>
      <th>adjusted high</th>
      <th>adjusted low</th>
      <th>adjusted open</th>
      <th>adjusted volume</th>
      <th>dividend amount</th>
      <th>splitFactor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-02-20</th>
      <td>336.9500</td>
      <td>338.6400</td>
      <td>333.6817</td>
      <td>337.7423</td>
      <td>71271706</td>
      <td>336.950000</td>
      <td>338.640000</td>
      <td>333.681700</td>
      <td>337.742300</td>
      <td>71271706</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-19</th>
      <td>338.3400</td>
      <td>339.0800</td>
      <td>337.4800</td>
      <td>337.7900</td>
      <td>48587393</td>
      <td>338.340000</td>
      <td>339.080000</td>
      <td>337.480000</td>
      <td>337.790000</td>
      <td>48587393</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-18</th>
      <td>336.7300</td>
      <td>337.6677</td>
      <td>335.2100</td>
      <td>336.5100</td>
      <td>57195407</td>
      <td>336.730000</td>
      <td>337.667700</td>
      <td>335.210000</td>
      <td>336.510000</td>
      <td>57195407</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-14</th>
      <td>337.6000</td>
      <td>337.7300</td>
      <td>336.2000</td>
      <td>337.5100</td>
      <td>64518123</td>
      <td>337.600000</td>
      <td>337.730000</td>
      <td>336.200000</td>
      <td>337.510000</td>
      <td>64518123</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-13</th>
      <td>337.0600</td>
      <td>338.1200</td>
      <td>335.5600</td>
      <td>335.8621</td>
      <td>54038002</td>
      <td>337.060000</td>
      <td>338.120000</td>
      <td>335.560000</td>
      <td>335.862100</td>
      <td>54038002</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1993-02-04</th>
      <td>45.0000</td>
      <td>45.0937</td>
      <td>44.4687</td>
      <td>44.9687</td>
      <td>531500</td>
      <td>27.096382</td>
      <td>27.152803</td>
      <td>26.776464</td>
      <td>27.077535</td>
      <td>531500</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1993-02-03</th>
      <td>44.8125</td>
      <td>44.8437</td>
      <td>44.3750</td>
      <td>44.4062</td>
      <td>529400</td>
      <td>26.983481</td>
      <td>27.002268</td>
      <td>26.720044</td>
      <td>26.738831</td>
      <td>529400</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1993-02-02</th>
      <td>44.3437</td>
      <td>44.3750</td>
      <td>44.1250</td>
      <td>44.2187</td>
      <td>201300</td>
      <td>26.701197</td>
      <td>26.720044</td>
      <td>26.569508</td>
      <td>26.625929</td>
      <td>201300</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1993-02-01</th>
      <td>44.2500</td>
      <td>44.2500</td>
      <td>43.9687</td>
      <td>43.9687</td>
      <td>480500</td>
      <td>26.644776</td>
      <td>26.644776</td>
      <td>26.475394</td>
      <td>26.475394</td>
      <td>480500</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1993-01-29</th>
      <td>43.9375</td>
      <td>43.9687</td>
      <td>43.7500</td>
      <td>43.9687</td>
      <td>1003200</td>
      <td>26.456607</td>
      <td>26.475394</td>
      <td>26.343705</td>
      <td>26.475394</td>
      <td>1003200</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>6814 rows × 12 columns</p>
</div>




```python
%autoreload 2
from src.data import stocks
from src.analysis import returns

returns.get_returns_by_year(data, minimum_nr_of_months=None, in_percentage=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>adjusted open</th>
      <th>adjusted close</th>
      <th>growth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020</th>
      <td>323.54</td>
      <td>336.95</td>
      <td>0.0414477</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>241.413</td>
      <td>321.86</td>
      <td>0.333236</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>257.934</td>
      <td>245.28</td>
      <td>-0.0490628</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>212.593</td>
      <td>256.991</td>
      <td>0.208837</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>185.414</td>
      <td>211.167</td>
      <td>0.138895</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>186.969</td>
      <td>188.54</td>
      <td>0.0084017</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>163.484</td>
      <td>186.208</td>
      <td>0.139</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>126.393</td>
      <td>164.114</td>
      <td>0.298449</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>108.865</td>
      <td>124.041</td>
      <td>0.139398</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>105.759</td>
      <td>106.94</td>
      <td>0.0111594</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>91.9834</td>
      <td>104.958</td>
      <td>0.141054</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>72.3488</td>
      <td>91.2221</td>
      <td>0.260866</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>114.487</td>
      <td>72.1888</td>
      <td>-0.369459</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>109.179</td>
      <td>114.237</td>
      <td>0.0463323</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>94.2369</td>
      <td>108.711</td>
      <td>0.153588</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>89.9853</td>
      <td>93.7924</td>
      <td>0.0423079</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>81.1582</td>
      <td>89.4745</td>
      <td>0.10247</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>63.5</td>
      <td>80.8241</td>
      <td>0.272821</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>80.98</td>
      <td>63.0569</td>
      <td>-0.221328</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>91.6915</td>
      <td>80.4172</td>
      <td>-0.122959</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>101.894</td>
      <td>91.1271</td>
      <td>-0.105665</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>83.8956</td>
      <td>100.949</td>
      <td>0.203266</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>65.3282</td>
      <td>83.8531</td>
      <td>0.283567</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>49.1686</td>
      <td>65.1604</td>
      <td>0.325245</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>39.7826</td>
      <td>48.8173</td>
      <td>0.227102</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>28.9484</td>
      <td>39.8332</td>
      <td>0.376005</td>
    </tr>
    <tr>
      <th>1994</th>
      <td>28.7439</td>
      <td>28.8594</td>
      <td>0.00401867</td>
    </tr>
    <tr>
      <th>1993</th>
      <td>26.4754</td>
      <td>28.7439</td>
      <td>0.0856827</td>
    </tr>
  </tbody>
</table>
</div>




```python
returns.get_continuous_return(data)
```




    {'adjusted close': 337.6,
     'total dividend amount': 69.08111745999996,
     'adjusted open': 26.4753935127,
     'return': 11.751462970250337}




```python
def compare_stocks(
    baseline: str,
    list_of_symbols: list,
) -> pd.DataFrame:
    
```


```python
baseline_symbol = "SPY"
targets_symbols = ["PRWAX", "LGILX", "PJFZX", "FBGRX"] 
```


```python
baseline_data = stocks.get_historical_data(baseline_symbol, api_key=API_KEY)
baseline_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>open</th>
      <th>volume</th>
      <th>adjusted close</th>
      <th>adjusted high</th>
      <th>adjusted low</th>
      <th>adjusted open</th>
      <th>adjusted volume</th>
      <th>dividend amount</th>
      <th>splitFactor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-02-20</th>
      <td>336.95</td>
      <td>338.6400</td>
      <td>333.6817</td>
      <td>337.7423</td>
      <td>71271706</td>
      <td>336.95</td>
      <td>338.6400</td>
      <td>333.6817</td>
      <td>337.7423</td>
      <td>71271706</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-19</th>
      <td>338.34</td>
      <td>339.0800</td>
      <td>337.4800</td>
      <td>337.7900</td>
      <td>48587393</td>
      <td>338.34</td>
      <td>339.0800</td>
      <td>337.4800</td>
      <td>337.7900</td>
      <td>48587393</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-18</th>
      <td>336.73</td>
      <td>337.6677</td>
      <td>335.2100</td>
      <td>336.5100</td>
      <td>57195407</td>
      <td>336.73</td>
      <td>337.6677</td>
      <td>335.2100</td>
      <td>336.5100</td>
      <td>57195407</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-14</th>
      <td>337.60</td>
      <td>337.7300</td>
      <td>336.2000</td>
      <td>337.5100</td>
      <td>64518123</td>
      <td>337.60</td>
      <td>337.7300</td>
      <td>336.2000</td>
      <td>337.5100</td>
      <td>64518123</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2020-02-13</th>
      <td>337.06</td>
      <td>338.1200</td>
      <td>335.5600</td>
      <td>335.8621</td>
      <td>54038002</td>
      <td>337.06</td>
      <td>338.1200</td>
      <td>335.5600</td>
      <td>335.8621</td>
      <td>54038002</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
targets_data = [stocks.get_historical_data(symbol, api_key=API_KEY) for symbol in targets_symbols]
[x.shape for x in targets_data]
```




    [(7592, 12), (5622, 12), (6003, 12), (7592, 12)]




```python
min_date = baseline_data.index[-1]
for data in targets_data:
    date = data.index[-1]
    if date > min_date:
        min_date = date

print(date)
```

    1990-01-02



```python
filter_indexes = baseline_data.index >= min_date
baseline_data = baseline_data[filter_indexes]

for idx in range(len(targets_data)):
    filter_indexes = targets_data[idx].index >= min_date
    targets_data[idx] = targets_data[idx][filter_indexes]
    
    
baseline_data.shape, [x.shape for x in targets_data], baseline_data.index[-1], [x.index[-1] for x in targets_data]
```




    ((5623, 12),
     [(5622, 12), (5622, 12), (5622, 12), (5622, 12)],
     '1997-10-15',
     ['1997-10-15', '1997-10-15', '1997-10-15', '1997-10-15'])




```python
minimum_nr_of_months = 8
baseline_returns = (
    returns.get_returns_by_year(baseline_data, minimum_nr_of_months=minimum_nr_of_months),
    returns.get_continuous_return(baseline_data)["return"]
)

targets_returns = [
    (
        symbol,
        returns.get_returns_by_year(data, minimum_nr_of_months=minimum_nr_of_months),
        returns.get_continuous_return(data)["return"]
    )
    for symbol, data in zip(targets_symbols, targets_data)
]
targets_returns.sort(key=lambda tup: tup[2], reverse=True)
baseline_returns[1], [(x[0], x[2]) for x in targets_returns]
```




    (4.232222067232761,
     [('PJFZX', 5.768547236601928),
      ('FBGRX', 5.558680804805675),
      ('PRWAX', 4.9145884796871036),
      ('LGILX', 3.4721264342325027)])




```python
import pandas as pd

subtract_years_to_baseline = True

growth_col = "growth"
total_idx = "Total"
df = pd.DataFrame(columns=[baseline_symbol] + [target[0] for target in targets_returns])

df.loc[total_idx, baseline_symbol] = baseline_returns[1]
for target in targets_returns:
    df.loc[total_idx, target[0]] = target[2]
    
for year, row in baseline_returns[0].iterrows():
    baseline_growth = row[growth_col]
    df.loc[year, baseline_symbol] = baseline_growth
    for target in targets_returns:
        growth = target[1].loc[year, growth_col]
        if subtract_years_to_baseline:
            growth = growth - baseline_growth
        df.loc[year, target[0]] = growth

df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SPY</th>
      <th>PJFZX</th>
      <th>FBGRX</th>
      <th>PRWAX</th>
      <th>LGILX</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Total</th>
      <td>4.23222</td>
      <td>5.76855</td>
      <td>5.55868</td>
      <td>4.91459</td>
      <td>3.47213</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>0.333236</td>
      <td>0.0937805</td>
      <td>-0.00108901</td>
      <td>0.0158721</td>
      <td>-0.00527827</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>-0.0490628</td>
      <td>0.0229571</td>
      <td>0.0439222</td>
      <td>0.049961</td>
      <td>0.0534895</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>0.208837</td>
      <td>0.144623</td>
      <td>0.138637</td>
      <td>0.126494</td>
      <td>0.116532</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>0.138895</td>
      <td>-0.126427</td>
      <td>-0.101981</td>
      <td>-0.0980795</td>
      <td>-0.108812</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>0.0084017</td>
      <td>0.103686</td>
      <td>0.0561231</td>
      <td>0.0803694</td>
      <td>-0.00900447</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>0.139</td>
      <td>-0.0313798</td>
      <td>0.0154203</td>
      <td>-0.0350919</td>
      <td>-0.0423936</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>0.298449</td>
      <td>0.0468035</td>
      <td>0.063611</td>
      <td>0.0521509</td>
      <td>0.0483416</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>0.139398</td>
      <td>0.00256071</td>
      <td>0.0204865</td>
      <td>-0.0186388</td>
      <td>0.0198204</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>0.0111594</td>
      <td>-0.0190666</td>
      <td>-0.0525111</td>
      <td>-0.023966</td>
      <td>-0.0354731</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>0.141054</td>
      <td>-0.0366909</td>
      <td>0.0351661</td>
      <td>0.0355319</td>
      <td>-0.00777607</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>0.260866</td>
      <td>0.1325</td>
      <td>0.144915</td>
      <td>0.175097</td>
      <td>0.177687</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>-0.369459</td>
      <td>4.68704e-05</td>
      <td>-0.00896601</td>
      <td>-0.00423241</td>
      <td>-0.00267337</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>0.0463323</td>
      <td>0.0686589</td>
      <td>0.069421</td>
      <td>0.0925045</td>
      <td>0.128915</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>0.153588</td>
      <td>-0.156533</td>
      <td>-0.11621</td>
      <td>-0.0905678</td>
      <td>-0.120935</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>0.0423079</td>
      <td>0.109249</td>
      <td>0.00527191</td>
      <td>0.0139188</td>
      <td>0.10997</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>0.10247</td>
      <td>-0.00780483</td>
      <td>-0.0371678</td>
      <td>0.00961004</td>
      <td>0.0173697</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>0.272821</td>
      <td>-0.0181214</td>
      <td>-0.0642089</td>
      <td>0.0343661</td>
      <td>-0.0148642</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>-0.221328</td>
      <td>-0.0910046</td>
      <td>-0.0363605</td>
      <td>-0.0649873</td>
      <td>-0.0691134</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>-0.122959</td>
      <td>-0.0316739</td>
      <td>-0.00534773</td>
      <td>0.0532295</td>
      <td>-0.0732745</td>
    </tr>
    <tr>
      <th>2000</th>
      <td>-0.105665</td>
      <td>-0.0671172</td>
      <td>0.00656171</td>
      <td>0.0228788</td>
      <td>-0.171542</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>0.203266</td>
      <td>0.213856</td>
      <td>0.0440275</td>
      <td>-0.062322</td>
      <td>0.0363969</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>0.283567</td>
      <td>0.0881662</td>
      <td>0.0599359</td>
      <td>-0.099548</td>
      <td>-0.0948116</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
