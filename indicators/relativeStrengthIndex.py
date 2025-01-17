#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:50:38 2024

@author: priyanshu

# RSI - Relative Strength Index

    RSI is a momentum oscillator which measures speed and change of price movements.
    It conveys the strength of price movements compare to its previous prices.
    
    The value oscillates between 0 and 100 with 
        - values above 70 indicating that the asset has now reached overbought territory.
          and a correction is expected.
          
        - values below 30 signify oversold territory and buying pressure is expected.
        
        For developed markets 70-30 are used and for developing 80-20 could be considered.
        
    Assets can remain in overbought and oversold territories for long durations.
    
    Calculation follows a two step method wherein the second step acts at a smoothening
    technique (similar to calculating exponential MA).
    
    Drawbacks:
        Even if a stock has RSI of 80 and we think that we can short that stock, but
        that situation can persist for long and hence there could be loss.
        
        Vice versa for the lower mark.
"""

import numpy as np
import pandas as pd

def rsi(DF: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """
    Parameters
    ----------
    DF : DF : pd.DataFrame, data on Adj close for a stock.
    
    window : int, optional
        The window size to consider for mvoing average. The default is 14.

    Returns
    -------
    df["rsi"]: Pandas DataFrame
        
        Relative Strength Index for the data calculated using Adj Close prices.

    """
    
    df = DF.copy()
    
    df["change"] = df["Adj Close"] - df["Adj Close"].shift(1)
    
    df["gain"] = np.where(df["change"]>=0, df["change"], 0)
    df["loss"] = np.where(df["change"]<0, -df["change"], 0)
    
    df["avg_gain"] = df["gain"].ewm(alpha = 1/window, min_periods = window).mean()
    df["avg_loss"] = df["gain"].ewm(alpha = 1/window, min_periods = window).mean()
    
    df["rs"] = df["avg_gain"]/df["avg_loss"]
    
    df["rsi"] = 100 - (100 / (1 + df["rs"]))
    
    return df["rsi"]