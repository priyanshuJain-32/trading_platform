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

from averageTrueRange import atr # to be used when implementing atr
from stocktrends import Renko
import pandas as pd
import yfinance as yf

def renkoFunc(DF: pd.DataFrame, ticker: str, use_atr: bool = False) -> pd.DataFrame :
    
    """
    Parameters
    ----------
    DF : pd.DataFrame, data on date, open, high, low, close, and volume for a stock.
    
    ticker : str, stock ticker symbol.
        
    use_atr : bool, optional
        If we have to Average True Range or not. The default is False.
        If no then a fixed brick size of 4 will be used.

    Returns
    -------
    renkoDf : Pandas DataFrame. Gives the Renko bricks data for the given stock.

    """
    
    df = DF.copy()
    df.drop("Close", axis = 1, inplace = True)
    
    df.reset_index(inplace = True)

    df.columns = ["date", "open", "high", "low", "close", "volume"]
    
    dfRenko = Renko(df)
    
    if use_atr:
        
        # we will need to download the hourly data if we want to use ATR this can be changed
        # its something that author recommended from where I learned
        hourly_data = yf.download(ticker, period = '1y', interval = '1h')
        hourly_data.dropna(axis = 0, inplace=True)
        
        # iloc -1 to pick the last value of the ATR series returned
        dfRenko.brick_size = 3*round(atr(hourly_data, window = 120).iloc[-1], 0)
    else:
        dfRenko.brick_size = 4
    
    renkoDf = dfRenko.get_ohlc_data()

    return renkoDf