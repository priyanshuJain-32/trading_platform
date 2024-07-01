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

# Import Custom Indicators
from indicators.macd import macdFunc
from indicators.bollingerBands import bBands
from indicators.averageTrueRange import atr
from indicators.relativeStrengthIndex import rsi
from indicators.averageDirectionalIndex import adx
from indicators.renkoChart import renkoFunc

# Import Custom Performance Indicators
from kpi.compoundedAnnualGrowthRate import cagr
from kpi.volatility import volatility
from kpi.sharpeRatio import sharpe
from kpi.sortinoRatio import sortino
# from kpi.maximumDrawdown import maxDraw
# from kpi.calmarRatio import calmar

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
    
    # Download open high low close volume data
    ohlcv_data[ticker] = (yf.download(ticker, start, end, period="1mo", interval="15m")).dropna(axis=0)
    results_data[ticker] = ohlcv_data[ticker].copy()

    # Calculate and save MACD to data
    results_data[ticker][["MACD","Signal"]] = macdFunc(ohlcv_data[ticker])
    
    # Calculate and save ATR to data
    results_data[ticker]["ATR"] = atr(ohlcv_data[ticker])
    
    # Calculate and save Bollinger Bands to data
    results_data[ticker][["middleBand", "upperBand", "lowerBand", "bandWidth"]] = bBands(ohlcv_data[ticker], window=14, sd=2)

    # Calculate and save RSI to data
    results_data[ticker]["RSI"] = rsi(ohlcv_data[ticker], window = 14)
    
    # Calculate ADX for the data
    results_data[ticker]["ADX"] = adx(ohlcv_data[ticker], window = 20)

    # Calculate Renko for the data
    renko[ticker] = renkoFunc(ohlcv_data[ticker], ticker = ticker, use_atr = False)


for ticker in stocks:
    
    print("CAGR for {} = {}".format(ticker, cagr(ohlcv_data[ticker])))
    print("Vol for {} = {}".format(ticker, volatility(ohlcv_data[ticker])))
    print("\nSharpe for {} = {}".format(ticker, sharpe(ohlcv_data[ticker])))
    print("Sortino for {} = {}\n".format(ticker, sortino(ohlcv_data[ticker])))

