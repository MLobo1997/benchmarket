```python
%load_ext autoreload
from src.data import stocks
```

# API key
Get your free security/stocks API key in [this link](https://api.tiingo.com/account/api/token).


```python
API_KEY = ""
```

# Select the securities you want to compare
* The baseline symbol is the ticker for the security you mostly want to compare others (the targets) with. It is designed to be some market index, in order to be able to conclude how consistently the target securities have (or not) "beat the market". The ITOT symbol is from an ETF that indexes stock from the whole world.
* `minimum_nr_of_months` is the minimum number of months of data a security must have in a year so that the year is accounted for. E.g: if some fund was created in july 1997, and `minimum_nr_of_months` is 6, then the year 1997 won't be analyzed.
* if `subtract_returns_to_baseline` is set to `True` then all the target securities yearly growths are subtracted to baseline value of the corresponding year, so that clearer insights on on yearly performance are obtained


```python
%autoreload 2
from src.analysis import returns

continuous_returns, returns_by_year, median_yearly_returns, avg_yearly_returns, beat_the_market_ratio = returns.compare_stocks(
    baseline_symbol="ITOT",
    targets_symbols=[
        "SPY",
        "PREFX",  
        "QQQ",
        "VGT",
    ],
    api_key=API_KEY,
    minimum_nr_of_months=8,
    subtract_returns_to_baseline=True
)

```

# Continuous returns
The continuous returns are computed throught only the time of data available


```python
continuous_returns
```




    {'baseline': 3.076656392323726,
     'targets': [('QQQ', 7.361796454274539),
      ('VGT', 6.186002583837699),
      ('PREFX', 4.309599591407751),
      ('SPY', 3.020131363260466)]}




```python
returns_by_year
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ITOT</th>
      <th>QQQ</th>
      <th>VGT</th>
      <th>PREFX</th>
      <th>SPY</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020</th>
      <td>0.0285272</td>
      <td>0.245175</td>
      <td>0.198617</td>
      <td>0.145352</td>
      <td>-0.00405211</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>0.326818</td>
      <td>0.0928743</td>
      <td>0.189091</td>
      <td>0.0418739</td>
      <td>0.0064179</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>-0.056447</td>
      <td>0.0501804</td>
      <td>0.0763515</td>
      <td>0.0425129</td>
      <td>0.00738419</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>0.204165</td>
      <td>0.113243</td>
      <td>0.157712</td>
      <td>0.0722189</td>
      <td>0.00467258</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>0.146367</td>
      <td>-0.0515708</td>
      <td>0.0125219</td>
      <td>-0.100687</td>
      <td>-0.00747229</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>0.00265032</td>
      <td>0.0864347</td>
      <td>0.0422622</td>
      <td>0.0605095</td>
      <td>0.00575137</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>0.132249</td>
      <td>0.0651254</td>
      <td>0.0526517</td>
      <td>-0.0255987</td>
      <td>0.00675079</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>0.288168</td>
      <td>0.046215</td>
      <td>-0.00786564</td>
      <td>0.0329283</td>
      <td>0.0102813</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>0.138362</td>
      <td>0.0203827</td>
      <td>-0.0199444</td>
      <td>-0.00169805</td>
      <td>0.00103648</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>0.0059413</td>
      <td>0.018494</td>
      <td>-0.00927043</td>
      <td>-0.0253387</td>
      <td>0.0052181</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>0.154556</td>
      <td>0.029777</td>
      <td>-0.040592</td>
      <td>0.0399018</td>
      <td>-0.0135024</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>0.264371</td>
      <td>0.281029</td>
      <td>0.351654</td>
      <td>0.105863</td>
      <td>-0.00350482</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>-0.362375</td>
      <td>-0.0554733</td>
      <td>-0.0720163</td>
      <td>-0.0630634</td>
      <td>-0.00707368</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>0.0454063</td>
      <td>0.136619</td>
      <td>0.0911635</td>
      <td>0.0855945</td>
      <td>0.00129388</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>0.148192</td>
      <td>-0.0830631</td>
      <td>-0.0644156</td>
      <td>-0.0746371</td>
      <td>0.00399728</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>0.0499895</td>
      <td>-0.0380743</td>
      <td>-0.0287254</td>
      <td>0.010048</td>
      <td>-0.00768162</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>0.0972514</td>
      <td>-0.0139772</td>
      <td>-0.119201</td>
      <td>0.00704305</td>
      <td>-0.0120677</td>
    </tr>
  </tbody>
</table>
</div>




```python
avg_yearly_returns
```




    [('QQQ', 0.05549356348395734),
     ('VGT', 0.04764677966302673),
     ('PREFX', 0.020754305059020928),
     ('SPY', -0.00015004256161888022)]




```python
median_yearly_returns
```




    [('QQQ', 0.046215010426060465),
     ('PREFX', 0.03292825606759314),
     ('VGT', 0.012521879430894084),
     ('SPY', 0.001293878091998435)]


