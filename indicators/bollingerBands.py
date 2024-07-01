#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:39:09 2024

@author: priyanshu

Implementation of Bollinger bands:
    
    Bollinger bands: are two lines plotted n standard deviations above and below the m period
    simple moving average line. The bands widen during increased volatility and shrink during
    reduced volatility. Typically n=2 and m=20.
    
    
    
    Used for volatility studies. If both ATR and Bollinger Bands say volatility is increasing then
    we consider that it is infact increasing.
    
    Two ways to use Bollinger Bands:
        
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


