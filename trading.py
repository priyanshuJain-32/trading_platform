#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:28:06 2024

@author: priyanshu
"""

# Download the libraries
import datetime as dt
import yfinance as yf
import pandas as pd
import numpy as np

# Import Custom functions
from macd import macdFunc
from bollingerBands import bBands
from averageTrueRange import atr
from relativeStrengthIndex import rsi
from averageDirectionalIndex import adx
from renkoChart import renkoFunc


""" 
Download the data using Yahoo finance
"""

stocks = {"AMZN", "MSFT","META","GOOG", "NVDA", "^GSPC"}
start = dt.datetime.today() - dt.timedelta(60)
end = dt.datetime.today()

ohlcv_data = {}
results_data = {}
renko = {}

for ticker in stocks:
    ohlcv_data[ticker] = (yf.download(ticker, start, end, period="1mo", interval="15m")).dropna(axis=0)
    results_data[ticker] = ohlcv_data[ticker].copy()

# Calculate and save MACD to data
for ticker in stocks:
    results_data[ticker][["MACD","Signal"]] = macdFunc(ohlcv_data[ticker])
    
# Calculate and save ATR to data
for ticker in stocks:
    results_data[ticker]["ATR"] = atr(ohlcv_data[ticker])
    
# Calculate and save Bollinger Bands to data
for ticker in stocks:
    results_data[ticker][["middleBand", "upperBand", "lowerBand", "bandWidth"]] = bBands(ohlcv_data[ticker], window=14, sd=2)

# Calculate and save RSI to data
for ticker in stocks:
    results_data[ticker]["RSI"] = rsi(ohlcv_data[ticker], window = 14)
    
for ticker in stocks:
    results_data[ticker]["ADX"] = adx(ohlcv_data[ticker], window = 20)

for ticker in stocks:
    renko[ticker] = renkoFunc(ohlcv_data[ticker])

# cl_price.plot()
# cl_price.drop("^GSPC", axis=1).plot()

""" 
Calculate simple return "R" and log return "r" 
"""
simple_return = ohlcv_data.pct_change()
simple_return.dropna(axis=0, inplace=True)

log_return = pd.DataFrame()
for ticker in stocks:
    log_return[ticker] = np.log(ohlcv_data[ticker]) - np.log(ohlcv_data[ticker]).shift(1)

log_return.dropna(axis=0, inplace=True)
