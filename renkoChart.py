#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:15:48 2024

@author: priyanshu

RENKO CHART

    Renko charts are built using price movement and not price against standardized time intervals -
    It filters out the noise and lets us visualize the trend.

    Price movements are represented by bricks and stacked at 45 degrees to each other.
    
    A new brick is added only if the price exceeds a pre-determined value in the same direction. Or
    double of the value in opposite direction.
    
    Renko charts have time axis but the time axis is not of fixed width. Some bricks may cover 
    longer time scale than others it all depends on how long it took price to move the required threshold.
    
    Renko charts use only closing price based on the time frame chosen.
    
    Brick size can be defined using:
        
        Traditional size = based on price bricks
        Average True Range = based on ATR calculation for a given window size
        
    Note: Do not use very small brick size as it will be noisy.
        Backtesting can be used to find the most appropriate brick size.
"""

from averageTrueRange import atr
from stocktrends import Renko

def renkoFunc(DF):
    df = DF.copy()
    df.drop("Close", axis = 1, inplace = True)
    
    df.reset_index(inplace = True)
    print(df)
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    
    dfRenko = Renko(df)
    
    dfRenko.brick_size = 4
    
    renkoDf = dfRenko.get_ohlc_data()
    print(renkoDf)
    return renkoDf