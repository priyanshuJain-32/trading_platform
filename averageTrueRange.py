#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:01:25 2024

@author: priyanshu

Average True Range: focuses on price movement and conveys how wildly he market is swinging.
The value of ATR shows the fluctuation in value of stock. For eg if value is 10 for a 
US stock then the stock will vary by $10 in that time period.

Takes into account price movement in each period by considering the following ranges:

    - Difference between high and low.
    - Difference between high and previous close.
    - Difference between low and previous close.
    
Used for volatility studies. If both ATR and Bollinger Bands say volatility is increasing then
we consider that it is infact increasing.
"""
import pandas as pd

def atr(DF: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    
    df = DF.copy() # create copy of original Database
    
    
    df["H-L"] = df["High"] - df["Low"] # calculate diff of high and low
    
    
    df["H-PC"] = df["High"] - df["Adj Close"].shift(1) # calculate diff of high and previous close
    
    
    df["L-PC"] = df["Low"] - df["Adj Close"].shift(1) # calculate diff of low and previous close
    
    
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1,skipna=False) # calculate max of all the diffs
    
    
    df["ATR"] = df["TR"].ewm(com=window, min_periods = window).mean() # calculate moving average
    
    
    return df["ATR"] # return the average true range