#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:01:44 2024

@author: priyanshu
"""

"""
    CAGR: Compounded Annual Growth Rate is the annual rate of return realized by 
    an asset/ portfolio to reach its current market value from its initial value.
    
    CAGR calculation assumes profits are continuously reinvested.
    
    CAGR = (End Value/ Beginning Value)^(1/years) - 1
    
"""
import sys
sys.path.append("..")
import pandas as pd
from otherData.periods import periods

def cagr(DF: pd.DataFrame, period: str = "monthly", column: str = "Adj Close", calculate_return: bool = True) -> int:
    
    """
    Parameters
    ----------
    DF : Pandas DataFrame, Data of stocks with Adj Close prices.
        
    period : String, Optional parameter specifying period of cagr 
                
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
    cagr : int, Compounded Annual Growth Rate.

    """
    
    df = DF.copy()
    
    if column != "Adj Close" and calculate_return == True:
        df["return"] = df[column].pct_change()
        
    elif column != "Adj Close" and calculate_return == False:
        df["return"] = df[column]
    
    elif column == "Adj Close" and calculate_return == True:
        df["return"] = df["Adj Close"].pct_change()
    
    df["cum_return"] = (1+df["return"]).cumprod()
    
    n = len(df)/periods[period]
        
    CAGR = df["cum_return"].iloc[-1]**(1/n) - 1
    return round(CAGR,4)