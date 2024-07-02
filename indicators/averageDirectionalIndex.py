#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:56:08 2024

@author: priyanshu

Average Directional Index (ADX):
    
    It is a way of measuring strength of a trend.
    
    Values range from 0 to 100
    
        0-25: Absent or weak trend
        25-50: Strong trend
        50-75: Very strong trend
        75-100: Extremely strong trend
        
    ADX is non directional meaning the ADX value makes no inference about the direction
    of the trend
    
    If the trend is weak then we should not trust that trend.
    
    The calculation involves finding both positive and negative directional movement
    (by comparing successive highs and successive lows) and then calculating the
    smoothed average of the difference of these.
    
    Calculations can vary a lot on different platforms and how it is calculated.
"""
import sys
sys.path.append("..")
from indicators.averageTrueRange import atr
import pandas as pd
import numpy as np

def adx(DF: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Parameters
    ----------
    DF : pd.DataFrame, data on open high low close for a stock.
    
    window : int, optional
        The window size to consider for mvoing average. The default is 20.

    Returns
    -------
    df["ADX"]: Pandas DataFrame. Average Directional Index.

    """
    
    df = DF.copy() # create copy of original Database
    
    
    df["upMove"] = df["High"] - df["High"].shift(1) # calculate diff of Current High and Previous High
    
    
    df["downMove"] = df["Low"].shift(1) - df["Low"] # calculate diff of Current Low and previous Low
    
    
    df["dmPlus"] = np.where((df["upMove"] > df["downMove"]) & (df["upMove"]>0),df["upMove"],0)  # calculate diff of low and previous close
    
    df["dmMinus"] = np.where((df["downMove"] > df["upMove"]) & (df["downMove"]>0),df["downMove"],0) # calculate diff of low and previous close
    
    df["ATR"] = atr(df, window = 20)
    
    df["diPlus"] = 100 * (df["dmPlus"]/df["ATR"]).ewm(com = window, min_periods = window).mean()

    df["diMinus"] = 100 * (df["dmMinus"]/df["ATR"]).ewm(com = window, min_periods = window).mean()
    
    df["ADX"] = (abs((df["diPlus"] - df["diMinus"])/(df["diPlus"] + df["diMinus"]))).ewm(span = window, min_periods = window).mean()
    
    return df["ADX"]