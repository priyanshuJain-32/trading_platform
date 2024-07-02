#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:11:21 2024

@author: priyanshu
"""

"""
Maximum Drawdown & Calmar Ratio

    Maximum Drawdonw:
    
    Largest percentage drop in asset price over a specified time period 
    (distance between peak and the trough in the line curve of the asset)

    Investments with longer backtesting period will have larger max drawdown
    and therefore caution must be applied in comparing across strategies.
    
    Calmar Ratio is the ratio CAGR and Max drawdown and it's a measure of it's
    risk adjusted return.
    
    It is very important as higher drawdown means we should not stay with the strategy for
    long periods of time as it can lead to losses and offset our CAGR.

    Drawdown also helps us understand whether our leverage is good and 
    investment is solvent or not.
"""
import pandas as pd

def maxDraw(DF: pd.DataFrame, column: str = "Adj Close", calculate_return: bool = True) -> int:
    """

    Parameters
    ----------
    DF : pd.DataFrame. Data of stock prices.

    Returns
    -------
    maxDD : int, Maximum Drawdown
    
    column : String, column to use in the given dataFrame for calculating CAGR. Default Adj Close.
    
    calculate_return: Boolean, Whether to calculate return for the specified column. Default True.

    """
    
    df = DF.copy()
    
    if column != "Adj Close" and calculate_return == True:
        df["return"] = df[column].pct_change()
        
    elif column != "Adj Close" and calculate_return == False:
        df["return"] = df[column]
    
    elif column == "Adj Close" and calculate_return == True:
        df["return"] = df["Adj Close"].pct_change()
    

    df["cum_return"] = (1+df["return"]).cumprod()
    
    df["cum_roll_max"] = df["cum_return"].cummax()
    
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    
    maxDD = (df["drawdown"]/df["cum_roll_max"]).max()
    
    return maxDD