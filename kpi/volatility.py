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


import numpy as np
import pandas as pd

def volatility(DF: pd.DataFrame, period = "monthly") -> int:
    """

    Parameters
    ----------
    DF : Pandas DataFrame, Data of stocks with Adj Close prices.
    
    period : String, Optional parameter specifying period of volatility 
                
                "quarterly", 
                "monthly", 
                "daily". 
                
            The default is "monthly".

    Returns
    -------
    vol : Integer, Volatility measure of the stock return over given period interval.

    """
    df = DF.copy()
    
    df["return"] = df["Adj Close"].pct_change()
    
    if period == "quarterly":
        n = len(df)/4
    if period == "monthly":
        n = len(df)/12
    elif period == "daily":
        n = len(df)/252
    
    vol = df["return"].std()*np.sqrt(n)
    
    return vol