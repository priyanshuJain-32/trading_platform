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
import matplotlib.pyplot as plt

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
from kpi.maximumDrawdown import maxDraw
from kpi.calmarRatio import calmar

# Import Custom Strategies
from backtesting.portfolioRebalancing import pfRebalance

# Import Tickers
from tickers.dji_2018_tickers import dji_2018_tickers

# Import Data processing and download functions
from otherData.returnsCalc import returns_calc

""" 
Download the data using Yahoo finance
"""

stocks = {"AMZN", "MSFT","META","GOOG", "NVDA", "^GSPC"}
start = dt.datetime.today() - dt.timedelta(60)
end = dt.datetime.today()
ohlcv_data = {}

for ticker in stocks:
    
    # Download open high low close volume data
    ohlcv_data[ticker] = (yf.download(ticker, start, end, period="1mo", interval="15m")).dropna(axis=0)

"""
    Run and Save data on Indicators for stocks
"""
results_data = {}
renko = {}

for ticker in stocks:
    
    # Download open high low close volume data
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


"""
    Run and save KPI's for the stocks.
"""

kpi_data = pd.DataFrame(columns = ["Ticker", 
                                   "CAGR", 
                                   "Volatility", 
                                   "Sharpe Ratio", 
                                   "Sortino Ratio", 
                                   "Maximum Drawdown", 
                                   "Calmar Ratio"]) 

idx = 0
for ticker in stocks:
    
    kpi_data.loc[idx,"Ticker"] = ticker
    
    kpi_data.loc[idx,"CAGR"] = cagr(ohlcv_data[ticker])

    kpi_data.loc[idx,"Volatility"] = volatility(ohlcv_data[ticker])

    kpi_data.loc[idx,"Sharpe Ratio"] = sharpe(ohlcv_data[ticker])

    kpi_data.loc[idx,"Sortino Ratio"] = sortino(ohlcv_data[ticker])
    
    kpi_data.loc[idx,"Maximum Drawdown"] = maxDraw(ohlcv_data[ticker])
    
    kpi_data.loc[idx,"Calmar Ratio"] = calmar(ohlcv_data[ticker])
    
    idx += 1

"""
    Strategy 1 - Portfolio Rebalancing
"""

# Download the data for last 10 years with monthly prices
# Use returns_calc for calculating returns and download.

return_df = returns_calc(dji_2018_tickers)
return_dji = returns_calc(["^DJI"])
"""
Run and calculate strategy KPI's
"""
# Strategy 1 Portfolio Rebalance
# Run and save returns for portfolio
portfolio_returns = pfRebalance(return_df, max_size = 15, rebalance = 7)

strategy_results = pd.DataFrame(columns = ["Type",
                                   "CAGR", 
                                   "Sharpe", 
                                   "MaxDraw"]

# Save KPI's for Index Returns
strategy_results.loc[0,"Type"] = "Index"
strategy_results.loc[0,"CAGR"] = cagr(return_dji, period = "monthly", column = "^DJI", calculate_return = False)
strategy_results.loc[0,"Sharpe"] = sharpe(return_dji, custom_risk_free_rate = False, period = "monthly", column = "^DJI", calculate_return = False)
strategy_results.loc[0,"MaxDraw"] = maxDraw(return_dji, column = "^DJI", calculate_return = False)

# Save KPI's for portfolio Returns

strategy_results.loc[1,"Type"] = "Portfolio Rebalance"
strategy_results.loc[1,"CAGR"] = cagr(portfolio_returns, period = "monthly", column = "monthly_return", calculate_return = False)
strategy_results.loc[1,"Sharpe"] = sharpe(portfolio_returns, custom_risk_free_rate = False, period = "monthly", column = "monthly_return", calculate_return = False)
strategy_results.loc[1,"MaxDraw"] = maxDraw(portfolio_returns, column = "monthly_return", calculate_return = False)

# Visual comparison
fig, ax = plt.subplots()

plt.plot((1+portfolio_returns).cumprod())
plt.plot((1+return_dji["^DJI"].reset_index(drop=True)).cumprod())

plt.title("Index Return vs Strategy Return")
plt.ylabel("cumulative return")
plt.xlabel("months")

ax.legend(["Strategy Return","Index Return"])

# Strategy 2











































