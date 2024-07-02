#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 06:12:22 2024

@author: priyanshu
"""

"""
Monthly Portfolio Rebalancing

    Choose a universe (Large cap, mid cap, small cap, industry specific of stocks 
    and stick to this group of stocks as a source for portfolio for the entire 
    duration of stocks.
    
    Build 
    
    - fixed individual position sized 
    - LONG only portfolio by 
    - picking "m" number of stocks 
    - based on a certain fixed criteria
    
    Rebalance the portfolio every month by removing worse x stocks and replacing them
    with top x stocks from the universe.
    
    Backtest the strategy and compare the KPI's with that of simple buy and hold
    strategy of corresponding index.
"""

import pandas as pd
import numpy as np


def pfRebalance(DF: pd.DataFrame, max_size: int = 6, rebalance: int = 3) -> pd.DataFrame:
    """
    
    Parameters
    ----------
    DF : pandas DataFrame. Data of stock prices at monthly interval
    
    max_size : Integer, Max_Size of portfolio. The default is 6.
    
    rebalance : Integer, Bottom number of stocks to rebalance. The default is 3.

    Returns
    -------
    monthly_ret_df : Pandas DataFrame, Monthly Return of portfolio.
    
    """
    
    df = DF.copy()
    
    portfolio = []
    
    monthly_ret = [0]
    
    for i in range(len(df)): 
        """ 
        We iterate over each row of dataframe as they 
        are all monthly data and we are performing portfolio 
        rebalancing each month.
        """
        
        if portfolio: # if portfolio is not empty
            
            # Calculate the mean of return of portfolio for each ticker in portfolio
            monthly_ret.append(df[portfolio].iloc[i,:].mean())
            
            # Pick bad stocks i.e. the bottom return stocks from portfolio. How many given by x.
            bad_stocks = df[portfolio].iloc[i,:].sort_values(ascending = True)[:rebalance].index.values.tolist()
            
            # Keep only those stocks in portfolio that are not in bad_stocks
            portfolio = [t for t in portfolio if t not in bad_stocks]
            
        # how many to add in portfolio
        fill = max_size - len(portfolio)
        
        # pick the tickers for the best stocks. How many given by "fill".
        new_picks = df.iloc[i,:].sort_values(ascending = False)[:fill].index.values.tolist()
        
        portfolio += new_picks # append the new_picks to portfolio
    
        print(portfolio) # just to keep a check
        
    monthly_ret_df = pd.DataFrame(np.array(monthly_ret), columns = ["monthly_return"])
    
    return monthly_ret_df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    