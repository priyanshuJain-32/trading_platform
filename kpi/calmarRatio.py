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

def calmar(DF: pd.DataFrame) -> int:
    
    """

    Parameters
    ----------
    DF : pd.DataFrame, Data with Adj Close price of stock.

    Returns
    -------
    CalmarRatio : int, Calmar Ratio of the stock

    """
    
    df = DF.copy()
    
    return cagr(df) / maxDraw(df)