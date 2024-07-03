#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 06:13:43 2024

@author: priyanshu
"""
"""
Intraday Resistance Breakout

    Resistance Breakout is a technical trading term which means that the price of the stock
    has breached a presumed resistance level (determined by a price chart)

    Choose high volume, high activity stocks for this strategy (pre market movers, historically
    high volume stocks, etc.)

    Define breakout rule - I will be using price breaching 20 period rolling max/min price in
    conjunction with volume breaching rolling max volume - go long/short stocks based on signals

    Define exit/stop loss signal - Implemented one will be using previous price plus/minus 20
    period ATR as the rolling stop loss price.

    Backtest the strategy by calculating cumulative return for each stock. 

"""

def intraResBreak(DF):

    pass
