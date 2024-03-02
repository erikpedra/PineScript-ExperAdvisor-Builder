# PineScript-ExperAdvisor-Builder
Name Project : PineScript-ExperAdvisor-Builder   
Website : https://tv2metatrader.com/   
Website : https://autotradevip.com/id/   
Telegram : https://t.me/minsanztuy   

PineScriptBuilder v5 adalah pustaka Python yang memungkinkan Anda untuk membuat script Pine untuk platform TradingView secara dinamis menggunakan Python. Dengan PineScriptBuilder, Anda dapat menghasilkan kode PineScript secara otomatis, mempercepat proses pengembangan strategi perdagangan atau indikator.

Expert Advisor adalah program yang digunakan dalam platform MetaTrader untuk melakukan trading secara otomatis berdasarkan aturan yang telah ditentukan. MQL4 dan MQL5 adalah bahasa pemrograman yang digunakan untuk membuat EA dalam platform MetaTrader 4 (MT4) dan MetaTrader 5 (MT5) secara berurutan. Dalam tutorial ini, kita akan membahas cara menggunakan Python untuk membangun EA dengan menggunakan ExpertAdvisor MQL4 & MQL5 Builder.



### Debug Mode ON
```python
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
```

### Import PineScript
```python
from PineScriptAPI import PineScriptBuilder
```

### Import Expert Advisor MQL4 & MQL5 Builder
```python
from ExpertAdvisorAPI import ExpertAdvisorBuilder
```

### Strategy Example
```python
from PineScriptAPI import PineScriptBuilder

# Inisialisasi objek PineScriptBuilder
builder = PineScriptBuilder()
builder.strategy(Title="MA Cross Take profits & stop losses", shorttitle="MA Strategy", overlay=True)

# Tambahkan input
builder.input(name="ShortMa", defval="10", title="Short Moving Average")
builder.input(name="LongMa", defval="30", title="Long Moving Average")
builder.input(name="ATRlength, defval="14", title="Average True Range")

# Tambahkan Indikator
builder.add_indikator(name="ShortMa1", indicator="sma", source="close", length="ShortMa")
builder.add_indikator(name="LongMa2", indicator="sma", source="close", length="LongMa")
builder.add_indikator(name="atr", indicator="atr", length="ATRlength")

# Tambahkan custom kode yang diinginkan Tanpa limit
builder.add_custom(name="takeProfit", code="high + atr * 2") 
builder.add_custom(name="stopLoss", code="low - atr * 2") 

# Tentukan kondisi persilangan
builder.add_cross(name="longCondition", indicator1="ShortMa1", indicator2="longSMA", "crossUp")
builder.add_cross(name="shortCondition", indicator1="ShortMa1", indicator2="longSMA", "crossDown")

#Tambahkan Long Entry
builder.add_condition(name="longCondition")
builder.entry(id="long", direction="long", qty="100")
builder.exit(id="exit", from_entry="long", stop="stopLoss", limit="takeProfit")

#Tambahkan Short Entry
builder.add_condition(name="shortCondition")
builder.entry(id="short direction="short", qty="100")
builder.exit(id="exit", from_entry="short", stop="stopLoss", limit="takeProfit")

# Tambahkan Plot Moving Average ke chart
builder.add_pot("ShortMa1", color="color.red")
builder.add_pot("LongMa2", color="color.green")

# Cetak kode Pinescript
print(builder.generate())
```


### Output
```pinescript
//
// TV2 Studio PineScript
//
// Created with: TradingView Studio
// Website: https://tv2metatrader.com
//
// Copyright 2024, TV2MetaTrader Software Ltd.
//
// Risk Disclosure
//
// Futures and forex trading contains substantial risk and is not for every investor.
// An investor could potentially lose all or more than the initial investment.
// Risk capital is money that can be lost without jeopardizing ones’ financial security or life style.
// Only risk capital should be used for trading and only those with sufficient risk capital should consider trading.
//@version=5
strategy("MA Cross Take profits & stop losses", shorttitle="MA Strategy", overlay=true)

// Tambahkan input
ShortMa = input(defval=10, title="Short Moving Average")
LongMa = input(defval=30, title="Long Moving Average")
ATRlength = input(defval=14, title="Average True Range")

// Tambahkan Indikator
ShortMa1 = ta.sma(close, ShortMa)
LongMa2 = ta.sma(close, LongMa)
atr = ta.atr(ATRlength)

// Tambahkan custom kode yang diinginkan Tanpa limit
takeProfit = high + atr * 2
stopLoss = low - atr * 2

// Tentukan kondisi persilangan
longCondition = ta.crossover(ShortMa1, LongMa2)
shortCondition = ta.crossunder(ShortMa1, LongMa2)

// Tambahkan Long Entry
if (longCondition)
    strategy.entry("long", strategy.long, qty=100)
    strategy.exit("exit", "long", stop=stopLoss, limit=takeProfit)

// Tambahkan Short Entry
if (shortCondition)
    strategy.entry("short", strategy.short, qty=100)
    strategy.exit("exit", "short", stop=stopLoss, limit=takeProfit)

// Tambahkan Plot Moving Average ke chart
plot(ShortMa1, color=color.red)
plot(LongMa2, color=color.green)

```
