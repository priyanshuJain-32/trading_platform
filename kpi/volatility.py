#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:05:19 2024

@author: priyanshu
"""

"""
Volatility: 
    
    Volatility of a strategy is represented by the standard deviation of the returns
    This captures the variability of returns from the mean.
    
    Annualization is achieved by multiplying volatility with square root of the annualization factor.
    For example:
        
        To annualize daily volatility multiply with sqrt(252)
        To annualize weekly volatility multiply with sqrt(52)
        To annualize monthly volatility multiply with sqrt(12)

    Widely used measure of risk. However this approach assumes normal distribution 
    of returns which is not true
    
    Fails to capture tail risk.
"""
import sys
sys.path.append("..")

import numpy as np
import pandas as pd
from otherData.periods import periods

def volatility(DF: pd.DataFrame, period: str = "monthly", column: str = "Adj Close", calculate_return: bool = True) -> int:
    """

    Parameters
    ----------
    DF : Pandas DataFrame, Data of stocks with Adj Close prices.
    
    period : String, Optional parameter specifying period of volatility 
                
                "yearly", "half_yearly", "quarterly", "monthly", "weekly", 
                "daily", "four_hourly", "three_hourly", "two_hourly",
                "one_hourly", "fourty_five_min", "thirty_min", "fifteen_min",
                "ten_min", "five_min", "three_min", "two_min", "one_min", "thirty_sec", "fifteen_sec",
                "ten_sec", "five_sec", "one_sec".
                
            The default is "monthly".
    
    column : String, column to use in the given dataFrame for calculating CAGR. Default Adj Close.
    
    calculate_return: Boolean, Whether to calculate return for the specified column. Default True.
    
    Returns
    -------
    vol : Integer, Volatility measure of the stock return over given period interval.

    """
    df = DF.copy()
    
    if column != "Adj Close" and calculate_return == True:
        df["return"] = df[column].pct_change()
        
    elif column != "Adj Close" and calculate_return == False:
        df["return"] = df[column]
    
    elif column == "Adj Close" and calculate_return == True:
        df["return"] = df["Adj Close"].pct_change()
    
    n = len(df)/periods[period]
    
    vol = df["return"].std()*np.sqrt(n)
    
    return vol