#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 06:13:43 2024

@author: priyanshu
"""
"""
Intraday Resistance Breakout

    Resistance Breakout is a technical trading term which means that the price of the stock
    has breached a presumed resistance level (determined by a price chart)

    Choose high volume, high activity stocks for this strategy (pre market movers, historically
    high volume stocks, etc.)

    Define breakout rule - Implementation is with price breaching 20 period rolling max/min price in
    conjunction with volume breaching rolling max volume - go long/short stocks based on signals

    Define exit/stop loss signal - Implemented one will be using previous price plus/minus 20
    period ATR as the rolling stop loss price.

    Backtest the strategy by calculating cumulative return for each stock. 

"""
import sys
sys.path.append("..")

import pandas as pd

from indicators.averageTrueRange import atr

def resistanceBreach(DF: pd.DataFrame, index: int, vol_mult: float) -> bool:
    
    return DF["High"][index] >= DF["roll_max_cp"][index] and DF["Volume"][index] > vol_mult*DF["roll_max_vol"][index-1]

def supportBreach(DF: pd.DataFrame, index: int, vol_mult: float) -> bool:

    return DF["Low"][index] <= DF["roll_min_cp"][index] and DF["Volume"][index] > vol_mult*DF["roll_max_vol"][index-1]

def stopLossHighSide(DF: pd.DataFrame, index: int) -> bool:

    return DF["Low"][index] < DF["Close"][index-1] - DF["ATR"][index-1]

def stopLossLowSide(DF: pd.DataFrame, index: int) -> bool:
    return DF["High"][index] > DF["Close"][index-1] - DF["ATR"][index-1]

def intraResBreak(DF):
    df = DF.copy()

    df["ATR"] = atr(df, window = 20) # average true range
    df["roll_max_cp"] = df["High"].rolling(20).max() # resistance
    df["roll_min_cp"] = df["Low"].rolling(20).min() # support
    df["roll_vol_max"] = df["Volume"].rolling(20).max() # vol max
    
    df.dropna(inplace=True)
    tickers_signal = []

    pass
