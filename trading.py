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
from macd import macdFunc


""" 
Download the data using Yahoo finance
"""
stocks = {"AMZN", "MSFT","META","GOOG", "NVDA", "^GSPC"}
start = dt.datetime.today() - dt.timedelta(60)
end = dt.datetime.today()

cl_price = {}

for ticker in stocks:
    cl_price[ticker] = (yf.download(ticker, start, end, period="1mo", interval="15m")).dropna(axis=0)
    
for ticker in stocks:
    cl_price[ticker][["MACD","Signal"]] = macdFunc(cl_price[ticker])

# cl_price.plot()
# cl_price.drop("^GSPC", axis=1).plot()

""" 
Calculate simple return "R" and log return "r" 
"""
simple_return = cl_price.pct_change()
simple_return.dropna(axis=0, inplace=True)

log_return = pd.DataFrame()
for ticker in stocks:
    log_return[ticker] = np.log(cl_price[ticker]) - np.log(cl_price[ticker]).shift(1)

log_return.dropna(axis=0, inplace=True)

print(cl_price)