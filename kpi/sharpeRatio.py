#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:07:39 2024

@author: priyanshu
"""

"""
Sharpe ratio: It is the ratio of average return earned in excess of risk
    free rate per unit of volatility.
    
    It is widely used measure of risk adjusted return
    
    Investors pay close attention to this metric when comparing funds.
    
    Sharpe ratio 1< is good, 2< is very good and 3< is excellent.
    
    Sharpe Ratio = (Rp - Rf) / sigma_p
    
    where, 
    
    Rp = Expected return, 
    Rf = Risk free rate of return, 
    sigma_p = standard deviation of all asset return

    Drawback: One criticism of Sharpe ratio is that it fails to distinguish between upside and downside
    fluctuation. That is where Sortino comes into picture.
"""
import sys
sys.path.append("..")

from otherData.riskFreeReturn import risk_free_rate, riskFreeReturn
from kpi.compoundedAnnualGrowthRate import cagr
from kpi.volatility import volatility

def sharpe(DF, custom_risk_free_rate: bool = False, rate: float = 0.0):
    df = DF.copy()
    
    global risk_free_rate
    
    if custom_risk_free_rate:
    
        if rate !=0:
            risk_free_rate = rate
        
        else:
            if risk_free_rate == 0:
            
                riskFreeReturn()
            
            print("provide custom risk free rate, currently it is latest US Treasury 5 year bold yield")
    
    elif risk_free_rate == 0:
        
        riskFreeReturn()
    
    sharpe = (cagr(df) - risk_free_rate) / volatility(df)
    
    return sharpe