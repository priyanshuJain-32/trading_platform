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
    
    period : String, Optional parameter specifying period of volatility 
                
                "quarterly", 
                "monthly", 
                "daily". 
                
            The default is "monthly".
    
    column : String, column to use in the given dataFrame for calculating CAGR. Default Adj Close.
    
    calculate_return: Boolean, Whether to calculate return for the specified column. Default True.

    Returns
    -------
    CalmarRatio : int, Calmar Ratio of the stock

    """
    
    df = DF.copy()
    
    return cagr(df, period = period, column = column, calculate_return = calculate_return) / maxDraw(df, column = column, calculate_return = calculate_return)