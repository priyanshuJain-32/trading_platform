#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:09:57 2024

@author: priyanshu
"""

"""
Sortino ratio:
    
    It is a variation of Sharpe ratio which takes into account standard deviation of 
    only negative returns.
    
    One criticism of Sharpe ratio is that it fails to distinguish between upside and downside
    fluctuation, 
    
    Sortino makes the distinction and considers only harmful volatility
    
    Sortino Ratio = (Rp - Rf) / sigma_p
    
    where, 
    
    Rp = Expected return, 
    Rf = Risk free rate of return, 
    sigma_p = standard deviation of NEGATIVE asset return
"""
import sys
sys.path.append("..")

from otherData.riskFreeReturn import riskFreeReturn
from kpi.compoundedAnnualGrowthRate import cagr

import numpy as np
import pandas as pd

def sortino(DF: pd.DataFrame, custom_risk_free_rate: bool = False, rate: float = 0.0, period: str = "monthly", column: str = "Adj Close", calculate_return: bool = True) -> int:
    
    """
    Parameters
    ----------
    DF : pd.DataFrame
        Data of stock prices.
        
    custom_risk_free_rate : bool, optional, specifies whether a custom risk free rate
        is to be used. The default is False.
    
    rate : float, optional. If custom risk free rate is True use this to provide the rate. 
        The default is 0.0.
        
    period : String, Optional parameter specifying period of volatility 
                
                "quarterly", 
                "monthly", 
                "daily". 
                
            The default is "monthly".
    
    column : String, column to use in the given dataFrame for calculating CAGR. Default Adj Close.
    
    calculate_return: Boolean, Whether to calculate return for the specified column. Default True.

    Returns
    -------
    sortino : Integer. Sortino Ratio of stock.

    """
    
    df = DF.copy()
    
    if custom_risk_free_rate:
        
        if rate != 0.0:
            risk_free_rate = rate
            
        else:
            risk_free_rate = riskFreeReturn()
            
            print("provide custom risk free rate, currently it is latest US Treasury 5 year bold yield")
            
    else:
        risk_free_rate = riskFreeReturn()
    
    if column != "Adj Close" and calculate_return == True:
        df["return"] = df[column].pct_change()
        
    elif column != "Adj Close" and calculate_return == False:
        df["return"] = df[column]
    
    elif column == "Adj Close" and calculate_return == True:
        df["return"] = df["Adj Close"].pct_change()
    
    neg_returns = np.where(df["return"]>0, 0, df["return"])
    
    neg_returns = pd.DataFrame(neg_returns[neg_returns!=0])
    
    if period == "quarterly":
        n = 4
    if period == "monthly":
        n = 12
    elif period == "daily":
        n = 252
    
    neg_vol = neg_returns.std().iloc[-1]*np.sqrt(n)
    
    sortino = (cagr(df, period = period, column = column, calculate_return = calculate_return) - risk_free_rate) / neg_vol
    
    return sortino