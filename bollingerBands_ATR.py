#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:39:09 2024

@author: priyanshu

Implementation of Bollinger bands:
    
    Bollinger bands: are two lines plotted n standard deviations above and below the m period
    simple moving average line. The bands widen during increased volatility and shrink during
    reduced volatility. Typically n=2 and m=20.
    
    ATR: focuses on price movement and conveys how wildly he market is swinging.
    The value of ATR shows the fluctuation in value of stock. For eg if value is 10 for a 
    US stock then the stock will vary by $10 in that time period.
    
    Takes into account price movement in each period by considering the following ranges:
    
        - Difference between high and low.
        - Difference between high and previous close.
        - Difference between low and previous close.
    
    Used for volatility studies. If both indicators say volatility is increasing then
    we consider that it is infact increasing.
    
    Two ways to use these bands:
        
        If a candle exceeds the band limit whether upper or lower then a reversal
        is expected.
        
        If the bands widen then there is higher volatility and higher activity in
        the stock and hence a good time to trade.
    
    
"""

def bBands(DF, window=20, sd=2):
    df = DF.copy()
    df["middleBand"] = df["Adj Close"].rolling(window).mean()
    df["upperBand"] = df["middleBand"] + sd * df["Adj Close"].rolling(window).std(ddof = 0)
    df["lowerBand"] = df["middleBand"] - sd * df["Adj Close"].rolling(window).std(ddof = 0)
    df["bandWidth"] = df["upperBand"] - df["lowerBand"]
    return df.loc[:,["middleBand", "upperBand", "lowerBand", "bandWidth"]]


def atr(DF, window = 14):
    df = DF.copy()
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] = df["High"] - df["Adj Close"].shift(1)
    df["L-PC"] = df["Low"] - df["Adj Close"].shift(1)
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1,skipna=False)
    df["ATR"] = df["TR"].ewm(com=window, min_periods = window).mean()
    return df["ATR"]