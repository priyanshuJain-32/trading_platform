#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:30:16 2024

@author: priyanshu

# Implementation of Moving Average Convergence Divergence (MACD):
    
    
    MACD Line: 
        Here we take two different moving averages one with longer length 
        and one with shorter length. These moving averages are used to calculate 
        a macd line by taking difference of both. Typically 12 and 26 are used.
    
    Signal Line: 
        the macd line is used to calculate a signal line which is again 
        a moving average. Typically 9 period is used.

    Interpretation:
        Whenever MACD line crosses the signal line from below it is called the start of bullish
        period. Vice versa is called bearish period. This is called CROSSOVER STRATEGY.
    
    Drawback: 
        Infamous for giving false positives if market is not trending.
        Not a predictive indicator. It is a lagging indicator.
    
"""
import pandas as pd

def macdFunc(DF: pd.DataFrame, fast_len: int = 12, slow_len: int = 26, signal_smoothing: int = 9) -> pd.DataFrame:
    """

    Parameters
    ----------
    DF : DF : pd.DataFrame, data on Adj close for a stock.
    
    fast_len : int, optional
        Length of the fast moving average. The default is 12.
    
    slow_len : int, optional
        Slow moving or long term average length. The default is 26.
    
    signal_smoothing : int, optional
        Signal smoothing parameter to use for MACD. The default is 9.

    Returns
    -------
    df.loc[:,["macd","signal"]] : Pandas DataFrame.
        
        Returns MACD and Signal series for the given stock.

    """
    
    df = DF.copy()
    
    df["ma_fast"] = df["Adj Close"].ewm(span = fast_len, min_periods = fast_len).mean()
    
    df["ma_slow"] = df["Adj Close"].ewm(span = slow_len, min_periods = slow_len).mean()
    
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    
    df["signal"] = df["macd"].ewm(span = signal_smoothing, min_periods = signal_smoothing).mean()
    
    return df.loc[:,["macd","signal"]]