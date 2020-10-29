```python
%load_ext autoreload
from src.data import stocks
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


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
        "PRWAX",
        "VWELX",
        "PJFZX", 
        "FMAGX",
        "PREFX",  
        "FKDNX", 
        "QQQ",
        "XLK",
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
      ('FKDNX', 6.317277791361265),
      ('VGT', 6.186002583837699),
      ('PJFZX', 6.037220557464273),
      ('XLK', 5.727539271277336),
      ('PRWAX', 5.534768417418527),
      ('PREFX', 4.309599591407751),
      ('SPY', 3.020131363260466),
      ('FMAGX', 2.6057392579293186),
      ('VWELX', 2.604164437778007)]}




```python
returns_by_year
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
      <th>ITOT</th>
      <th>QQQ</th>
      <th>FKDNX</th>
      <th>VGT</th>
      <th>PJFZX</th>
      <th>XLK</th>
      <th>PRWAX</th>
      <th>PREFX</th>
      <th>SPY</th>
      <th>FMAGX</th>
      <th>VWELX</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020</th>
      <td>0.0285272</td>
      <td>0.245175</td>
      <td>0.326691</td>
      <td>0.198617</td>
      <td>0.309008</td>
      <td>0.189284</td>
      <td>0.200235</td>
      <td>0.145352</td>
      <td>-0.00405211</td>
      <td>0.115023</td>
      <td>-0.0271777</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>0.326818</td>
      <td>0.0928743</td>
      <td>0.0421649</td>
      <td>0.189091</td>
      <td>0.100198</td>
      <td>0.203092</td>
      <td>0.02229</td>
      <td>0.0418739</td>
      <td>0.0064179</td>
      <td>-0.0181394</td>
      <td>-0.102721</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>-0.056447</td>
      <td>0.0501804</td>
      <td>0.0698728</td>
      <td>0.0763515</td>
      <td>0.0303413</td>
      <td>0.0358632</td>
      <td>0.0573451</td>
      <td>0.0425129</td>
      <td>0.00738419</td>
      <td>-0.00833411</td>
      <td>0.018559</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>0.204165</td>
      <td>0.113243</td>
      <td>0.173616</td>
      <td>0.157712</td>
      <td>0.149295</td>
      <td>0.129797</td>
      <td>0.131167</td>
      <td>0.0722189</td>
      <td>0.00467258</td>
      <td>0.0474103</td>
      <td>-0.0707161</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>0.146367</td>
      <td>-0.0515708</td>
      <td>-0.109003</td>
      <td>0.0125219</td>
      <td>-0.1339</td>
      <td>0.0248998</td>
      <td>-0.105552</td>
      <td>-0.100687</td>
      <td>-0.00747229</td>
      <td>-0.0747868</td>
      <td>-0.026486</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>0.00265032</td>
      <td>0.0864347</td>
      <td>0.0817443</td>
      <td>0.0422622</td>
      <td>0.109438</td>
      <td>0.0456459</td>
      <td>0.0861207</td>
      <td>0.0605095</td>
      <td>0.00575137</td>
      <td>0.0380013</td>
      <td>0.00263223</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>0.132249</td>
      <td>0.0651254</td>
      <td>-0.0522158</td>
      <td>0.0526517</td>
      <td>-0.0246291</td>
      <td>0.0502043</td>
      <td>-0.0283411</td>
      <td>-0.0255987</td>
      <td>0.00675079</td>
      <td>0.0102287</td>
      <td>-0.027328</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>0.288168</td>
      <td>0.046215</td>
      <td>0.0741333</td>
      <td>-0.00786564</td>
      <td>0.0570848</td>
      <td>-0.0584979</td>
      <td>0.0624321</td>
      <td>0.0329283</td>
      <td>0.0102813</td>
      <td>0.0311172</td>
      <td>-0.108952</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>0.138362</td>
      <td>0.0203827</td>
      <td>-0.00112719</td>
      <td>-0.0199444</td>
      <td>0.00359718</td>
      <td>-0.00412945</td>
      <td>-0.0176024</td>
      <td>-0.00169805</td>
      <td>0.00103648</td>
      <td>0.00878448</td>
      <td>-0.0261269</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>0.0059413</td>
      <td>0.018494</td>
      <td>-0.0436975</td>
      <td>-0.00927043</td>
      <td>-0.0138485</td>
      <td>0.0124408</td>
      <td>-0.0187479</td>
      <td>-0.0253387</td>
      <td>0.0052181</td>
      <td>-0.131597</td>
      <td>0.0259406</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>0.154556</td>
      <td>0.029777</td>
      <td>0.0153427</td>
      <td>-0.040592</td>
      <td>-0.0501933</td>
      <td>-0.0507371</td>
      <td>0.0220295</td>
      <td>0.0399018</td>
      <td>-0.0135024</td>
      <td>-0.0539367</td>
      <td>-0.0581082</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>0.264371</td>
      <td>0.281029</td>
      <td>0.166208</td>
      <td>0.351654</td>
      <td>0.128995</td>
      <td>0.240009</td>
      <td>0.171592</td>
      <td>0.105863</td>
      <td>-0.00350482</td>
      <td>0.0954908</td>
      <td>-0.061613</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>-0.362375</td>
      <td>-0.0554733</td>
      <td>-0.0386344</td>
      <td>-0.0720163</td>
      <td>-0.00703713</td>
      <td>-0.052567</td>
      <td>-0.0113164</td>
      <td>-0.0630634</td>
      <td>-0.00707368</td>
      <td>-0.124452</td>
      <td>0.142531</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>0.0454063</td>
      <td>0.136619</td>
      <td>0.185809</td>
      <td>0.0911635</td>
      <td>0.069585</td>
      <td>0.104084</td>
      <td>0.0934306</td>
      <td>0.0855945</td>
      <td>0.00129388</td>
      <td>0.142192</td>
      <td>0.0389551</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>0.148192</td>
      <td>-0.0830631</td>
      <td>-0.142191</td>
      <td>-0.0644156</td>
      <td>-0.151137</td>
      <td>-0.0263414</td>
      <td>-0.0851716</td>
      <td>-0.0746371</td>
      <td>0.00399728</td>
      <td>-0.0976399</td>
      <td>-0.0112397</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>0.0499895</td>
      <td>-0.0380743</td>
      <td>0.0333438</td>
      <td>-0.0287254</td>
      <td>0.101568</td>
      <td>-0.0606383</td>
      <td>0.00623719</td>
      <td>0.010048</td>
      <td>-0.00768162</td>
      <td>0.0217453</td>
      <td>0.0257328</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>0.0972514</td>
      <td>-0.0139772</td>
      <td>-0.0432091</td>
      <td>-0.119201</td>
      <td>-0.0251396</td>
      <td>-0.0830899</td>
      <td>-0.0145987</td>
      <td>0.00704305</td>
      <td>-0.0120677</td>
      <td>-0.0358947</td>
      <td>0.00645163</td>
    </tr>
  </tbody>
