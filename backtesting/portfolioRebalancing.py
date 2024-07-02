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

import sys
import pandas as pd
sys.path.append("..")

from kpi.compoundedAnnualGrowthRate import cagr
from kpi.volatility import volatility
from kpi.sharpeRatio import sharpe
from kpi.maximumDrawdown import maxDraw


def pfRebalance(DF: pd.DataFrame, max_size: int = 6, rebalance: int = 3) -> pd.DataFrame:
    """
    
    Parameters
    ----------
    DF : pandas DataFrame. Data of stock prices
    
    max_size : Integer, Max_Size of portfolio. The default is 6.
    
    rebalance : Integer, Bottom number of stocks to rebalance. The default is 3.

    Returns
    -------
    Pandas DataFrame, Monthly Return of portfolio.
    
    """
    
    