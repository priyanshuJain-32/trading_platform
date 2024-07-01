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

def volatility(DF):
    df = DF.copy()
    
    df["return"] = df["Adj Close"].pct_change()
    
    vol = df["return"].std()*np.sqrt(252)
    
    return vol