</table>
</div>




```python
avg_yearly_returns
```




    [('QQQ', 0.055493563483957314),
     ('VGT', 0.047646779663026675),
     ('FKDNX', 0.04346163066178063),
     ('XLK', 0.04113638336698048),
     ('PJFZX', 0.03842509099284753),
     ('PRWAX', 0.033620520592008554),
     ('PREFX', 0.02075430505902091),
     ('SPY', -0.00015004256161892348),
     ('FMAGX', -0.0020463025225751987),
     ('VWELX', -0.015274514918881054)]




```python
median_yearly_returns
```




    [('QQQ', 0.04621501042606024),
     ('FKDNX', 0.03334381087701557),
     ('PREFX', 0.03292825606759314),
     ('PJFZX', 0.030341309034129203),
     ('XLK', 0.024899768412464496),
     ('PRWAX', 0.02202952454383686),
     ('VGT', 0.012521879430894056),
     ('FMAGX', 0.008784483720657876),
     ('SPY', 0.0012938780919987333),
     ('VWELX', -0.02612687537148664)]




```python
beat_the_market_ratio
```




    [('QQQ', 0.7058823529411765),
     ('PREFX', 0.6470588235294118),
     ('FKDNX', 0.5882352941176471),
     ('PJFZX', 0.5882352941176471),
     ('XLK', 0.5882352941176471),
     ('PRWAX', 0.5882352941176471),
     ('SPY', 0.5882352941176471),
     ('VGT', 0.5294117647058824),
     ('FMAGX', 0.5294117647058824),
     ('VWELX', 0.4117647058823529)]




```python

```
