#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:12:00 2024

@author: priyanshu
"""

"""
Calmar Ratio:
    
    Ratio of CAGR/ Maximum Drawdown is Calmar Ratio.
    
"""
import sys
sys.path.append("..")

from kpi.compoundedAnnualGrowthRate import cagr
from kpi.maximumDrawdown import maxDraw
import pandas as pd

def calmar(DF: pd.DataFrame, period: str = "monthly", column: str = "Adj Close", calculate_return: bool = True) -> int:
    
    """

    Parameters
    ----------
    DF : pd.DataFrame, Data with Adj Close price of stock.
    
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
    CalmarRatio : int, Calmar Ratio of the stock

    """
    
    df = DF.copy()
    
    return cagr(df, period = period, column = column, calculate_return = calculate_return) / maxDraw(df, column = column, calculate_return = calculate_return)