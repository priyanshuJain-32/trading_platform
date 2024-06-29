#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:39:09 2024

@author: priyanshu

Implementation of Bollinger bands:
    
    Bollinger bands are two lines plotted n standard deviations above and below the m period
    simple moving average line. The bands widen during increased volatility and shrink during
    reduced volatility. Typically n=2 and m=20.
    
    ATR focuses on price movement and conveys how wildly he market is swinging.
    Takes into account price movement in each period by considering the following ranges:
    
        - Difference between high and low.
        - Difference between high and previous close.
        - Difference between low and previous close.
    
    Used for volatility studies. If both indicators say volatility is increasing then
    we consider that it is infact increasing.
    
"""

