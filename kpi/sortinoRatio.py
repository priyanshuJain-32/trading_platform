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

from otherData.riskFreeReturn import risk_free_rate, riskFreeReturn
from kpi.compoundedAnnualGrowthRate import cagr

import numpy as np
import pandas as pd

def sortino(DF, custom_risk_free_rate: bool = False, rate: float = 0.0):
    df = DF.copy()
    
    global risk_free_rate
    
    if custom_risk_free_rate:
        
        if rate != 0.0:
            risk_free_rate = rate
            
        else:
            if risk_free_rate == 0:
                riskFreeReturn()
            
            print("provide custom risk free rate, currently it is latest US Treasury 5 year bold yield")
            
    else:
        if risk_free_rate == 0:
        
            riskFreeReturn()
    
    df["returns"] = df["Adj Close"].pct_change()
    
    neg_returns = np.where(df["returns"]>0, 0, df["returns"])
    
    neg_returns = pd.DataFrame(neg_returns[neg_returns!=0])
    
    neg_vol = neg_returns.std()*np.sqrt(252)
    
    sortino = (cagr(df) - risk_free_rate) / neg_vol
    
    return sortino