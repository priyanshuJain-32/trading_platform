#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:06:16 2024

@author: priyanshu
"""

    
"""
To calculate risk free return using US 5 year bond yield

"""

import datetime as dt
import yfinance as yf

risk_free_rate = 0

def riskFreeReturn():
    risk_free = yf.download("^FVX", dt.datetime.today() - dt.timedelta(10), dt.datetime.today(), period = '1mo', interval = "1d").dropna(axis = 0)
    
    global risk_free_rate
    
    risk_free_rate = risk_free["Adj Close"].iloc[-1]/100
    
    return